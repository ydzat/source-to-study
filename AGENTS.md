# Source to Study — Agent Contract

[简体中文说明](AGENTS.zh-CN.md) · English (authoritative agent instructions)

This file applies to this template and to projects created from it. Users may adapt it for their own course, institution, and assessment rules.

## Source integrity

- Treat user-provided course materials as the authority for course-specific claims. Read the relevant page or section before citing it; never invent a page number, quotation, result, or source.
- Mark what comes from the current course, another course, a derivation, or an illustrative example. Do not present an AI-generated explanation as a source quotation.
- Keep the user's materials local and private unless the user has explicitly established the right and intent to publish them. Never copy private source pages, screenshots, extracted text, or derivative notebooks into `examples/`.
- If a source or an academic-integrity policy is missing, identify the gap before making a definitive claim or doing assessed work.

## Teaching

- Begin with the source's learning goal and expected output. Explain every new symbol before using it in a formula, then connect inputs, transformations, and outputs without hidden jumps.
- Put a figure directly after the concept it illustrates, followed by a caption explaining the input, operation, output, and observation. Prefer one concrete input carried through the whole explanation.
- Use **Predict → Run → Break it → Reproduce** for executable learning units. Run code from a clean state and verify every numerical claim and local asset path.
- Do not mistake polished notes or a successful run for mastery. Record teaching progress separately from the learner's own closed-book performance.
- For a quiz, withhold the solution until the learner responds. Match the assessment's actual format and language.

## Engineering and publication

- Preserve user edits and original source files. Change declarative inputs rather than generated notebooks or card packages when a generator exists.
- Keep reusable code independent of any single course, operating-system path, AI provider, or UI framework. UI adapters must call the same tested core functions as the CLI.
- Make the smallest relevant verification run after a change; state what was and was not tested.
- Treat `materials/`, `private/`, `work/`, `output/`, and `cache/` as unpublished user space. A Git ignore rule is not a publication audit. Review tracked files and history before any public release.
- Do not initialize Git, connect a remote, install dependencies, upload content, or change the selected license without explicit authorization.

User-facing documentation is maintained in paired `README.md` / `README.zh-CN.md` or `*.md` / `*.zh-CN.md` files. English is the source text; update its Chinese counterpart in the same change. Identifiers, paths, schema keys, and commands stay in English.
