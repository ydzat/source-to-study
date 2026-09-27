# Source to Study

English · [简体中文](README.zh-CN.md)

Study your own course materials with a file-capable AI Agent. The Agent prepares and improves your notes; JupyterLab lets you read them, run examples, and write answers. No specific agent provider is required.

## Install and start

Download and extract this repository. Install [uv](https://docs.astral.sh/uv/getting-started/installation/), then open a terminal in the folder containing `pyproject.toml` and run:

```sh
uv sync --locked
uv run python scripts/init_workspace.py
uv run jupyter lab
```

uv manages Python and the project's `.venv`; there is no separate Python/Jupyter installation or manual activation step. Leave the last terminal running while you use JupyterLab.

**First time using these tools? Follow [the Windows step-by-step tutorial](guides/getting-started.md).** It explains installation, where to open the terminal, which window to talk in, and how to find your Notebook.

## Study with your Agent

Use a file-capable agent such as Codex or OpenCode, installed and authenticated separately. Open this project folder in it. Copy your PDF into `materials/`, then say:

> Read AGENTS.md and guides/tools.md. My course is [subject], my goal is [goal], and my preferred teaching language is [language]. The source is materials/[filename.pdf]. Establish my course profile, inspect the source, and propose knowledge units. After I confirm them, generate a Notebook framework in study/notes/. Do not write every lesson yet.

Open the resulting `.ipynb` in JupyterLab's left file browser under `study/notes/`. Continue the conversation **in your Agent**, for example:

> Teach K01 only. Define the notation, show the steps from the source's goal to its result, and use figures and a worked example. Update the corresponding notes and run the checks. Wait for my questions before moving on.

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
