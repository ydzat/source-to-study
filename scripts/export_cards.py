"""Export reviewed card JSON to Anki TSV and local media; never contact Anki."""

import argparse
import csv
import hashlib
from html import escape
import json
from pathlib import Path
import re
import shutil
import zipfile


def text_html(value):
    return escape(value).replace("\r\n", "\n").replace("\r", "\n").replace("\n", "<br>")


def export(source, output):
    source, output = Path(source).resolve(), Path(output).resolve()
    archive = output.with_name(output.name + ".zip")
    if output.exists() or archive.exists():
        raise FileExistsError("Choose a new export directory; existing exports are never replaced")
    data = json.loads(source.read_text(encoding="utf-8"))
    if data.get("version") != 1 or not isinstance(data.get("cards"), list) or not data["cards"]:
        raise ValueError("Expected version=1 and a non-empty cards list")
    rows, media, ids = [], {}, set()
    for card in data["cards"]:
        cid = card["id"]
        if not isinstance(cid, str) or not re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9_.:-]{0,119}", cid) or cid in ids:
            raise ValueError(f"Invalid or duplicate card ID: {cid!r}")
        ids.add(cid)
        for field in ("front", "back", "source"):
            if not isinstance(card.get(field), str) or not card[field].strip():
                raise ValueError(f"{cid}: non-empty {field} required")
        sides = {}
        for side in ("front", "back"):
            sides[side] = text_html(card[side])
            images = card.get(side + "_images", [])
            if not isinstance(images, list):
                raise ValueError(f"{cid}: {side}_images must be a list")
            for item in images:
                if not isinstance(item, dict) or not isinstance(item.get("path"), str) or not isinstance(item.get("alt"), str) or not item["alt"].strip():
                    raise ValueError(f"{cid}: each image needs path and non-empty alt text")
                relative = Path(item["path"])
                if relative.is_absolute() or ":" in item["path"]:
                    raise ValueError(f"{cid}: use local relative image paths")
                image = (source.parent / relative).resolve()
                if not image.is_file():
                    raise FileNotFoundError(image)
                suffix = image.suffix.lower()
                if suffix not in {".png", ".jpg", ".jpeg"}:
                    raise ValueError("Export images as PNG or JPEG first")
                content = image.read_bytes()
                if not (content.startswith(b"\x89PNG\r\n\x1a\n") if suffix == ".png" else content.startswith(b"\xff\xd8\xff")):
                    raise ValueError(f"Invalid image signature: {image}")
                name = "sts_" + hashlib.sha256(content).hexdigest() + suffix
                media[name] = image
                sides[side] += f'<br><img src="{name}" alt="{escape(item["alt"], quote=True)}">'
        tags = card.get("tags", [])
        if not isinstance(tags, list) or any(not isinstance(t, str) or not re.fullmatch(r"[\w:-]+", t) for t in tags):
            raise ValueError(f"{cid}: tags must be whitespace-free words; use underscores")
        rows.append([cid, sides["front"], sides["back"], text_html(card["source"]), " ".join(tags)])
    # All input checks finish before any deliverable is created.
    output.mkdir(parents=True)
    (output / "media").mkdir()
    for name, path in media.items():
        shutil.copyfile(path, output / "media" / name)
    with (output / "cards.tsv").open("w", encoding="utf-8", newline="") as stream:
        stream.write("#separator:Tab\n#html:true\n#columns:ID\tFront\tBack\tSource\tTags\n#tags column:5\n")
        csv.writer(stream, delimiter="\t", lineterminator="\n", quoting=csv.QUOTE_ALL).writerows(rows)
    guide_dir = Path(__file__).resolve().parents[1] / "guides"
    shutil.copyfile(guide_dir / "anki.md", output / "IMPORT.md")
    shutil.copyfile(guide_dir / "anki.zh-CN.md", output / "IMPORT.zh-CN.md")
    (output / "front-template.html").write_text("{{Front}}\n", encoding="utf-8")
    (output / "back-template.html").write_text(
        '{{FrontSide}}<hr id="answer">{{Back}}<hr><small>{{Source}}</small>\n', encoding="utf-8")
    (output / "style.css").write_text(
        ".card { font-family: sans-serif; font-size: 20px; text-align: left; }\n"
        "img { max-width: 100%; height: auto; }\n", encoding="utf-8")
    (output / "manifest.json").write_text(json.dumps({
        "version": 1, "notes": len(rows), "media": sorted(media), "ids": [row[0] for row in rows],
        "input_sha256": hashlib.sha256(source.read_bytes()).hexdigest(),
    }, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    with zipfile.ZipFile(archive, "w", compression=zipfile.ZIP_DEFLATED) as bundle:
        for path in sorted(output.rglob("*")):
            if path.is_file():
                bundle.write(path, path.relative_to(output).as_posix())
    print(f"Exported {len(rows)} notes, {len(media)} images: {output}")
    print(f"Transport archive: {archive}. Extract it; Anki does not import this ZIP directly.")
    return rows


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("source", type=Path)
    parser.add_argument("output", type=Path)
    args = parser.parse_args()
    export(args.source, args.output)


if __name__ == "__main__":
    main()
