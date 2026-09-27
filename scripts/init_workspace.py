"""Create local study directories without replacing existing learner files."""

from pathlib import Path
import shutil


def initialize(root):
    root = Path(root).resolve()
    for directory in ("materials", "study/notes", "study/specs", "study/sources",
                      "study/review", "study/sessions", "output"):
        (root / directory).mkdir(parents=True, exist_ok=True)
    target = root / "study/COURSE.md"
    if not target.exists():
        shutil.copyfile(root / "templates/course.md", target)
    print(f"Ready: {root / 'study'}. Existing files were not replaced.")


if __name__ == "__main__":
    initialize(Path(__file__).resolve().parents[1])
