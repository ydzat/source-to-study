---
name: sts-study-session
description: Teach or revise an STS knowledge unit, quiz the learner, resume study, or close an actual study session. Use when explaining course content and maintaining its notes; not for initial source preprocessing, software maintenance, or card export alone.
---

# Teach, revise, and resume

Work from the STS repository root, three directories above this file. Read [AGENTS.md](../../../AGENTS.md) for the teaching and evidence contract; do not replace it with a fixed answer template.

## Recover the learning context

Read study/COURSE.md, the latest relevant session, and the requested lesson. For a Notebook, inspect its spec and saved learner responses as well as the generated file. Establish the requested unit and its actual source pages. If the learner only asks a narrow clarification, do not expand to the rest of the lecture.

Inspect the source itself. When missing prerequisites are covered by another supplied course, consult that material and introduce the necessary objects before using them. Record unresolved evidence explicitly.

Before teaching or revising, read [the teaching guide](../../../guides/teaching.md) completely and inspect [the lesson form](../../../templates/lesson.md). Map the requested source steps to their reasons and explanation locations. If the learner designates a benchmark, inspect an actual completed unit, its source and available output; reuse its functions subject to current scope checks. Quiz/resume/close-only requests need only the relevant guide sections.

## Perform the requested mode

For an established notes-based study workspace, a request such as "Start K01" authorizes authoring that unit in the existing notes. A question such as "What does this symbol mean?" requests an answer in conversation and does not authorize file edits. If the same message explicitly asks to update the notes, integrate the explanation there. Complete the requested unit's learning chain, leave later units untouched, and pause at the unit boundary. Respect explicit chat-only, quiz, and smaller-scope requests. Keep recall prompts in the notes without requiring answers before delivering a requested lesson.

- **Teach or revise:** use [the lesson form](../../../templates/lesson.md) as guidance. Build the source-goal-to-result chain, using questions to find gaps. Preserve the course's notation and integrate corrections into the owning section. Keep figures and captions beside the corresponding reasoning, with one worked input across stages where useful. Do not append a chat transcript.
- **Quiz:** match the course's assessment language and form. Ask before revealing the answer, then assess the actual response. Store review material using [the review form](../../../templates/review.md), without automatically exporting cards.
- **Resume:** verify the recorded next point against current notes and the learner's request. Do not assume that generated or previously read material was independently mastered.
- **Close:** only after actual teaching or practice, use [the session form](../../../templates/session.md) to record covered scope, assistance, observed performance, unresolved issues, and the next point. Link the record from the course profile. A maintenance-only request does not create a learning session.

Complete authored units include isolated self-test answers and an assessment-appropriate model response. Live quizzes still wait for the learner's response. If the learner reports finishing a course and skipping another section, record those statements separately from verified proficiency; do not fill skipped lessons or erase unresolved questions. Explicit answer-only requests and conditions such as “continue only if correct” govern whether notes or later units may change.

## Maintain and verify the deliverable

For Notebook changes, read Notebook source and build and Execution checks in [the tool reference](../../../guides/tools.md). Update the spec and preserve learner cells. Have the learner save and close an open Notebook before replacement, respecting any already established save/close agreement. Reconcile conflicts while keeping the builder's protections active.

Build and check the Notebook from the documented commands. Apply the teaching guide's four gates separately: source coverage/scope, explanation, example consistency, and artifact verification. Verify computed results, image references, and the source support; execution is not semantic validation. A failed check stops delivery until fixed or explicitly reported as unresolved. For Markdown-only notes, check citations, figures, and worked reasoning without introducing unnecessary code.

For a completed note update, briefly report what changed, link the file, and state verification results without repeating the lesson. For a question-only request, answer directly with the reasoning needed to resolve it; do not edit files or append an offer to do so. A one-sentence limit must not remove necessary explanation. Pause at the requested unit boundary. Do not generate cards or advance mastery merely because the notes are complete.
