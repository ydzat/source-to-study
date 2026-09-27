# Content, privacy, and language conventions

## Public versus private

| Location | Purpose | Publish? |
|---|---|---|
| `examples/` | Original, rights-cleared mini-course only | Yes, after review |
| `docs/`, `AGENTS.md`, reusable code and tests | General workflow | Yes, after review |
| `materials/` | User-owned PDFs, slides, images, datasets | Never by default |
| `private/` | Personal goals, responses, progress, institution rules | Never by default |
| `cache/`, `work/`, `output/` | Extracted text, page images, generated notebooks/cards | Never by default |

The absence of a PDF is not enough: a notebook can embed slide images or long extracted passages, and [Git history can retain removed files](https://docs.github.com/en/repositories/working-with-files/managing-files/deleting-files-in-a-repository). Before publication, inspect every tracked file, notebook output, binary, embedded image, path, and commit history. Keep the public sample independently authored. Document third-party assets and their permissions explicitly rather than assuming an overall repository license covers them; [Creative Commons advises licensing only material one has the rights to license](https://creativecommons.org/faq/).

## Bilingual documentation

- Public entry points and user guides have English and Simplified Chinese counterparts: `README.md` ↔ `README.zh-CN.md`, `name.md` ↔ `name.zh-CN.md`.
- English is the canonical editing source; both language versions must be updated together. The Chinese version is a usable guide, not a short summary.
- Code, filenames, configuration keys, command names, and standard mathematical notation remain in English. A student's own teaching notes may use their preferred learning language.
- Tests should check that required documentation pairs exist; they cannot prove translation quality, so human review remains necessary.

## Evidence and learning state

- Course-specific claims cite the source file and verified page/section. Separate sourced facts from cross-course recap, derivation, and intuition.
- In a teaching notebook, explain symbols before formulas; keep each figure adjacent to its explanation; verify numerical examples by running their code.
- "Explained", "understood with help", and "reproduced without help" are different states. Only the learner's response can establish the last state.
- AI-generated material is a draft until source checks and learner review are complete. Respect the applicable academic-integrity policy.

## Release gates (planned, not yet automated)

1. Run tests and the original sample from a clean checkout.
2. Confirm that every tracked file is allowlisted; scan binaries, notebook outputs, generated assets, and history separately.
3. Confirm no private path, credential, copyrighted course extract, or unlicensed third-party asset is included.
4. Confirm that the MIT license covers only materials the owner has the right to license; document any separate asset licenses.
5. Only then connect and publish the GitHub repository.
