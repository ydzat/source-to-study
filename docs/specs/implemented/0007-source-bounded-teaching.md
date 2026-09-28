# Source-bounded teaching

English · [简体中文](0007-source-bounded-teaching.zh-CN.md)

## Problem

The template describes a goal-to-result lesson but does not require an operation-by-operation source coverage and necessity check. Its tool guide withholds answers from persistent notes, confusing complete study material with a live quiz. Successful execution and populated headings cannot establish explanatory completeness.

## Decision

The bilingual [teaching guide](../../../guides/teaching.md) owns source mapping, reasoning continuity, visual/example selection, complete written answers, and four separate review gates. The study skill requires reading it before authoring; the lesson, course, and session forms expose the corresponding decisions. The tool guide now distinguishes live-quiz withholding from a persistent answer key. The parent workspace retains the private evidence-linked retrospective; this template contains only general lessons.

## Alternatives considered

Adding rules only to AGENTS would duplicate detailed procedures. Copying an entire successful subject notebook would transfer its depth and subject assumptions. Enforcing heading presence in code would not test the missing reasoning. Retain the current builder schema and use a source-to-explanation checklist with manual semantic review.

## Consequences

- Source steps map to explanations and reasons; added prerequisites and examples have an explicit local purpose.
- Complete notes include isolated answers and an assessment-appropriate closure; live quizzes still withhold answers.
- Scope, mechanism, example consistency, and execution are separate checks.
- Material readiness, learner-reported completion, skips, and demonstrated proficiency remain separate.
- Agent entry points require the guide; bilingual documents and links agree.
- Existing documentation tests and changed skill validation pass. Manual scenarios cover overexpansion, missing answers, clarification scope, and course completion without a test.

## Applicability and limits

Overprescribing a numerical oral-exam pattern would harm other subjects. The guide must support textual evidence and non-executable reasoning, and keep language and assessment conventions configurable. No private notes or fixed machine paths may enter the public template. No new runtime dependency or schema change is proposed.

The observed progression was from reusable lesson structure, to connected goal-to-result explanations, to complete persistent answers, and finally to source-bounded examples with separate semantic checks. Structure and executable evidence remain useful. Treating either as sufficient produced incomplete or unnecessarily expanded lessons. These are design lessons from iterative use, not measurements of learning efficacy.

## Verification

On 2026-09-28, the existing documentation test passed (`python -m unittest discover -s tests -p test_docs.py -v` in the project environment, through offline `uv run --no-sync`): one test traversing public links, language pairs, and JSON illustrations. The modified study skill passed `quick_validate.py`. `git diff --check` reported no whitespace errors. No dependencies were installed.

Manual instruction/form review covered these scenarios:

| Scenario | Result of document walkthrough |
|---|---|
| A source gives a short algorithm; a runnable lesson could grow into a full application | Coverage map requires each source step's reason; the guide permits a local example and excludes unnecessary metrics/API details. |
| A learner has not answered a self-test | The lesson form requires an isolated complete answer and closure; the live-quiz rule retains answer withholding in conversation. The conflicting tool-guide sentence was removed. |
| A narrow answer-only question or “continue only if correct” | Explicit scope and conditions override the established notes-update default; a failed correctness check cannot advance the next unit. |
| Learner finishes review, skips a lecture, and has no independent test | Session form records report, skip, and “not tested” separately; prior unresolved questions remain. No new Notebook status is invented. |
| A humanities lesson has no computation | Evidence analysis and changed assumptions fulfill the verification functions without introducing code or oral-exam formatting. |
| A new workspace lacks a reference lesson | Guide and form are sufficient; a designated benchmark is inspected only when available. No private reference is required. |

These were manual document walkthroughs, not independent Agent executions or human learning tests. Existing runtime code, private notes, generated sample workspaces, and historical acceptance results were not rewritten. This change does not claim a fresh installation, GUI, or end-to-end teaching acceptance test.
