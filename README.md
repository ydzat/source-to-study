# Source to Study (STS)

English · [简体中文](README.zh-CN.md)

**Version 1.1** · Windows setup · [MIT License](LICENSE)

Study your own course materials with a file-capable AI Agent. The Agent prepares and improves your notes; JupyterLab lets you read them, run examples, and write answers. No specific agent provider is required.

## Features

- PDF text extraction, rendered source pages, verified page coverage, and knowledge-unit frameworks.
- Source-grounded lessons with defined notation, worked reasoning, adjacent figures, and complete answer keys.
- Predict → Run → Break it → Reproduce, adapted to the subject and assessment.
- Declarative Notebook generation, clean-kernel checks, backups, and preserved learner-owned cells.
- Separate records for authored material, reported completion, practice, and demonstrated proficiency.
- Optional TSV/image export for manual Anki import.

## Requirements

- Windows and PowerShell for the documented setup workflow.
- An installed, authenticated AI Agent that can read/edit project files and run approved local commands. Choose your provider separately.
- A browser for JupyterLab and internet access for initial dependency downloads.
- Course materials you are permitted to use; automated source preparation currently accepts PDF.

uv manages the environment and the Python version selected in `.python-version` (currently Python 3.12). Other operating systems have not received the documented setup acceptance checks.

## Quick start

### 1. Set up the workspace

On Windows, download and extract this repository. Open the extracted folder in an already installed, signed-in, file-capable AI Agent (for example Codex or OpenCode), then say:

> Read AGENTS.md and .agents/skills/sts-setup/SKILL.md. Follow that skill to install and verify this project. Give me a brief result and the next step.

The Agent checks uv, installs the locked Python environment, prepares your folders, and tests a real Notebook kernel and JupyterLab. Approve necessary downloads when your Agent asks. You do not need to install Python or Jupyter separately. This direct-file request also works when native skill discovery is unavailable.

After successful setup, **restart the Agent application and open a new session in this folder**, then follow [the short practice tutorial](guides/first-session.md) with the bundled PDF. Restarting is a conservative onboarding step, not a requirement of every Agent.

Prefer manual installation? Follow [the manual setup steps](guides/getting-started.md). If uv is already available, the verified setup entry point is:

```powershell
./scripts/setup.ps1
```

### 2. Open JupyterLab

Open a terminal in the project folder and run:

```sh
uv run jupyter lab
```

uv manages Python and the project's `.venv`; there is no separate Python/Jupyter installation or manual activation step. Leave the last terminal running while you use JupyterLab.

## Usage

### Prepare and study a course

The project includes on-demand [skills](guides/skills.md) for environment setup, course preparation, study sessions, and requested card export. You can describe the task naturally; the Agent follows the matching workflow. The guide also explains direct-file use if native discovery is unavailable.

Use a file-capable agent such as Codex or OpenCode, installed and authenticated separately. Open this project folder in it. Copy your PDF into `materials/`, then say:

> Please preprocess materials/[filename.pdf]. I'm studying [subject] to [goal], I know [starting knowledge], and I'd like to study in [language].

Open the resulting `.ipynb` in JupyterLab's left file browser under `study/notes/`. Continue the conversation **in your Agent**, for example:

> Let's start K01.

Ask questions in conversation. When you want the explanation added to the file, explicitly request a note update.

Save and close the Notebook tab before an Agent rebuild; reopen afterward. Use the “My response” cells for your answers. At session end, ask the Agent to record your actual performance and next starting point. On a new chat, ask it to read the course profile and latest session before resuming.

The [teaching workflow](guides/teaching.md) explains how each unit connects source goals, defined objects, worked reasoning, visible results, and independent reproduction. It also describes source-scope checks and complete written answers separated from live quizzes.

### Export review cards

When you ask, the Agent can make cards from selected completed notes and source sections. The exporter produces **TSV + images + import instructions**, also bundled as a ZIP for transport. You manually import into Anki; no MCP, add-on, or Anki connection is used. See [the import tutorial](guides/anki.md).

## Project structure

| Location | What it contains |
|---|---|
| `AGENTS.md`, `.agents/skills/` | Tutor rules and task-specific procedures |
| `guides/`, `templates/` | Usage guides and blank study forms |
| `examples/` | Original examples and attributed external learning material |
| `scripts/`, `tests/` | Local tools and automated checks |
| `docs/` | Maintainer documentation and design decisions |
| `materials/` | Your original course files |
| `study/COURSE.md` | Goals, source map, and links to your work |
| `study/specs/`, `study/notes/` | Lesson source specifications and study Notebooks |
| `study/sources/` | Extracted page text and rendered source pages |
| `study/review/`, `study/sessions/` | Review material and observed learning progress |
| `output/` | Files you choose to export |
| `work/` | Local intermediate artifacts |

## Documentation

- [Installation and troubleshooting](guides/getting-started.md)
- [First study session](guides/first-session.md)
- [Teaching workflow and quality checks](guides/teaching.md)
- [Available skills](guides/skills.md)
- [Commands and file formats](guides/tools.md)
- [Anki import](guides/anki.md)
- [Development and maintenance](docs/README.md)

## Version history

### 1.1 — Current

- Added source-step coverage, minimum-necessary examples, and four separate teaching-quality checks.
- Completed written-answer requirements while preserving answer withholding during live quizzes.
- Expanded expression, evidence, authorization, safe-editing, and verification rules across instructions and tutorials.
- Clarified that questions alone do not authorize note edits; recorded completion, skips, and proficiency separately.
- Reorganized the bilingual README and aligned project metadata to `1.1.0`.

### 1.0 — Previous baseline

The earlier template is retrospectively designated **1.0**. It established Windows/uv setup, source preparation, Notebook generation and checking, study-session workflows, and file-only card export.

These project version labels do not assert that matching Git tags or GitHub Releases have been published. Version 1.1 retains the existing file formats and runtime dependencies.

## Privacy and limitations

Personal materials, study records, intermediate files, and exports belong in the ignored `materials/`, `study/`, `work/`, and `output/` directories. Git ignore rules provide no access control: inspect files and history before publishing. Check your AI provider's data policy and your institution's AI-use rules before sharing materials.

Notebook code runs locally with the executing process's permissions. Inspect unfamiliar code. Successful execution verifies technical properties; source accuracy, teaching completeness, and learner proficiency require separate evidence.

## Support and contributing

For setup problems, use the troubleshooting guide and share the relevant error with secrets removed. For repository changes, follow [maintainer documentation](docs/README.md): keep language pairs consistent, preserve personal data, and run the checks relevant to the change.

## License

The template is distributed under the [MIT License](LICENSE), copyright Dongze Yang. Course materials retain their own rights. Attribution and reuse information for the bundled PDF are documented with the [example source](examples/central-tendency/README.md).
