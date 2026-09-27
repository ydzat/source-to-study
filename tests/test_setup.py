"""Exercise deployment failure reporting and real server lifecycle."""

import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from check_setup import check, check_server


class SetupTests(unittest.TestCase):
    def setUp(self):
        (ROOT / "work").mkdir(exist_ok=True)
        self.temp = tempfile.TemporaryDirectory(prefix="setup space-", dir=ROOT / "work")
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name).resolve()

    def test_wrong_environment_is_rejected(self):
        with self.assertRaisesRegex(RuntimeError, "interpreter"):
            check(self.root)

    def test_real_server_starts_and_stops(self):
        scratch = self.root / "check"
        scratch.mkdir()
        check_server(self.root, scratch)
        # Its process has exited when the function returns; log stays local.
        self.assertTrue((scratch / "server.log").is_file())

    def test_missing_uv_replaces_previous_success_with_failure(self):
        (self.root / "scripts").mkdir()
        shutil.copyfile(ROOT / "scripts/setup.ps1", self.root / "scripts/setup.ps1")
        for name in ("pyproject.toml", "uv.lock", ".python-version"):
            shutil.copyfile(ROOT / name, self.root / name)
        report = self.root / "work/setup/report.json"
        report.parent.mkdir(parents=True)
        report.write_text('{"status":"passed"}', encoding="utf-8")
        result = subprocess.run([
            shutil.which("pwsh") or "powershell", "-NoProfile", "-File", str(self.root / "scripts/setup.ps1"),
            "-UvPath", str(self.root / "missing-uv.exe"),
        ], capture_output=True, timeout=30)
        self.assertNotEqual(result.returncode, 0)
        state = json.loads(report.read_text(encoding="utf-8-sig"))
        self.assertEqual(state["status"], "failed", result.stderr.decode(errors="replace"))
        self.assertEqual(state["stage"], "preflight")
        self.assertFalse((self.root / "study").exists())


if __name__ == "__main__":
    unittest.main()
