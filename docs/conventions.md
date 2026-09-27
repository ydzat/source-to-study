# Maintenance conventions

English · [简体中文](conventions.zh-CN.md)

## Publication boundary

Publish reusable instructions, blank forms, original examples, attributed external examples with verified reuse rights, and maintainer documents. Personal course material, extracted text, screenshots, notes, responses, logs, credentials, and derived assets remain private by default.

`materials/`, `study/`, `private/`, `cache/`, `work/`, and `output/` are ignored. Before publishing, inspect the actual staged files and relevant Git history; inspect embedded Notebook outputs and binary assets separately. Ignore rules do not remove tracked content or establish rights. Keep the existing MIT license; record any independently licensed assets explicitly.

## Languages

Maintain English and Chinese prose as `name.md` and `name.zh-CN.md`, updating both in the same change. English is the editing source, but the Chinese version must be independently usable. Keep paths, identifiers, and commands unchanged.

The short forms in `templates/` use bilingual field guidance in one file. Personal completed notes use the learner's language, not mandatory parallel translations. This prevents two copies of live course state.

Instruction entry points under `.agents/skills/` use one English `SKILL.md` per task. The bilingual [skills guide](../guides/skills.md) explains them to learners; do not create duplicate machine entries for translations. Link shared schemas and scripts instead of copying them into skills.

## Verification

Check relative links, required language pairs, the setup path, and consistency between claimed capabilities and actual files. Walk through a form as a learner; document checks cannot prove teaching quality. When executable features arrive, add behavioral tests and run the original example from a clean workspace.

Do not copy this private parent project's course material or machine-specific configuration into the public template. New dependencies and external services require an actual use case and appropriate authorization.
