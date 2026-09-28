# Using the built-in study skills

English · [简体中文](skills.zh-CN.md)

Skills package the tasks your Agent repeats. You describe the learning goal; the Agent loads the matching workflow and uses the existing local tools. They do not replace your Agent, install another service, or connect to Anki.

## What to say

| Your request | Workflow |
|---|---|
| “Install and verify this project.” | `sts-setup`: uv, isolated environment, workspace, real kernel/server checks, restart handoff |
| “Prepare this lecture and propose a Notebook framework.” | `sts-course-setup`: course profile, source inspection, unit division, framework checks |
| “Continue K03” or “Revise this explanation in my notes.” | `sts-study-session`: recover context, teach the requested unit, update and verify notes |
| “What does this symbol mean?” | Answer the question in conversation; file edits require an explicit change request. |
| “Quiz me” or “Finish today's study and record the next step.” | `sts-study-session`: actual practice and evidence-based session records |
| “Make cards from these notes and export them.” | `sts-export-cards`: source-checked card input and a TSV/media bundle |

Supply the relevant file or unit when the context is unclear. No special invocation syntax is required by STS; natural-language requests are the normal entry point. If you prefer, explicitly ask the Agent to use a named skill.

## Discovery

Open the STS folder itself in your Agent. The files live at `.agents/skills/<name>/SKILL.md`; the leading dot does not mean they are disposable. Keep `.agents/` when downloading or copying the template.

Codex documents repository discovery under `.agents/skills/`, and OpenCode documents the same location as an agent-compatible source. Both describe loading skill instructions on demand. These are documented host capabilities, not a guarantee that every version or configuration selects the right skill for every request. See [official OpenAI documentation](https://learn.chatgpt.com/docs/build-skills) and [OpenCode documentation](https://opencode.ai/docs/skills).

After adding/updating skills, ask the Agent which `sts-` skills are available. If a skill is missing, reopen the project or start a new session, check the project directory and host skill permissions, and avoid changing global settings merely to bypass a restriction.

## If your Agent does not discover skills

Use the file-reading path:

> Read AGENTS.md, then read .agents/skills/sts-course-setup/SKILL.md and follow it to prepare materials/[my lecture.pdf].

Substitute the other skill name when teaching or exporting cards. This works only with an Agent that can actually read the project files; it does not pretend that native skill loading occurred. If your Agent does not load AGENTS.md automatically, provide that file explicitly too.

## What stays where

`AGENTS.md` retains the permanent teaching and safety principles. Skills own task procedures. The [tool reference](tools.md) owns commands and formats; `scripts/` performs deterministic operations. Skills reference these files to keep shared instructions consistent.

The machine entry points are English; they instruct the Agent to use your course's chosen teaching language. This guide and the user tutorials are available in both languages. Skill loading alone never authorizes installations, publication, card generation at every lesson end, or changes to your learning status.
