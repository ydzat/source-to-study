# Project-local study skills

Status: implemented

## Problem

Learners must repeat operational prompts even though the repository already defines the workflows. Loading every task's mechanics into AGENTS.md would obscure the permanent teaching contract.

## Decision

Three instruction-only skills live under .agents/skills/: sts-course-setup, sts-study-session, and sts-export-cards. Standing principles remain in AGENTS.md, schemas and commands in guides/tools.md, and implementation in scripts/. Skills reference these owners rather than copying scripts or schemas. English SKILL.md files are machine entry points; the paired [learner guide](../../../guides/skills.md) explains their use in both languages.

## Alternatives considered

One universal skill would load unrelated workflows. One skill per script would split learner goals into implementation fragments. Per-agent duplicate skill trees would drift. Three task-scoped entries keep initialization, actual learning, and requested export separate.

## Verification

The skill-creator quick validator passed for all three manifests. The repository document test passed with skill references included, and diff whitespace checks passed. Manual routing review covered a new lecture, revising one unit, quiz/session closure, requested export, draft-only cards, and maintenance-only work; the last two do not authorize export or progress updates respectively. Scripts, dependencies, global agent configuration, and actual learning records are unchanged. Native discovery is documented from official host sources in the learner guide, not exercised in a fresh host session during this change.

## Consequences

Discovery depends on the host and enabled permissions. Manifest/link validation does not prove model behavior; root routing retains a user-directed file-reading path. Only the matching procedure is loaded, while the standing teaching contract remains available across tasks.
