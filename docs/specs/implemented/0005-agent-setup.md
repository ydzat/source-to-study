# Agent-led environment setup

English · [简体中文](0005-agent-setup.zh-CN.md)

## Problem

Learners currently install tools manually before using the Agent. Installation needs a short entry point independent of native skill discovery.

## Decision

Make a local `sts-setup` skill the canonical procedure. A Windows PowerShell script synchronizes the locked environment and initializes directories. A Python health check verifies the project interpreter, dependencies, a real kernel, and a local JupyterLab server. Keep manual installation as a fallback. End with a short report, an Agent restart/new-session request, and the tutorial link.

## Alternatives considered

- Remote installation instructions: risk mismatching the checked-out scripts.
- Agent-generated commands each time: harder to test and repeat.
- Silent global bootstrap: unnecessary system changes; use an existing uv or explicitly approved official installation instead.

## Consequences

- Bilingual README entry works through direct file reading.
- Setup exits nonzero on failure; reruns preserve learner files.
- Health check runs actual code and starts/stops its own authenticated local server.
- No global Agent configuration, permissions, Anki, or learning-state changes.
- New workflow and existing tests pass on Windows; untested fresh-machine bootstrap is disclosed.

## Limitations

Network and host approvals can prevent installation. Existing global kernel configuration can select the wrong interpreter. Runtime logs may contain local authentication tokens and must remain ignored. The PDF learning walkthrough is documented in [the tutorial](../../../guides/first-session.md), with its historical verification in [0006](0006-live-tutorial-acceptance.md); setup verification alone does not establish teaching behavior.

## Verification

On Windows with PowerShell 7.6.6 and uv 0.12.19, all 20 unittest checks passed. They include stale-report replacement when uv is missing, wrong-interpreter rejection, actual JupyterLab startup/shutdown, and the existing course pipeline. Skill Creator's `quick_validate.py` passed. A fresh project copy without `.venv` completed setup using existing uv/Python/cache, then completed a second run with an unchanged course-profile hash. Python was 3.12.14. Fresh-machine uv installation and real Agent discovery were not exercised. Windows PowerShell 5.1 script execution was blocked by local policy; no policy was changed, and the skill documents the manual-command path. Kernel runtime warnings were visible and did not fail execution.
