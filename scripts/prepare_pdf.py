"""Extract page text and render a PDF without changing its page numbering."""

import argparse
from contextlib import closing
import hashlib
import json
import os
from pathlib import Path

import pypdfium2 as pdfium


def prepare(source, output, dpi=120):
    source, output = Path(source).resolve(), Path(output).resolve()
    if not source.is_file():
        raise FileNotFoundError(source)
    if not 36 <= dpi <= 300:
        raise ValueError("dpi must be between 36 and 300")
    if output.exists():
        raise FileExistsError(f"Use a new output directory: {output}")
    digest = hashlib.sha256(source.read_bytes()).hexdigest()
    with pdfium.PdfDocument(source) as document:
        if not len(document):
            raise ValueError("PDF contains no pages")
        output.mkdir(parents=True)
        pages = []
        for index in range(len(document)):
            number = index + 1
            with closing(document[index]) as page:
                with closing(page.get_textpage()) as text_page:
                    text = text_page.get_text_bounded()
                image_name, text_name = f"p{number:04d}.png", f"p{number:04d}.txt"
                with closing(page.render(scale=dpi / 72)) as bitmap:
                    with bitmap.to_pil() as image:
                        image.save(output / image_name)
                (output / text_name).write_text(text, encoding="utf-8")
                pages.append({"page": number, "image": image_name, "text": text_name,
                              "has_text": bool(text.strip())})
    manifest = {"version": 1, "source": Path(os.path.relpath(source, output)).as_posix(),
                "sha256": digest, "page_count": len(pages), "dpi": dpi, "pages": pages}
    (output / "manifest.json").write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return manifest


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("source", type=Path)
    parser.add_argument("output", type=Path, help="New directory for page assets and manifest")
    parser.add_argument("--dpi", type=int, default=120)
    args = parser.parse_args()
    result = prepare(args.source, args.output, args.dpi)
    empty = sum(not p["has_text"] for p in result["pages"])
    print(f"Prepared {result['page_count']} pages; {empty} without extracted text. Inspect page images; no OCR was performed.")
    print(args.output / "manifest.json")


if __name__ == "__main__":
    main()
