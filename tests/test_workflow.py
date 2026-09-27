"""Behavioral checks using synthetic local fixtures, never private course files."""

import csv
import hashlib
import io
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import time
import unittest
from urllib.request import Request, urlopen
import zipfile

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
import nbformat
from PIL import Image

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from export_cards import export
from init_workspace import initialize
from nb_build import build
from nb_check import check, check_assets
from prepare_pdf import prepare


class WorkflowTests(unittest.TestCase):
    def setUp(self):
        (ROOT / "work").mkdir(exist_ok=True)
        self.temp = tempfile.TemporaryDirectory(dir=ROOT / "work")
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)

    def make_pdf(self):
        path = self.root / "input.pdf"
        with PdfPages(path) as pdf:
            for label in ("FIRST PAGE", "", "THIRD PAGE"):
                figure = plt.figure(figsize=(3, 2))
                if label:
                    figure.text(0.1, 0.5, label)
                pdf.savefig(figure)
                plt.close(figure)
        return path

    def make_spec(self):
        prepare(self.make_pdf(), self.root / "pages", dpi=72)
        spec = {"version": 1, "title": "Fixture", "language": "en",
                "manifest": "pages/manifest.json", "units": [
                    {"id": "K01", "title": "Previous", "pages": [1], "status": "recap", "recap": "Earlier notes"},
                    {"id": "K02", "title": "Current", "pages": [2, 3], "status": "todo"}]}
        path = self.root / "lesson.json"
        path.write_text(json.dumps(spec), encoding="utf-8")
        return path, spec

    def make_cards(self):
        Image.new("RGB", (12, 8), "blue").save(self.root / "chart.png")
        cards = {"version": 1, "cards": [{"id": "fixture.k01.q01", "front": '中文, "quote"\tline\nnext <tag>',
                  "back": r"\(x^2\) & answer", "source": "fixture, section A",
                  "front_images": [{"path": "chart.png", "alt": "A blue test image"}], "tags": ["test_tag"]}]}
        path = self.root / "cards.json"
        path.write_text(json.dumps(cards, ensure_ascii=False), encoding="utf-8")
        return path, cards

    def test_pdf_preserves_blank_page_and_source(self):
        source = self.make_pdf()
        before = source.read_bytes()
        manifest = prepare(source, self.root / "pages", dpi=72)
        self.assertEqual([p["page"] for p in manifest["pages"]], [1, 2, 3])
        self.assertFalse(manifest["pages"][1]["has_text"])
        self.assertIn("THIRD", (self.root / "pages/p0003.txt").read_text())
        with Image.open(self.root / "pages/p0003.png") as image:
            self.assertEqual(image.size, (216, 144))
        self.assertEqual(source.read_bytes(), before)
        with self.assertRaises(FileExistsError):
            prepare(source, self.root / "pages")

    def test_build_skeleton_recap_and_assets(self):
        path, _ = self.make_spec()
        nb = build(path, self.root / "notes/lesson.ipynb")
        self.assertEqual(sum(c.id.startswith("K01-") for c in nb.cells), 1)
        self.assertEqual(sum(c.id.startswith("K02-part") for c in nb.cells), 6)
        self.assertGreater(check_assets(nb, self.root / "notes"), 0)

    def test_build_rejects_coverage(self):
        path, spec = self.make_spec()
        for pages in ([2], [1, 2, 3], [2, 4], [2, 2, 3]):
            spec["units"][1]["pages"] = pages
            path.write_text(json.dumps(spec))
            with self.assertRaises(ValueError):
                build(path, self.root / "lesson.ipynb")
            self.assertFalse((self.root / "lesson.ipynb").exists())

    def test_rebuild_preserves_answers_and_backs_up(self):
        path, spec = self.make_spec()
        output = self.root / "lesson.ipynb"
        nb = build(path, output)
        response = next(c for c in nb.cells if c.id == "K02-response")
        response.source = "My actual answer"
        nb.cells.append(nbformat.v4.new_code_cell("answer = 42", id="my-extra"))
        nbformat.write(nb, output)
        before = output.read_bytes()
        spec["units"][1].update(status="ready", cells=[{"id": "explanation", "type": "markdown", "source": "Updated"}])
        path.write_text(json.dumps(spec))
        rebuilt = build(path, output)
        self.assertEqual(next(c.source for c in rebuilt.cells if c.id == "K02-response"), "My actual answer")
        self.assertEqual(rebuilt.cells[-1].id, "my-extra")
        self.assertEqual(next(self.root.glob("*.backup-*.ipynb")).read_bytes(), before)

    def test_manual_generated_edit_refuses_overwrite(self):
        path, _ = self.make_spec()
        output = self.root / "lesson.ipynb"
        nb = build(path, output)
        nb.cells[0].source = "A manual edit"
        nbformat.write(nb, output)
        before = output.read_bytes()
        with self.assertRaisesRegex(ValueError, "Manual edit"):
            build(path, output)
        self.assertEqual(output.read_bytes(), before)

    def test_changed_pdf_rejected(self):
        path, _ = self.make_spec()
        with (self.root / "input.pdf").open("ab") as stream:
            stream.write(b"\n% changed")
        with self.assertRaisesRegex(ValueError, "PDF changed"):
            build(path, self.root / "lesson.ipynb")

    def test_reconciled_edit_can_rebuild(self):
        path, spec = self.make_spec()
        output = self.root / "lesson.ipynb"
        nb = build(path, output)
        nb.cells[0].source = "# Agreed title"
        nbformat.write(nb, output)
        spec["title"] = "Agreed title"
        path.write_text(json.dumps(spec))
        self.assertEqual(build(path, output).cells[0].source, "# Agreed title")

    def test_duplicate_cell_id_refused(self):
        path, spec = self.make_spec()
        spec["units"][1]["cells"] = [{"id": "response", "type": "markdown", "source": "Reserved"}]
        path.write_text(json.dumps(spec))
        with self.assertRaisesRegex(ValueError, "Duplicate cell"):
            build(path, self.root / "lesson.ipynb")

    def test_assets_markdown_html_and_reference_images(self):
        for source in ('![x](missing.png)', '<img src="missing.png">', '![x][figure]\n\n[figure]: missing.png'):
            nb = nbformat.v4.new_notebook(cells=[nbformat.v4.new_markdown_cell(source)])
            with self.assertRaises(FileNotFoundError):
                check_assets(nb, self.root)

    def test_real_kernel_relative_paths_and_magics(self):
        (self.root / "value.txt").write_text("42")
        nb = nbformat.v4.new_notebook(cells=[nbformat.v4.new_code_cell(
            "%matplotlib inline\nfrom pathlib import Path\nassert Path('value.txt').read_text() == '42'\nprint('kernel-success')")])
        path = self.root / "run.ipynb"
        nbformat.write(nb, path)
        before = path.read_bytes()
        result = check(path)
        self.assertIn("kernel-success", result.cells[0].outputs[-1].text)
        self.assertEqual(path.read_bytes(), before)

    def test_real_kernel_failure_is_not_suppressed(self):
        path = self.root / "fail.ipynb"
        nbformat.write(nbformat.v4.new_notebook(cells=[nbformat.v4.new_code_cell("raise ValueError('expected fixture failure')")]), path)
        result = subprocess.run([sys.executable, str(ROOT / "scripts/nb_check.py"), str(path)], capture_output=True, text=True)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("expected fixture failure", result.stderr)

    def test_cards_unicode_html_media_and_zip(self):
        path, cards = self.make_cards()
        output = self.root / "export"
        export(path, output)
        content = (output / "cards.tsv").read_text(encoding="utf-8")
        lines = content.splitlines()
        rows = list(csv.reader(io.StringIO("\n".join(line for line in lines if not line.startswith("#"))), delimiter="\t"))
        self.assertEqual(len(rows), 1)
        self.assertEqual(len(rows[0]), 5)
        self.assertIn('中文, &quot;quote&quot;\tline<br>next &lt;tag&gt;', rows[0][1])
        self.assertIn(r"\(x^2\)", rows[0][2])
        media = list((output / "media").iterdir())
        self.assertEqual(len(media), 1)
        self.assertIn(media[0].name, rows[0][1])
        self.assertEqual(media[0].read_bytes(), (self.root / "chart.png").read_bytes())
        with zipfile.ZipFile(self.root / "export.zip") as archive:
            self.assertIsNone(archive.testzip())
            self.assertIn("cards.tsv", archive.namelist())
        with self.assertRaises(FileExistsError):
            export(path, output)

    def test_invalid_cards_fail_without_output(self):
        path, cards = self.make_cards()
        cards["cards"].append(dict(cards["cards"][0]))
        path.write_text(json.dumps(cards))
        with self.assertRaisesRegex(ValueError, "duplicate"):
            export(path, self.root / "export")
        self.assertFalse((self.root / "export").exists())
        cards["cards"].pop()
        cards["cards"][0]["front_images"][0]["path"] = "missing.png"
        path.write_text(json.dumps(cards))
        with self.assertRaises(FileNotFoundError):
            export(path, self.root / "export")
        self.assertFalse((self.root / "export").exists())

    def test_initialization_preserves_course(self):
        (self.root / "templates").mkdir()
        (self.root / "templates/course.md").write_text("blank form")
        initialize(self.root)
        target = self.root / "study/COURSE.md"
        target.write_text("My course")
        initialize(self.root)
        self.assertEqual(target.read_text(), "My course")

    def test_cli_preparation_build_and_check(self):
        source = self.make_pdf()
        result = subprocess.run([sys.executable, str(ROOT / "scripts/prepare_pdf.py"),
                                 str(source), str(self.root / "pages")], capture_output=True)
        self.assertEqual(result.returncode, 0, result.stderr.decode(errors="replace"))
        spec = self.root / "spec.json"
        spec.write_text(json.dumps({"version": 1, "title": "CLI fixture", "language": "zh-CN",
                                    "manifest": "pages/manifest.json", "units": [
                                        {"id": "K01", "title": "Unit", "pages": [1, 2, 3], "status": "todo"}]}))
        notebook = self.root / "notes/fixture.ipynb"
        for name, args in (("nb_build.py", [spec, notebook]), ("nb_check.py", [notebook])):
            result = subprocess.run([sys.executable, str(ROOT / "scripts" / name), *map(str, args)], capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode(errors="replace"))

    def test_jupyterlab_starts_in_project_directory(self):
        runtime = self.root / "runtime"
        runtime.mkdir()
        env = dict(os.environ, JUPYTER_CONFIG_DIR=str(self.root / "config"),
                   JUPYTER_RUNTIME_DIR=str(runtime))
        with (self.root / "server.log").open("wb") as log:
            process = subprocess.Popen([
                sys.executable, "-m", "jupyterlab", "--no-browser", "--ServerApp.port=0",
                "--ServerApp.ip=127.0.0.1", "--ServerApp.root_dir=" + str(self.root),
            ], stdout=log, stderr=subprocess.STDOUT, env=env)
            info = None
            try:
                deadline = time.monotonic() + 30
                verified = False
                while time.monotonic() < deadline and process.poll() is None:
                    records = list(runtime.glob("jpserver-*.json"))
                    if records:
                        try:
                            info = json.loads(records[0].read_text(encoding="utf-8"))
                            request = Request(info["url"] + "api", headers={"Authorization": "token " + info["token"]})
                            with urlopen(request, timeout=2) as response:
                                self.assertEqual(response.status, 200)
                            self.assertEqual(Path(info["root_dir"]).resolve(), self.root.resolve())
                            verified = True
                            break
                        except (OSError, ValueError):
                            pass
                    time.sleep(0.2)
                self.assertTrue(verified, "JupyterLab did not become ready within 30 seconds")
            finally:
                if info is not None:
                    request = Request(info["url"] + "api/shutdown", data=b"",
                                      headers={"Authorization": "token " + info["token"]})
                    with urlopen(request, timeout=5) as response:
                        self.assertEqual(response.status, 200)
                elif process.poll() is None:
                    process.terminate()
                process.wait(timeout=15)


if __name__ == "__main__":
    unittest.main()
