"""Validate public document links, translations, and JSON illustrations."""

import json
from pathlib import Path
import unittest
from urllib.parse import unquote, urlsplit

from markdown_it import MarkdownIt

ROOT = Path(__file__).resolve().parents[1]


class DocumentationTests(unittest.TestCase):
    def test_public_docs(self):
        files = list(ROOT.glob("*.md"))
        for directory in ("guides", "docs", "templates", "examples", ".agents/skills"):
            files.extend((ROOT / directory).rglob("*.md"))
        parser = MarkdownIt()
        for path in files:
            with self.subTest(path=path.relative_to(ROOT)):
                text = path.read_text(encoding="utf-8")
                self.assertTrue(text.endswith("\n"))
                if "templates" not in path.parts and path.name != "SKILL.md" and not path.name.endswith(".zh-CN.md"):
                    self.assertTrue(path.with_name(path.stem + ".zh-CN.md").is_file())
                stack = list(parser.parse(text))
                while stack:
                    token = stack.pop()
                    stack.extend(token.children or [])
                    if token.type == "fence" and token.info == "json":
                        json.loads(token.content)
                    if token.type == "link_open":
                        target = urlsplit(token.attrGet("href"))
                        if not target.scheme and target.path:
                            self.assertTrue((path.parent / unquote(target.path)).exists(), token.attrGet("href"))


if __name__ == "__main__":
    unittest.main()
