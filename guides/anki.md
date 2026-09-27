# Importing STS cards into Anki

English · 简体中文: use anki.zh-CN.md in the repository, or IMPORT.zh-CN.md in an exported bundle.

STS exports files only. It never reads your Anki database, starts Anki, installs an add-on, or changes your existing cards. You decide when and where to import.

## What you receive

The export directory contains `cards.tsv`, `media/`, a manifest, card-template snippets, and these instructions. A ZIP beside the directory is a transport copy: **extract it first; do not import the ZIP into Anki**.

We choose UTF-8 TSV for readable text and standard-library export. CSV is also supported by Anki, but neither embeds pictures. Pictures must be copied separately and referenced from fields. An `.apkg` can bundle media, but is not the format implemented here. See the official [text import](https://docs.ankiweb.net/importing/text-files.html) and [package description](https://docs.ankiweb.net/exporting.html).

## Ask for cards

Tell your agent which completed notes and optional source sections to use, your review language, and the desired scope. It should verify sources, create focused questions rather than whole lecture paragraphs, and prepare `study/review/cards.json` using the tool reference. Request an export only after reviewing the proposed content.

```sh
uv run python scripts/export_cards.py study/review/cards.json output/anki-review-01
```

Use a new output directory for each export. Stable IDs identify the same note across revisions; use a course-specific prefix and keep an ID unchanged when editing its question or answer.

## One-time setup in desktop Anki

1. Open **Tools → Manage Note Types** and add a copy of the basic, single-card note type. Name it `STS`.
2. In **Fields**, arrange exactly these four fields in this order: `ID`, `Front`, `Back`, `Source`. Keep `ID` first. Tags are not a fifth custom field.
3. In **Cards**, replace the front template with `{{Front}}`. Replace the back template with:

```html
{{FrontSide}}<hr id="answer">{{Back}}<hr><small>{{Source}}</small>
```

4. Add `img { max-width: 100%; height: auto; }` to Styling if desired. The export also includes the templates and a stylesheet as files.

The ID is used for matching, not displayed. This note type produces one question/answer card per exported note. Do not choose a reversed-card or cloze type. Field and card-template controls are described in Anki's [editing manual](https://docs.ankiweb.net/editing.html) and [field replacement reference](https://docs.ankiweb.net/templates/fields.html).

## Import a small batch first

1. Back up your collection before updating existing notes. Create or select a destination deck.
2. Copy the **files inside** the exported `media/` into the active profile's `collection.media` directory, without subdirectories. Never replace a different existing file blindly. The generated names are content-hashed to reduce collisions. On Windows, profile folders normally live under `%APPDATA%\Anki2`; custom installations may differ. See [Anki file locations](https://docs.ankiweb.net/files.html).
3. Choose **File → Import**, select `cards.tsv`, and choose `STS` and your deck. Confirm Tab separation, HTML enabled, and column mapping `ID → ID`, `Front → Front`, `Back → Back`, `Source → Source`, `Tags → Tags` in the preview. Modern Anki reads the supplied headers; always inspect the preview.
4. Review the duplicate/update option before importing. Existing notes may be updated using their first field and selected matching scope. Keep IDs stable; deleting a row from a later export does **not** delete the existing Anki note. Details: [text import](https://docs.ankiweb.net/importing/text-files.html).
5. Inspect several cards: question, answer, picture, formula, and source. Compare the imported note count with `manifest.json`. Only then import a larger batch.

Math uses `\(...\)` inline or `\[...\]` display notation, not Notebook `$...$` delimiters. No external LaTeX installation is needed for Anki's built-in MathJax. See [Math & Symbols](https://docs.ankiweb.net/math.html).

## Limits

The exporter checks file structure, identifiers, required fields, and referenced image files. It cannot prove that the teaching content or source citation is correct. It supports basic Q&A and PNG/JPEG images, not cloze, image occlusion, audio, scheduling, or synchronization. A successful export is not evidence of a tested import in your Anki version; verify the first batch yourself.

If images are missing, check the active profile, filenames, and HTML option. If formulas show as text, ask the agent to correct the MathJax delimiters. Do not upload a private bundle publicly merely because STS is MIT-licensed.
