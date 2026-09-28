# Local tools and file contracts

English · [简体中文](tools.zh-CN.md)

This reference is for the agent operating your files. Learners can follow the conversational walkthrough in [Getting started](getting-started.md). Run commands from the project root with `uv run`. Paths below are illustrative inputs; use the learner's actual files.

## Environment and initialization

For Agent-led Windows deployment, load [sts-setup](../.agents/skills/sts-setup/SKILL.md). With uv available, `./scripts/setup.ps1` runs locked sync, initialization, and `uv run --locked python scripts/check_setup.py`. It accepts `-UvPath` for a verified executable outside PATH. It returns nonzero on failure and records stage/status/time in ignored `work/setup/report.json`; a shell-level refusal may prevent any report update. The health check runs a fresh kernel with a plot, checks tool imports and workspace paths, and starts/stops an authenticated loopback JupyterLab server. Its local artifacts/logs stay under `work/setup/` and must not be published. Reruns preserve learner files; no server stays running after a successful check.

`pyproject.toml` owns direct dependencies; `uv.lock` locks resolved versions; `.python-version` selects Python 3.12. Run `uv sync --locked`, then:

```sh
uv run python scripts/init_workspace.py
```

This creates the local directory structure and copies the course form only if `study/COURSE.md` does not already exist. Do not use global pip or install an Anki integration. Extra course dependencies require approval and `uv add`, which updates the project dependency files.

## PDF preparation

```sh
uv run python scripts/prepare_pdf.py materials/lecture01.pdf study/sources/lecture01
```

The new destination contains `manifest.json`, `p0001.txt`, `p0001.png`, and corresponding files for every PDF page, including blank pages. The manifest records the source's relative path, SHA-256, page count, render DPI, and asset names. An existing destination is refused: prepare changed sources in a new directory and update the spec.

This script uses PDFium and Pillow supplied by the Python environment, not a separate TeX or Poppler installation. Text is a search aid, not authoritative formula transcription. No OCR or automatic knowledge-unit classification is performed. Inspect the source images and agree on unit boundaries with the learner; keep new material mixed into recap sections.

## Notebook source and build

Create `study/specs/lecture01.json`. The following is a structural illustration, not an actual three-page course:

```json
{
  "version": 1,
  "title": "Course — Lecture 01",
  "language": "en",
  "manifest": "../sources/lecture01/manifest.json",
  "assets": [],
  "units": [
    {"id": "K01", "title": "First unit", "pages": [1, 2], "status": "todo"},
    {"id": "K02", "title": "Second unit", "pages": [3], "status": "todo"}
  ]
}
```

Use `language: "zh-CN"` for Chinese scaffold headings. Page lists must cover the actual PDF exactly once. Units may use an empty page list for explicit background, but must not substitute that for missing source coverage. Status is `todo`, `ready`, or `recap`; `ready` means authored, not mastered or automatically verified. A recap unit requires a non-empty `recap` pointer and cannot contain teaching cells.

```sh
uv run python scripts/nb_build.py study/specs/lecture01.json study/notes/lecture01.ipynb
uv run python scripts/nb_check.py study/notes/lecture01.ipynb
```

The `manifest` path is relative to the spec. Paths in cell content and `assets` are relative to the **output Notebook directory**. List code-read data and other local dependencies in `assets`; the checker also parses Markdown and HTML image references, but cannot infer arbitrary paths constructed by Python code.

To teach a unit, add its `cells` list. Each entry has a stable `id`, `type` (`markdown` or `code`), and string `source`:

```json
{"id": "notation", "type": "markdown", "source": "### Notation\n\nDefine each new object here."}
```

The list replaces that unit's six default placeholders. Apply [the teaching guide](teaching.md): goal/source, notation, derivation, Predict/Run/Break it where useful, independent reproduction, and takeaway. Place figures beside their explanations. Include complete self-test answers in collapsed blocks or a separate linked answer section, and an assessment-appropriate closure. Withhold answers during a live quiz until the learner responds; this does not remove the written answer key. Reserved generated suffixes include `intro` and `response`; other cell IDs must be unique within the unit. Keep the unit `todo` until its actual explanation is complete. Readiness requires manual content review; the builder does not enforce teaching quality.

The builder checks source hashes, coverage, cell identity, and manifest assets. It preserves cells marked `sts.owner=learner`, including answers and outputs, and appends unknown user-added cells. It refuses direct modifications to generated cell source or attachments. Reconcile such edits into the spec and preserved learner cells before rebuilding; do not remove the protection. Before each successful replacement it keeps a sibling backup. Generated code outputs are cleared on rebuilding so outdated results are not presented as current. Save and close the Notebook before rebuilding; scripts cannot protect unsaved browser state.

## Execution checks

The checker uses nbclient to run trusted code in a fresh Python kernel with the Notebook's directory as the working directory. It leaves the input file unchanged and stops on execution errors. It also checks local image references and declared assets. A preflight checks the interpreter and promotes NumPy divide/overflow/invalid warnings to errors; underflow remains allowed. This is verification, **not isolation from side effects**. Inspect unfamiliar code before running it.

An empty framework has no executable cells and receives a structural check only. Execution does not prove source accuracy, mathematical correctness, completeness, or mastery. See [nbclient's execution contract](https://nbclient.readthedocs.io/en/latest/client.html).

## File-only card export

Only generate cards when requested. Prepare a reviewed JSON file in `study/review/`, using this shape:

```json
{
  "version": 1,
  "cards": [{
    "id": "my-course.k01.q01",
    "front": "A focused recall question",
    "back": "A verified answer. Inline math: \\(x^2\\).",
    "source": "lecture01.pdf, PDF p.3; notes/lecture01.ipynb, K01",
    "front_images": [],
    "back_images": [{"path": "../notes/img/diagram.png", "alt": "What this figure shows"}],
    "tags": ["my_course", "K01"]
  }]
}
```

`front`, `back`, and `source` are non-empty plain text, not Markdown or raw HTML. The exporter escapes HTML characters and converts text line breaks. Write Anki MathJax delimiters explicitly, with JSON-escaped backslashes; keep each math expression on one physical line. Image paths are relative to the card JSON. Use PNG/JPEG and meaningful alt text; image arrays are optional. Images appear after the corresponding side's text. Sources are recorded, not semantically validated by the exporter.

IDs are stable and unique, using letters, numbers, `.`, `_`, `:`, or `-`; use a course prefix. Tags have no whitespace. The exporter rejects missing fields, duplicate IDs, invalid image signatures, and missing media before creating output.

```sh
uv run python scripts/export_cards.py study/review/cards.json output/anki-review-01
```

The output contains UTF-8 `cards.tsv` with `ID`, `Front`, `Back`, `Source`, and `Tags` columns; flat content-hashed media files; templates; a manifest; and bilingual instructions. A ZIP transport copy is created alongside it. No Anki connection, import, deletion, scheduling, or synchronization occurs. Follow [the import guide](anki.md).
