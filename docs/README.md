# Maintaining Source to Study

English · [简体中文](README.zh-CN.md)

These documents are for template maintainers. Learners start at the [root README](../README.md).

- [Architecture](architecture.md): current files and ownership.
- [Conventions](conventions.md): publication boundaries and bilingual maintenance.
- [Design records](specs/README.md): proposals, decisions, and verification.

For a non-trivial change, first record the problem, proposed behavior, alternatives, acceptance criteria, and risks under `specs/proposed/`. Implement against observable criteria. After verification, move the record to `specs/implemented/` and rewrite it as the current decision with consequences and verification evidence. Do not label partially implemented work as implemented.

Keep product usage in learner-facing files and development rationale here. Each fact has one owning document; other documents link to it. A typo or local wording correction needs no new proposal.
