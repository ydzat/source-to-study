---
name: sts-setup
description: Install, verify, or repair the Source to Study Windows learning environment with uv. Use for project deployment and dependency setup, not course preparation or teaching.
---

# Set up Source to Study

Use the learner's language. Read the checked-out [AGENTS.md](../../../AGENTS.md) and this skill, not a moving remote copy. Resolve the project root from this file (three directories up); it must contain `pyproject.toml`, `uv.lock`, and `scripts/setup.ps1`.

## Preconditions and scope

- Support Windows only. Confirm the shell and project location. The user supplies an already working file-capable Agent; do not install/configure providers, subscriptions, MCPs, or global skills.
- A deployment request covers project environment setup, subject to the host's approvals for commands/downloads. Explain downloads briefly. Never relax sandbox, approval, authentication, or execution-policy settings to bypass a restriction.
- Inspect existing `.venv` and project files. Do not delete environments, replace learner work, regenerate `uv.lock`, or add dependencies to fix a failure without diagnosing it. Stop for permission or a consequential repair decision when needed.

## Find or install uv

1. Check `Get-Command uv -CommandType Application` and run the resolved executable with `--version`. Reuse a working installation; do not update it routinely.
2. If missing, use the official Windows installation instructions at <https://docs.astral.sh/uv/getting-started/installation/>. Prefer `winget install --id=astral-sh.uv -e` when WinGet is available and installation is authorized. Respect prompts; do not accept unrelated agreements or install alternatives silently.
3. If WinGet is unavailable or the installation fails, inspect the error and official alternative with the user. Do not loop through installers. Do not assume the current Agent inherited a new PATH. Locate the actual executable from installation output and verify it, or request a restart and resume here. A missing uv is not a successful setup.

## Run and verify

From the project root, run `./scripts/setup.ps1`. When uv is not on this process's PATH, pass `-UvPath 'the verified absolute path to uv.exe'`.

If script execution is blocked before the script starts, no new report can be written. Report that restriction and use the manual commands in [Getting started](../../../guides/getting-started.md) only if the host permits those commands; otherwise ask the user for direction. Never change execution policy. The manual path must still run the real health check; do not treat an old report as its result.

The script uses `uv sync --locked`, preserves existing learner files during initialization, and runs `scripts/check_setup.py`. It records its latest status in ignored `work/setup/report.json`. Check the command exit status **and this run's report**. A previous report is not evidence for a failed current run. `failed` or `running` is not success.

The check executes a fresh Notebook kernel and briefly starts an authenticated loopback JupyterLab server, then stops that server. It does not leave a browser or background service running. Runtime logs stay under `work/`; do not paste tokens or entire environment/configuration files into chat.

If verification fails, inspect the named stage and minimal relevant error. Fix only in scope and rerun. Never skip a check, fabricate success, or mark learning progress. Do not launch the learner's long-running JupyterLab session during installation.

## Handoff

On success, use at most two short lines in the user's language:

> STS is ready: the project environment, Notebook kernel, and JupyterLab check passed.
> Restart your Agent application and open a new session in this folder, then follow [the short practice tutorial](../../../guides/first-session.md).

For Chinese, link [the Chinese practice tutorial](../../../guides/first-session.zh-CN.md). Ask for the restart as a conservative onboarding step, not a universal host requirement. The tutorial uses the bundled public-domain PDF; learners generate their own notes with the Agent, rather than opening a prewritten completed course. Do not begin teaching, fill the course profile, or generate cards as part of setup.

If blocked, report the failed stage and the specific user action needed instead of the success handoff. Preserve partial installation so a later run can resume safely.
