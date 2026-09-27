# Workspace architecture

English · [简体中文](architecture.zh-CN.md)

## Public template

| Location | Responsibility |
|---|---|
| Root README pair | Learner setup and study workflow |
| Root AGENTS pair | AI tutor's standing instructions |
| `templates/` | Bilingual blank forms, filled once in the learner's language |
| `examples/` | Original examples of the learning workflow |
| `docs/` | Maintainer contracts and design records |

## Local learning workspace

The assistant creates `study/COURSE.md` from the course form. This profile owns goals and the source map, and links the learner's notes, review questions, and latest session. Notes live in `study/notes/`, review material in `study/review/`, and dated sessions in `study/sessions/`. These files are hand-maintained learning sources, not generated exports.

Original materials remain in `materials/` or at a learner-designated location. Derived caches and exports belong in the ignored directories described by [publication conventions](conventions.md). No command-line pipeline or UI framework is required to use the forms.

The structural decision is recorded [here](specs/implemented/0001-learning-workspace.md). Proposed automation is separate from the current workspace contract.
