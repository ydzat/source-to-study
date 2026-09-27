---
name: sts-export-cards
description: Generate or revise review cards from user-selected STS notes and optional source sections, then export TSV and images for manual Anki import. Use only when cards or their export are requested; not for routine lesson completion or live Anki management.
---

# Prepare a file-only card bundle

Work from the STS repository root, three directories above this file. Read [AGENTS.md](../../../AGENTS.md), File-only card export in [the tool reference](../../../guides/tools.md), and [the import guide](../../../guides/anki.md). Reuse scripts/export_cards.py; do not create a separate exporter.

## Select and verify material

Use the notes and optional source sections the learner selected. Resolve ambiguity that would change the subject or scope; do not silently turn the entire course into cards. Read existing card input before revising it and retain stable course-prefixed IDs for the same learning targets.

Verify the question and answer against the notes and cited source. If they disagree, resolve or flag the conflict before exporting that claim. Split independent recall targets, retain necessary context and boundary conditions, and avoid answers that reproduce whole lessons. Match the requested review language.

## Prepare the input

Create or update the documented card JSON in study/review/. Use plain-text fields and explicit Anki MathJax delimiters; do not pass Notebook Markdown through unchanged. Include meaningful sources and optional PNG/JPEG images only when they help recall. Verify image meaning as well as file existence; keep original files unchanged and provide alt text.

If the request is only to draft or review proposed cards, stop there. If export is also requested, respect the learner's review checkpoint or existing approval; do not invent another approval requirement after they accepted the content.

## Export and deliver

Run the documented exporter to a new output directory. If validation fails, fix the input and rerun; do not suppress the check or overwrite an existing bundle. Inspect the TSV's parsed fields, note count, manifest IDs, and image references. Source correctness remains the agent's responsibility, not the exporter's.

Link the bundle and import instructions, state note/media counts, and explain that ZIP is for transport and must be extracted. Do not claim a live import was tested. Never connect to Anki, read its database, install MCP/add-ons, import, synchronize, or delete cards. Export does not update learning mastery or create a study-session record.
