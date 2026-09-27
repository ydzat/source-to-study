"""Check a real project kernel and authenticated local JupyterLab without learner edits."""

import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import time
from urllib.request import Request, urlopen


ROOT = Path(__file__).resolve().parents[1]


def check_server(root, scratch):
    runtime = scratch / "runtime"
    runtime.mkdir()
    env = dict(os.environ, JUPYTER_CONFIG_DIR=str(scratch / "config"),
               JUPYTER_RUNTIME_DIR=str(runtime))
    with (scratch / "server.log").open("wb") as log:
        process = subprocess.Popen([
            sys.executable, "-m", "jupyterlab", "--no-browser",
            "--ServerApp.port=0", "--ServerApp.ip=127.0.0.1",
            "--ServerApp.root_dir=" + str(root),
        ], stdout=log, stderr=subprocess.STDOUT, env=env)
        info = None
        try:
            deadline = time.monotonic() + 40
            while time.monotonic() < deadline and process.poll() is None:
                for record in runtime.glob("jpserver-*.json"):
                    try:
                        info = json.loads(record.read_text(encoding="utf-8"))
                        if not info.get("token"):
                            raise RuntimeError("JupyterLab started without token authentication.")
                        if Path(info["root_dir"]).resolve() != root:
                            raise RuntimeError("JupyterLab has the wrong root directory.")
                        request = Request(info["url"] + "api", headers={
                            "Authorization": "token " + info["token"]})
                        with urlopen(request, timeout=2) as response:
                            if response.status == 200:
                                return
                    except (OSError, ValueError):
                        # The runtime file may appear before the server accepts requests.
                        continue
                time.sleep(0.2)
            raise RuntimeError(f"JupyterLab did not become ready; inspect {scratch / 'server.log'}")
        finally:
            if info is not None and process.poll() is None:
                try:
                    request = Request(info["url"] + "api/shutdown", data=b"", headers={
                        "Authorization": "token " + info["token"]})
                    with urlopen(request, timeout=5) as response:
                        if response.status != 200:
                            raise RuntimeError("JupyterLab shutdown failed.")
                except OSError:
                    process.terminate()
            elif process.poll() is None:
                process.terminate()
            try:
                process.wait(timeout=10)
            except subprocess.TimeoutExpired:
                process.kill()
                process.wait(timeout=10)


def check(root=ROOT):
    root = Path(root).resolve()
    if Path(sys.prefix).resolve() != (root / ".venv").resolve():
        raise RuntimeError("Run this check with the project's uv-managed .venv interpreter.")
    for directory in ("materials", "study/notes", "study/specs", "study/sources",
                      "study/review", "study/sessions", "output"):
        if not (root / directory).is_dir():
            raise RuntimeError(f"Missing workspace directory: {directory}")
    if not (root / "study/COURSE.md").is_file():
        raise RuntimeError("Missing study/COURSE.md; run init_workspace.py first.")

    import nbformat
    from nbclient import NotebookClient
    # Import the actual tool modules, including their direct dependencies.
    import prepare_pdf  # noqa: F401
    import nb_build  # noqa: F401
    import nb_check  # noqa: F401
    import export_cards  # noqa: F401

    work = root / "work/setup"
    work.mkdir(parents=True, exist_ok=True)
    scratch = Path(tempfile.mkdtemp(prefix="check-", dir=work))
    source = (
        "import sys\nfrom pathlib import Path\n"
        f"assert Path(sys.prefix).resolve() == Path({str(root / '.venv')!r}).resolve()\n"
        "import numpy as np\nimport matplotlib\nmatplotlib.use('Agg')\n"
        "import matplotlib.pyplot as plt\n"
        "assert int(np.array([1, 2, 3]).sum()) == 6\n"
        "plt.plot([1, 2, 3], [1, 4, 9])\nplt.savefig('smoke.png')\nplt.close()\n"
        "assert Path('smoke.png').stat().st_size > 0\n"
    )
    nb = nbformat.v4.new_notebook(cells=[nbformat.v4.new_code_cell(source)])
    NotebookClient(nb, timeout=60, kernel_name="python3",
                   resources={"metadata": {"path": str(scratch)}}).execute()
    nbformat.write(nb, scratch / "smoke.ipynb")
    check_server(root, scratch)
    print("PASS: project interpreter, workspace, tool imports, real kernel/plot, JupyterLab HTTP.")
    return scratch


if __name__ == "__main__":
    check()
