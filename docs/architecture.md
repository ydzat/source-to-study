# Architecture and first milestone

## Design decision

The first release is a **local-first workflow template**, not a hosted application. A CLI drives deterministic indexing, builds, and checks; a teaching notebook provides the interactive study surface. An AI assistant may read local sources and draft content under `AGENTS.md`, but no single model or paid service is a required dependency.

The core should expose ordinary Python functions so that a future browser UI can call the same functions without duplicating business rules. Do not implement a UI before the original sample works end to end.

## Planned components

| Layer | Input | Output | Verification |
|---|---|---|---|
| Source intake | User-owned files under `materials/` | Local page/section index in `cache/` | Source exists; page counts and references checked |
| Teaching | Index + declarative lesson spec | Notebook under `output/` | All source ranges accounted for; clean-kernel execution; linked assets exist |
| Review | Learner-approved review source | Questions and card data | Schema, citations, and empty/duplicate cards checked |
| Export | Validated card data | Optional Anki package | Package contents and counts checked before import |
| Progress | Actual teaching and learner responses | Local learning log in `private/` | No mastery upgrade from AI generation alone |

`examples/` will contain one original mini-course and its expected outputs. It must have no copied university slides, logos, exam questions, or private study notes. The sample is the acceptance test: a new user should be able to follow its instructions from a clean checkout.

## UI decision

The first UI is the notebook itself. A small setup/status UI can be evaluated later if the CLI proves difficult for new users; that UI must be optional. ComfyUI is **not** a foundation dependency: its [official project description](https://github.com/Comfy-Org/ComfyUI) centers on visual generative-media workflows, while this project is mainly source indexing, citation checking, text/notebook authoring, and card export. [JupyterLab](https://docs.jupyter.org/en/stable/start/) already provides an interactive notebook interface. If an optional image-generation step is ever added, it can be integrated at the edge without changing the core pipeline.

## Milestones

1. Publish-safe bilingual scaffold and explicit private/public boundary (**this milestone**).
2. Original mini-course + portable source index + one notebook build/check.
3. Review/card schema + Anki export + clean-checkout tests.
4. Optional UI evaluation with user testing; release audit before publication. The owner has already selected MIT for this repository.
