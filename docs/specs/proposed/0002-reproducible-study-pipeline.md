# Reproducible study pipeline

Status: proposed

## Problem

Manual AI-assisted study can produce broken asset paths, unsupported citations, and review content that cannot be exported reproducibly.

## Proposal

Build a minimal pipeline around a rights-cleared original mini-course: source indexing, editable lesson inputs, validated Notebook output, review-card validation, and optional Anki export. Preserve learner responses across rebuilds. Keep reusable logic independent of course, machine paths, model provider, and optional UI.

Define concrete formats and commands in a follow-up design before implementation; no command in this proposal is available to learners.

## Alternatives considered

A document-only template supports immediate use but cannot verify executable artifacts. A UI-first implementation is deferred until the underlying workflow and failure cases can be tested. No UI framework, including ComfyUI, is a required dependency.

## Acceptance criteria

- A fresh workspace can run the original example using documented dependencies and commands.
- Source locators are checked; missing files and unsupported citations fail visibly.
- A generated Notebook runs from its own directory in a clean kernel, and rebuilding preserves learner answers.
- Cards have validated identifiers, prompts, answers, and sources; an exported package can be inspected before import.
- Tests include missing assets, malformed input, and reconstruction from source files.
- Public artifacts contain no private course excerpts, personal paths, or credentials.
- English and Chinese instructions both reproduce the same workflow.

## Risks

Source formats differ; extracted text may omit equations. Execution is not proof of conceptual correctness. Export introduces dependencies and format choices requiring review. UI work can obscure these unresolved contracts.
