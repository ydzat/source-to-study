"""Check local assets and execute trusted Notebook code in a fresh kernel."""

import argparse
from html.parser import HTMLParser
import os
from pathlib import Path
import sys
from urllib.parse import unquote, urlsplit

from markdown_it import MarkdownIt
from nbclient import NotebookClient
import nbformat


class Images(HTMLParser):
    def __init__(self):
        super().__init__()
        self.paths = []

    def handle_starttag(self, tag, attrs):
        if tag == "img":
            value = dict(attrs).get("src")
            if value is None:
                raise ValueError("Image tag missing src")
            self.paths.append(value)


def check_assets(nb, directory):
    parser = MarkdownIt()
    paths = list(nb.metadata.get("sts", {}).get("assets", []))
    for cell in nb.cells:
        if cell.cell_type != "markdown":
            continue
        stack = list(parser.parse(cell.source))
        while stack:
            token = stack.pop()
            stack.extend(token.children or [])
            if token.type == "image":
                src = token.attrGet("src")
                if src.startswith("attachment:"):
                    if src.removeprefix("attachment:") not in cell.get("attachments", {}):
                        raise ValueError(f"Missing attachment: {src}")
                else:
                    paths.append(src)
            elif token.type in {"html_inline", "html_block"}:
                html = Images()
                html.feed(token.content)
                paths.extend(html.paths)
    for value in paths:
        link = urlsplit(value)
        if link.scheme or link.netloc:
            raise ValueError(f"Use a local asset instead of external/absolute URL: {value}")
        target = directory / unquote(link.path)
        if not link.path or not target.is_file():
            raise FileNotFoundError(f"Missing local asset: {value}")
    return len(paths)


def check(path, timeout=120):
    path = Path(path).resolve()
    nb = nbformat.read(path, as_version=4)
    nbformat.validate(nb)
    count = check_assets(nb, path.parent)
    code_count = sum(c.cell_type == "code" for c in nb.cells)
    if code_count:
        # Detect accidentally selected global kernels before running lesson code.
        preflight = nbformat.v4.new_code_cell(
            "import sys\nfrom pathlib import Path\n"
            f"assert Path(sys.executable).resolve() == Path({sys.executable!r}).resolve(), 'Wrong kernel: start via uv run'\n"
            "import numpy as np\nnp.seterr(divide='raise', invalid='raise', over='raise', under='ignore')\n")
        nb.cells.insert(0, preflight)
        env = dict(os.environ, MPLBACKEND="Agg")
        NotebookClient(nb, timeout=timeout, kernel_name="python3", allow_errors=False,
                       resources={"metadata": {"path": str(path.parent)}}).execute(env=env)
        nb.cells.pop(0)
    print(f"PASS: {count} local asset references, {code_count} code cells; input Notebook unchanged.")
    if not code_count:
        print("No executable cells: this is a structural check, not proof of a completed lesson.")
    return nb


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("notebook", type=Path)
    parser.add_argument("--timeout", type=int, default=120)
    args = parser.parse_args()
    check(args.notebook, args.timeout)


if __name__ == "__main__":
    main()
