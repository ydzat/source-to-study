# From source to a usable lesson

English · [简体中文](teaching.zh-CN.md)

Read this guide completely before authoring or substantially revising a lesson. Use the [lesson form](../templates/lesson.md) for the deliverable and [tool reference](tools.md) for file operations. The course profile determines scope, language, and assessment; this guide does not assume a particular subject or exam.

## 1. Establish scope before writing

Read the requested source section and relevant existing lesson. Build a short coverage map in the lesson or its authoring notes:

| Verified source location | Goal, claim, or operation | Why it needs explanation | Explanation / figure / check location |
|---|---|---|---|
| Actual page or section | What the source requires | Missing prerequisite or reasoning step | Where the lesson resolves it |

Cover every substantive step in the requested section. Keep definitions, proofs, experiments, self-tests, and priorities within the agreed sources plus the minimum reasoning needed to understand them. Each added example must explain an identifiable source step. Do not add software API details, new evaluation measures, or a full application merely to make a lesson executable. A small local calculation may be sufficient; state exactly which part it demonstrates.

Use the source's notation, conventions, and operation order. Define unfamiliar concepts that the source itself includes. Absence from another course's text search does not establish exclusion. Inspect relevant supplied prerequisite sources, distinguish their role, and introduce their objects before using them. A combined assessment may require several courses; prerequisites within that scope remain required even if the learner has not reviewed them yet.

If a source formula appears inconsistent, inspect the original page, test the inconsistency, and explain the verified issue and adopted convention locally. Record unresolved uncertainty. Neither silently replace the notation nor reproduce a confirmed error as valid.

For suspected recap, compare both sources and the earlier note. Replace verified repetition in derived notes with a precise pointer; retain newly introduced content. Preserve original materials and page numbering. If the earlier note is still a framework, record that explanation gap explicitly.

## 2. Build the reasoning chain

Organize the lesson as **goal → inputs → intermediate objects and operations → derivation or reasoning → verifiable result**. For each transition, state what is given, what is calculated or inferred, why the operation serves the goal, and what it yields. Identify what the result still cannot determine.

Define new symbols before formulas: meaning, type, dimensions, coordinate system or units when applicable, and pronunciation when useful. Show substitutions and intermediate equalities wherever the learner would otherwise need to guess a step. For non-mathematical subjects, explain the evidence, inference, assumptions, and limits of the argument with the same care.

Treat the learner's questions as diagnostic evidence. Several connected questions often reveal a missing prerequisite chain. Organize the answer around that chain and check that each question is resolved. When a note update is requested, integrate that structure into the owning section. Keep the source's task as the organizing goal.

Use source evidence, cross-course prerequisites, derivation, and illustrative intuition as distinct labels. Explain each component's removal or changed assumption when relevant; distinguish mathematical necessity, numerical necessity, and an empirical improvement. Do not invent an ablation for an unrelated subject.

## 3. Make the mechanism visible

Choose a representation for the actual difficulty: a diagram for geometry or relationships, aligned intermediate images for image processing, a table for changing objects, a small calculation for algebra, or annotated textual evidence for an argument. Prefer one input across connected stages when it makes those changes comparable. Split examples when a single input would require unrelated machinery.

Put each figure directly after its corresponding explanation, followed by a caption stating input, operation, output, and the important observation. Use readable labels and distinguish source figures, schematic illustrations, constructed teaching data, and computed results. A collection of screenshots without an explanation does not fulfill this function.

Execute code behind reported numbers and generated plots; inspect the rendered figure as well as the values. For code-free reasoning, verify the worked argument against the source. A local demonstration must not be described as running the complete algorithm. Do not ask the learner to debug untested teaching code.

## 4. Complete the learning loop

The six functions are goal/source, notation/prerequisites, reasoning, worked verification, independent reproduction, and closure. Preserve these functions in a full unit; headings alone do not satisfy them. Mark genuinely inapplicable functions and explain why. Keep every included section relevant to the unit.

For executable concepts use **Predict → Run → Break it → Reproduce**:

- Predict: pose a checkable question before revealing the result.
- Run: show the actual result and connect it to the source operation.
- Break it: change one relevant assumption or input, observe the consequence, and explain the boundary.
- Reproduce: provide a blank answer area for independently reconstructing the result or explanation.

For textual, historical, or conceptual topics, adapt the same functions to an evidence-based prediction or claim, worked analysis, counterexample or changed assumption, and independent reconstruction. Code is not mandatory.

Complete written material includes worked answers and an assessment-appropriate model response. Keep self-test answers in collapsed sections or a clearly linked answer section, separate from questions. A live quiz withholds the answer until the learner responds; it does not require deleting the note's answer key. Do not leave closure as “to be supplied after the learner answers.”

For a method-focused oral exam, **Problem → Solution → Why → Boundary** is a useful closure. Other assessments may need a proof, essay plan, interpretation, or practical demonstration. Include a concise takeaway and source-grounded priorities; label tutor recommendations as recommendations, without claiming unsupported exam frequency.

## 5. Review four different things

| Gate | Evidence required before delivery |
|---|---|
| Source coverage and scope | Every mapped source step is addressed; every added concept has a necessary local purpose. |
| Explanation | Symbols precede formulas; intermediate reasoning and reasons for operations are explicit; the chain reaches its stated result. |
| Example consistency | Inputs, order, constraints, units, and output match the source; figures are adjacent and explained; partial demonstrations are identified. |
| Artifact verification | Calculations agree with prose; links exist; applicable code runs from the Notebook directory in a fresh kernel; answers and existing learner work remain available. |

A checker establishes only its documented technical properties. Manual review is required for the first three gates and for answer quality. Report unverified aspects honestly.

If the learner designates an existing lesson as a benchmark, inspect one relevant completed unit and its source, generated document, and available output before writing. Reuse the teaching functions; check its depth, notation, figure placement, and answer quality against the current contract. A preferred older lesson can still contain defects. Do not require a private benchmark file in a new workspace; this guide and the blank form provide the initial standard.

## 6. Deliver and record separately

Honor the agreed deliverable and scope. A question requests an answer in conversation; it does not authorize file edits. When the learner explicitly asks to update notes, integrate the explanation there and give a short change/verification report with a link. Do not repeat the full edited lesson in chat. A correctness check conditional on success must not trigger teaching the next unit after a failed check.

Record material readiness, learner-reported reading/review completion, assisted practice, and independently demonstrated performance separately. Record intentional skips explicitly; they are neither recap nor completed instruction. A learner can finish their chosen review without all notes being filled or every topic being tested. Only observed independent performance supports mastery. A template audit itself creates no learning progress.

When a problem recurs, identify the missing decision or conflicting instruction and change its owning guide and execution entry point. Avoid accumulating source-specific exceptions or duplicating rules in every file. Recheck the previously failing scenario and state whether verification was document review, script execution, or an actual learner session.
