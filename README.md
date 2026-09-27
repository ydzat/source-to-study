# Source to Study

**Turn your own course materials into source-grounded notes, executable learning exercises, review questions, and spaced-repetition cards.**

[简体中文](README.zh-CN.md) · English

> **Project status: design scaffold.** This repository does not yet contain a runnable end-to-end pipeline or a complete example. Do not treat the planned commands and components below as implemented.

Source to Study is a course-agnostic, AI-assisted study workflow. It is designed to keep the learner in charge: the AI explains and drafts; source references, executable checks, and closed-book recall make those drafts auditable. Oral exams are one possible use case, not the default assumption for every course.

## Intended learning loop

1. Bring your own lawfully obtained materials into a local, Git-ignored `materials/` directory.
2. Index the sources and verify page or section references before writing claims.
3. Build a teaching notebook around the source's actual learning goal: **goal → inputs → intermediate objects and operations → derivation or computation → verifiable result**.
4. Use **Predict → Run → Break it → Reproduce** to test understanding. Diagrams and worked examples belong next to the concepts they explain.
5. Maintain a concise review source and derive cards from it. Track what was taught separately from what the learner can reproduce without help.

This is a target workflow, **not a claim that it already runs in this scaffold**.

## What will and will not be published

The public repository will contain reusable instructions, portable code, tests, and a small **original** sample course. It will not contain the author's university slides, slide screenshots, extracted PDF text, private notes, personal study history, credentials, or generated artifacts from those materials. A `.gitignore` is a safety layer, not proof that a file is safe to publish; every release will require a content and history review. See [Content and privacy conventions](docs/conventions.md).

## Planned architecture

The core will be local-first and AI-provider-independent. Jupyter notebooks provide the first interactive learning surface; a separate optional UI may be added only after the underlying workflow works and is tested. See [Architecture](docs/architecture.md).

## Current repository contents

- `AGENTS.md`: generic instructions for an AI assistant working in a user's copy, with a Chinese reading counterpart.
- `docs/`: paired English and Simplified Chinese design and safety documents.
- `examples/`: reserved for a future original, rights-cleared end-to-end sample.

There is **no installation step yet**. The next milestone is one original sample course and a minimal pipeline that can run against it from a clean checkout.

## License and contributions

This project uses the [MIT License](LICENSE), matching the license already committed to the [GitHub repository](https://github.com/ydzat/source-to-study/blob/main/LICENSE). It applies only to material the project owner can license; it does not grant rights to users' course materials or unrelated third-party assets. Contributions and external course examples should wait until the rights and review process is documented.
