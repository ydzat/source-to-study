---
name: sts-course-setup
description: Set up an STS course or prepare a new lecture's source map and Notebook framework. Use for course initialization, PDF preparation, unit division, and recap mapping; not for teaching an existing unit or exporting cards.
---

# Prepare a course or lecture

Work from the STS repository root, three directories above this file. Read [AGENTS.md](../../../AGENTS.md). Use existing scripts; skill loading does not authorize dependency installation or external writes.

## What preprocessing means here

A learner's short request to preprocess a course or PDF means preparing it for study: source extraction, a source-grounded unit map, and a validated Notebook framework. Extraction alone is an intermediate step, not completion. If a necessary scope choice is missing, ask a concise question and resume the remaining steps after the reply. Stop at extraction only when the learner explicitly requests extraction alone.

## Establish the input

- Read an existing study/COURSE.md before changing it. For a new course, use [the course form](../../../templates/course.md) to establish the learner's goal, language, prior knowledge, source priority, and assessment policy. Do not reset existing work.
- For environment setup, read only the relevant parts of [Getting started](../../../guides/getting-started.md). For local preparation and builds, read Environment and initialization, PDF preparation, and Notebook source and build in [the tool reference](../../../guides/tools.md).
- Resolve actual source files and output names. Reuse a matching source manifest only after checking its source hash and assets; use a new destination if the source changed. Do not infer page numbering from filtered text.

## Agree on scope, then build

Inspect the source text and relevant page images. Propose units with exact PDF page coverage and their goals. Confirm an unresolved division with the learner before building; an already agreed division needs no repeated approval.

Check suspected recap against the previous source and notes. Retain novel material and represent verified repetition with a pointer. Preserve all PDF pages and their original numbering.

Run the documented PDF preparation and Notebook build commands. Create the spec in study/specs/ and Notebook in study/notes/; leave untaught units as todo. Framework creation is not a request to write the entire lecture. Respect save/close and conflict handling for any existing Notebook.

## Verify and hand off

Run the Notebook checker. Distinguish structural validation of a skeleton from execution of authored experiments. Link the course profile, spec, Notebook, and source map; report coverage and unresolved source issues briefly. Update course navigation, not mastery or a fictional study-session record. End at the agreed framework boundary unless the learner also requested teaching.
