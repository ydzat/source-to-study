# Source to Study

English · [简体中文](README.zh-CN.md)

Study your own course materials with a file-capable AI Agent. The Agent prepares and improves your notes; JupyterLab lets you read them, run examples, and write answers. No specific agent provider is required.

## Install and start

On Windows, download and extract this repository. Open the extracted folder in an already installed, signed-in, file-capable AI Agent (for example Codex or OpenCode), then say:

> Read AGENTS.md and .agents/skills/sts-setup/SKILL.md. Follow that skill to install and verify this project. Give me a brief result and the next step.

The Agent checks uv, installs the locked Python environment, prepares your folders, and tests a real Notebook kernel and JupyterLab. Approve necessary downloads when your Agent asks. You do not need to install Python or Jupyter separately. This direct-file request also works when native skill discovery is unavailable.

After successful setup, **restart the Agent application and open a new session in this folder**, then follow [the short practice tutorial](guides/first-session.md) with the bundled PDF. Restarting is a conservative onboarding step, not a requirement of every Agent.

Prefer manual installation? Follow [the manual setup steps](guides/getting-started.md). If uv is already available, the verified setup entry point is:

```powershell
./scripts/setup.ps1
```

To start JupyterLab afterward, open a terminal in the project folder and run:

```sh
uv run jupyter lab
```

uv manages Python and the project's `.venv`; there is no separate Python/Jupyter installation or manual activation step. Leave the last terminal running while you use JupyterLab.

**First time studying with STS? Follow [the short practice tutorial](guides/first-session.md).** For manual installation or troubleshooting, use [the detailed Windows guide](guides/getting-started.md).

## Study with your Agent

The project includes on-demand [skills](guides/skills.md) for environment setup, course preparation, study sessions, and requested card export. You can describe the task naturally; the Agent follows the matching workflow. The guide also explains direct-file use if native discovery is unavailable.

Use a file-capable agent such as Codex or OpenCode, installed and authenticated separately. Open this project folder in it. Copy your PDF into `materials/`, then say:

> Please preprocess materials/[filename.pdf]. I'm studying [subject] to [goal], I know [starting knowledge], and I'd like to study in [language].

Open the resulting `.ipynb` in JupyterLab's left file browser under `study/notes/`. Continue the conversation **in your Agent**, for example:

> Let's start K01.

Save and close the Notebook tab before an Agent rebuild; reopen afterward. Use the “My response” cells for your answers. At session end, ask the Agent to record your actual performance and next starting point. On a new chat, ask it to read the course profile and latest session before resuming.

## Optional review cards

When you ask, the Agent can make cards from selected completed notes and source sections. The exporter produces **TSV + images + import instructions**, also bundled as a ZIP for transport. You manually import into Anki; no MCP, add-on, or Anki connection is used. See [the import tutorial](guides/anki.md).

## Your files

| Location | What it contains |
|---|---|
| `materials/` | Your original course files |
| `study/COURSE.md` | Goals, source map, and links to your work |
| `study/specs/`, `study/notes/` | Lesson source specifications and study Notebooks |
| `study/sources/` | Extracted page text and rendered source pages |
| `study/review/`, `study/sessions/` | Review material and observed learning progress |
| `output/` | Files you choose to export |

These directories are ignored by Git, not access-controlled. Check your AI provider's data policy before sharing materials; inspect files and history before publishing your workspace. The [MIT license](LICENSE) covers the template, not automatically your course materials. Follow your institution's AI-use rules.

For precise commands and file formats, see [the tool reference](guides/tools.md). To maintain STS itself, see [developer documentation](docs/README.md).
