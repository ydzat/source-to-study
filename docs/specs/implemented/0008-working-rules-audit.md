# Working rules and Markdown consistency

English · [简体中文](0008-working-rules-audit.zh-CN.md)

## Problem

The tutor instructions omit reusable expression, authorization, evidence, and editing rules established in the reference workspace. The study skill and tutorial authorize note edits from questions alone. Some historical decisions read as current instructions, and several Chinese passages use discouraged shorthand.

## Decision

The [AGENTS language pair](../../../AGENTS.md) now owns reusable expression, question authorization, evidence, safe editing, and verification rules. The study skill, learner tutorials, teaching guide, and course form distinguish questions from explicit revision requests. Historical decisions identify superseded behavior without rewriting observed test results.

Reviewed all 50 pre-existing maintained Markdown files in the root, guides, docs, templates, examples, and .agents/skills/. This decision adds two language files. Dependencies, generated acceptance workspaces, private learner state, and source materials were excluded. Private course paths, exam facts, and fixed interpreter choices were not imported into the template.

## Alternatives considered

Copying the entire reference instruction file would import private course paths, exam facts, and runtime assumptions. A style-only replacement would leave the question-to-edit behavior unchanged. Use targeted edits supported by the local reference rules and current documents.

## Consequences

- Questions receive answers without implied file edits; explicit teaching/edit requests retain their requested workflow.
- AGENTS covers expression, evidence, scope, safe editing, and honest verification without requiring the private parent workspace.
- Tutorials, skills, forms, and current design decisions agree; historical observations retain their original identity.
- English and Chinese instructions agree; links, Markdown structure, and skill manifests validate.
- No runtime code, dependencies, original materials, or learning records change.

## Verification and limits

Text searches can confuse technical terms and quotations with stylistic violations. Review matches in context. Historical verification cannot be rewritten as evidence of the new behavior. This documentation change requires document and scenario review; it does not establish fresh end-to-end Agent compliance.

On 2026-09-28, the existing documentation test passed through offline `uv run --no-sync` in the existing environment: `python -m unittest discover -s tests -p test_docs.py -v`. It checks public relative links, language pairs, JSON illustrations, and final newlines. Both changed skills, sts-study-session and sts-setup, passed `quick_validate.py`; `git diff --check` reported no whitespace errors.

Manual review checked the following decisions across the relevant documents:

| Request or condition | Current instruction |
|---|---|
| “What does this symbol mean?” | Answer in conversation with enough explanation; do not edit or append an implementation offer. |
| “Explain this and update K01 in my notes.” | Update the requested section, verify it, and provide a concise file handoff. |
| “Start K01.” in the established notes workflow | Author the requested unit; leave later units untouched. |
| “Continue only if my answer is correct.” | Evaluate the condition before proceeding. |
| Setup only | Verify the environment; leave course content and learning progress unchanged. |
| A failed script | Inspect the relevant error with secrets removed; retain validation and report unresolved failures. |
| Earlier acceptance changed a note after a question | Keep the observation dated and explicitly separate it from the current rule. |

No runtime code, dependencies, original materials, or learning records were modified. The prior 20-test runtime acceptance was not rerun or claimed for this change. No new independent Agent or graphical-interface acceptance was performed. The checks above establish document consistency and manifest validity, with runtime behavior left unverified in this iteration.
