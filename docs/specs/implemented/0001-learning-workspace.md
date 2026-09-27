# Learning workspace as the product

Status: implemented

## Problem

Students need a reusable learning workspace. A root dominated by software-development plans does not tell a student how to begin studying.

## Decision

The root README guides course setup, AGENTS defines tutor behavior, and bilingual forms support local course profiles, lessons, retrieval questions, and sessions. Personal state lives in ignored `study/`. Maintainer information belongs in `docs/`; the [architecture](../../architecture.md) owns the current layout.

## Alternatives considered

Keeping the development scaffold as the main entry was rejected because it addresses contributors rather than learners. Duplicating completed course state in English and Chinese was rejected because the copies can diverge; only form guidance is bilingual.

## Consequences

A learner can begin with a file-capable assistant and the forms, or use the local tools described in the [tool reference](../../../guides/tools.md). The small example demonstrates note structure, not a complete course or tested learning efficacy.

## Verification

The implementation supplies all four forms and both language entry points. A local check passed for 22 Markdown files, 58 relative links, language counterparts, and final newlines. Git confirmed that study/COURSE.md and materials/example.pdf are ignored; diff whitespace checks passed. A manual review of the setup instructions found no invented pipeline commands. These checks do not validate model compliance or educational outcomes.
