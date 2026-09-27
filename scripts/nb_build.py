"""Build a study Notebook from a JSON spec, preserving learner-owned cells."""

import argparse
import copy
import hashlib
from html import escape
import json
import os
from pathlib import Path
import re
import uuid

import nbformat


PARTS = {
    "en": ["Goal and source", "Notation and objects", "Derivation",
           "Predict / Run / Break it", "Reproduce", "Takeaway and limits"],
    "zh-CN": ["目标与来源", "符号与对象", "推导", "预测 / 运行 / 改变条件", "独立复现", "收口与边界"],
}


def fingerprint(cell):
    payload = [cell.cell_type, cell.source, cell.get("attachments", {})]
    return hashlib.sha256(json.dumps(payload, sort_keys=True).encode()).hexdigest()


def generated(kind, source, cell_id):
    make = nbformat.v4.new_markdown_cell if kind == "markdown" else nbformat.v4.new_code_cell
    cell = make(source, id=cell_id)
    cell.metadata["sts"] = {"owner": "generated", "baseline": fingerprint(cell)}
    return cell


def load_spec(path, output):
    spec = json.loads(path.read_text(encoding="utf-8"))
    if spec.get("version") != 1 or not isinstance(spec.get("title"), str) or not spec["title"].strip():
        raise ValueError("Spec requires version=1 and a non-empty title")
    if spec.get("language") not in PARTS:
        raise ValueError("language must be en or zh-CN")
    manifest_path = (path.parent / spec["manifest"]).resolve()
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    source = (manifest_path.parent / manifest["source"]).resolve()
    if hashlib.sha256(source.read_bytes()).hexdigest() != manifest["sha256"]:
        raise ValueError("PDF changed; prepare it again in a new directory")
    total = manifest["page_count"]
    if total < 1 or [p["page"] for p in manifest["pages"]] != list(range(1, total + 1)):
        raise ValueError("Manifest page numbering is not contiguous")
    seen_ids, covered, assets = set(), [], []
    if not spec.get("units"):
        raise ValueError("Spec requires units")
    for unit in spec["units"]:
        uid = unit["id"]
        if not re.fullmatch(r"[A-Za-z][A-Za-z0-9_-]{0,23}", uid) or uid in seen_ids:
            raise ValueError(f"Invalid or duplicate unit ID: {uid}")
        seen_ids.add(uid)
        if not isinstance(unit.get("title"), str) or not unit["title"].strip():
            raise ValueError(f"{uid}: title required")
        if unit.get("status") not in {"todo", "ready", "recap"}:
            raise ValueError(f"{uid}: invalid status")
        pages = unit.get("pages")
        if not isinstance(pages, list) or any(type(p) is not int for p in pages):
            raise ValueError(f"{uid}: pages must be an integer list")
        covered.extend(pages)
        if unit["status"] == "recap" and (not unit.get("recap", "").strip() or unit.get("cells")):
            raise ValueError(f"{uid}: recap requires a pointer and no teaching cells")
        if unit["status"] == "ready" and not unit.get("cells"):
            raise ValueError(f"{uid}: ready requires teaching cells")
    if sorted(covered) != list(range(1, total + 1)):
        raise ValueError("Units must cover every PDF page exactly once, including recap pages")
    for page in manifest["pages"]:
        for key in ("image", "text"):
            asset = (manifest_path.parent / page[key]).resolve()
            if not asset.is_relative_to(manifest_path.parent) or not asset.is_file():
                raise ValueError(f"Missing or invalid page asset: {asset}")
            assets.append(Path(os.path.relpath(asset, output.parent)).as_posix())
    return spec, manifest, manifest_path, assets


def build(spec_path, output):
    spec_path, output = Path(spec_path).resolve(), Path(output).resolve()
    spec, manifest, manifest_path, assets = load_spec(spec_path, output)
    cells = [generated("markdown", f"# {spec['title']}", "sts-title")]
    mapping = ["| Unit / 单元 | PDF pages / 页号 | Status / 状态 |", "|---|---|---|"]
    for unit in spec["units"]:
        mapping.append(f"| {unit['id']} · {unit['title']} | {', '.join(map(str, unit['pages']))} | {unit['status']} |")
    cells.append(generated("markdown", "\n".join(mapping), "sts-map"))
    for unit in spec["units"]:
        uid = unit["id"]
        locator = f"{Path(manifest['source']).name}, PDF pages {unit['pages']}"
        heading = f"## {uid} · {unit['title']}\n\nSource / 来源: {locator}"
        if unit["status"] == "recap":
            cells.append(generated("markdown", heading + "\n\nRecap: " + unit["recap"], uid + "-intro"))
            continue
        cells.append(generated("markdown", heading, uid + "-intro"))
        if unit.get("cells"):
            for item in unit["cells"]:
                cid = item["id"]
                if not re.fullmatch(r"[A-Za-z0-9_-]{1,30}", cid) or item["type"] not in {"markdown", "code"}:
                    raise ValueError(f"{uid}: invalid cell ID or type")
                if not isinstance(item["source"], str):
                    raise ValueError("Cell source must be a string")
                cells.append(generated(item["type"], item["source"], uid + "-" + cid))
        else:
            for number, label in enumerate(PARTS[spec["language"]], 1):
                body = f"### {uid}.{number} {label}\n\nTODO / 待讲解"
                if number == 1:
                    for page in unit["pages"]:
                        image = manifest_path.parent / manifest["pages"][page - 1]["image"]
                        relative = Path(os.path.relpath(image, output.parent)).as_posix()
                        body += f'\n\n<img src="{escape(relative, quote=True)}" alt="PDF page {page}">\n\nSource page {page} / 原始课件页；待结合知识点讲解。'
                cells.append(generated("markdown", body, f"{uid}-part{number}"))
        response = nbformat.v4.new_markdown_cell(
            "### My response / 我的作答\n\n", id=uid + "-response")
        response.metadata["sts"] = {"owner": "learner"}
        cells.append(response)
    ids = [c.id for c in cells]
    if len(set(ids)) != len(ids):
        raise ValueError("Duplicate cell IDs, including reserved intro/response IDs")
    original = output.read_bytes() if output.exists() else None
    if original:
        old = nbformat.reads(original.decode("utf-8"), as_version=4)
        if old.metadata.get("sts", {}).get("spec") != Path(os.path.relpath(spec_path, output.parent)).as_posix():
            raise ValueError("Existing notebook belongs to another spec; use a new output path")
        old_by_id = {c.id: c for c in old.cells}
        if len(old_by_id) != len(old.cells):
            raise ValueError("Existing Notebook contains duplicate cell IDs")
        new_by_id = {c.id: c for c in cells}
        for cell in old.cells:
            state = cell.metadata.get("sts", {})
            if state.get("owner") == "generated" and state.get("baseline") != fingerprint(cell):
                replacement = new_by_id.get(cell.id)
                if replacement is None or fingerprint(replacement) != fingerprint(cell):
                    raise ValueError(f"Manual edit in generated cell {cell.id}; merge it into the spec before rebuilding")
        for index, cell in enumerate(cells):
            previous = old_by_id.get(cell.id)
            if previous is None:
                continue
            if previous.metadata.get("sts", {}).get("owner") == "learner":
                cells[index] = copy.deepcopy(previous)
        # Preserve user-added and orphaned learner cells, including their outputs.
        for previous in old.cells:
            if previous.id not in ids and previous.metadata.get("sts", {}).get("owner") != "generated":
                cells.append(copy.deepcopy(previous))
    nb = nbformat.v4.new_notebook(cells=cells, metadata={
        "kernelspec": {"name": "python3", "display_name": "Python 3", "language": "python"},
        "sts": {"spec": Path(os.path.relpath(spec_path, output.parent)).as_posix(),
                "assets": assets + spec.get("assets", [])}})
    nbformat.validate(nb)
    output.parent.mkdir(parents=True, exist_ok=True)
    if original is not None:
        if output.read_bytes() != original:
            raise RuntimeError("Notebook changed during build; save/close it and retry")
        backup = output.with_name(output.stem + ".backup-" + uuid.uuid4().hex[:8] + ".ipynb")
        backup.write_bytes(original)
        print(f"Backup: {backup}")
    staging = output.with_name(output.name + "." + uuid.uuid4().hex + ".tmp")
    staging.write_text(nbformat.writes(nb), encoding="utf-8")
    staging.replace(output)
    print(f"Built {output}: {len(spec['units'])} units. Generated outputs cleared; learner cells preserved.")
    return nb


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("spec", type=Path)
    parser.add_argument("output", type=Path)
    args = parser.parse_args()
    build(args.spec, args.output)


if __name__ == "__main__":
    main()
