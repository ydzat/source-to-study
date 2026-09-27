# Live tutorial acceptance

English · [简体中文](0006-live-tutorial-acceptance.zh-CN.md)

## Problem

Document and script tests do not show whether short, ordinary learner messages actually produce and improve usable notes.

## Decision

Keep the tutorial's short learner messages. Make their intended actions explicit in the owning skills: preprocessing includes a source map and validated framework; starting a unit and asking follow-up questions update existing notes by default; chat reports the result instead of repeating the lesson. Explicit requests for extraction only, chat only, quizzes, or a smaller scope still take precedence.

Verify this contract with a real independent Agent in an isolated, initialized workspace, not a simulated response. Use the tutorial's messages without injecting a test rubric. Inspect actual artifacts, source support, execution, and revision diffs.

## Alternatives considered

A scripted fake Agent cannot test discovery or behavior. Giving the second instance a detailed test rubric would contaminate the test. Running against personal notes would risk real learning state.

## Consequences

- Learners do not need to repeat the internal workflow or ask explicitly for every Notebook update.
- Missing learning choices and protection of unsaved edits can require a short reply. They are not hidden by the tutorial.
- Skills are canonical English instructions; learner-facing tutorials remain bilingual. No longer prompts or source-specific rules were added to the tutorial.
- Local logs, generated lessons, snapshots, and test fixtures remain ignored; none are a shipped reference answer or real learner progress.

## Verification

Tested on Windows on 2026-09-27 with Codex CLI `0.158.0-alpha.2.1` and the existing configured model, Python 3.12.14, and the locked STS environment. The local Codex installation required `--no-daemon`; this is a host workaround, not a universal STS prerequisite. Child sessions retained `workspace-write` permissions.

### Observed failures and corrections

- Initial preprocessing stopped after PDF extraction. After the setup-skill correction, the same short request proposed a division, requested learning choices, and built the framework after confirmation.
- Initial K01 teaching was chat-only and left the Notebook unchanged. The study-skill correction made notes the default deliverable.
- A follow-up updated the note but repeated its example and table in chat. The delivery rule was tightened; a fresh-session clarification returned a brief answer and file/verification handoff instead of another lesson.
- An existing session did not reload a changed skill. Corrected behaviors were tested in new conversations; the core preprocessing verification → K01 → follow-up → K02 sequence then ran in one persistent conversation. The final concise-delivery change received a separate fresh-session test.

### Artifact checks

| Checkpoint | Observed result |
|---|---|
| `帮我预处理 summarizing_distributions.pdf。` | 12 units, all 41 pages assigned exactly once; original PDF unchanged; source assets and framework validated. A fresh-session rerun safely reused these artifacts. |
| `我们从 K01 开始吧。` | K01 covers PDF pp.2–8, with defined notation, worked calculations, source figures/captions, two executable cells, and recall prompts. Later units remain untaught. |
| `为什么同一组数据可以有不同的“中心”？我没太理解。` | Only K01 changed; clarification was integrated before formulas. Learner-owned cells, including an explicitly labeled preservation fixture, remained identical. |
| `这部分我明白了，继续 K02 吧。` | Only K02 changed, using PDF pp.9–11; K01 and learner cells remained identical. Self-reported understanding was not recorded as independent mastery. |
| Fresh-session `K01 里的 c 是数据里的某个数吗？` | Only K01's explanation changed; the short handoff and preserved learner content were verified. |

Independent final verification passed 115 local asset references and three code cells in clean top-to-bottom execution from the Notebook directory. A separate inline-backend execution produced one PNG containing the two cost plots; the plots and numerical outputs were inspected. Both the standard check and inline check left the input Notebook unchanged. The final examples reproduce the source values: absolute-deviation minimum 20 at 4, squared-deviation minimum 134.8 at 6.8, and the 31-team dataset's sum 634, median 20, and mode 18.

The existing 20 automated tests passed, including real kernel and local Jupyter server tests. Both modified skills passed the skill validator; public links and bilingual document pairs passed the documentation test.

### Limits

This is one Chinese-language, Agent-driven learner simulation, not a claim about human learning or every Agent/model. It exercises post-setup usage with an initialized environment, not fresh-machine installation. No GUI keystroke or full browser rendering test was performed; inline kernel output and local server tests are not substitutes for that claim. English conversational behavior and card export were outside this run. Host warnings and failed trials remain in local evidence. No private course materials or real progress records were changed.
