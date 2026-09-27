# Workspace architecture

English · [简体中文](architecture.zh-CN.md)

## Public template

| Location | Responsibility |
|---|---|
| Root README pair | Learner setup and study workflow |
| Root AGENTS pair | AI tutor's standing instructions |
| `.agents/skills/` | On-demand environment setup, course preparation, study-session, and card-export procedures |
| `guides/` | Learner setup, local tool contracts, and manual Anki import |
| `templates/` | Bilingual blank forms, filled once in the learner's language |
| `scripts/` and `tests/` | Portable local operations and behavioral checks |
| `pyproject.toml`, `uv.lock`, `.python-version` | Direct dependencies, resolved lock, and project Python selection |
| `examples/` | Original learning examples and attributed, rights-cleared external sources |
| `docs/` | Maintainer contracts and design records |

## Local learning workspace

Initialization creates `study/COURSE.md` from the course form. This profile owns goals and the source map, and links notes, review questions, and the latest session. Lesson JSON in `study/specs/` generates Notebooks in `study/notes/`; Notebook learner cells remain user-owned. PDF page assets and manifests live in `study/sources/`, review/card inputs in `study/review/`, and dated sessions in `study/sessions/`. The [tool reference](../guides/tools.md) owns schemas and commands.

Original materials remain in `materials/` or at a learner-designated location. Anki exports live in `output/` and never connect to Anki. Derived artifacts belong in ignored directories described by [publication conventions](conventions.md). uv manages `.venv`; the learner uses an independent file-capable agent and JupyterLab. Markdown-only study remains possible without executing the Notebook tools.

The structural decision is recorded [here](specs/implemented/0001-learning-workspace.md). Proposed automation is separate from the current workspace contract.
