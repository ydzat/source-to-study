# From download to your first study session

English · [简体中文](getting-started.zh-CN.md)

You will use two windows: an **AI Agent** to discuss the course and edit files, and **JupyterLab** in your browser to read and run your notes. JupyterLab is not the chat window. Both work with the same files on your computer.

## 1. Download the template and install uv

On the [repository page](https://github.com/ydzat/source-to-study), choose **Code → Download ZIP**, then extract it to a folder you can find again. Alternatively, use Git. Neither Git nor a GitHub account is needed for the ZIP route.

Install uv once. It manages Python and this project's isolated environment, so you do not need to install Python, JupyterLab, and scientific packages separately. The commands below come from the [official uv installation instructions](https://docs.astral.sh/uv/getting-started/installation/).

Windows: open PowerShell and run:

```powershell
winget install --id=astral-sh.uv -e
```

If WinGet is unavailable, choose another Windows installation method from the official instructions above. Close and reopen the terminal, then run `uv --version`. If the command is not found, follow the installer's PATH instructions; do not continue until this works.

## 2. Open a terminal in the project folder

The correct folder contains `README.md`, `AGENTS.md`, and `pyproject.toml`. It is not the containing Downloads folder or the `.venv` directory.

On Windows, open the extracted folder in File Explorer and choose **Open in Terminal** from its context menu. Alternatively, type `cd` followed by your actual folder path:

```powershell
cd "C:\your\folder\source-to-study-main"
```

Replace this illustrative path; do not copy it literally. All remaining commands run from this project folder.

## 3. Install the environment and prepare the workspace

```sh
uv sync --locked
uv run python scripts/init_workspace.py
```

The first command downloads the selected Python if necessary and installs the locked dependencies into `.venv`. It can take a few minutes and needs internet access. The second creates your local study directories and an empty course profile without replacing existing files. No manual environment activation is needed. See [uv's project guide](https://docs.astral.sh/uv/guides/projects/) for the environment and lockfile model.

Copy your first PDF into `materials/`. Start with one lecture, not the whole semester. Other formats can be read by your agent or converted to PDF separately; the preprocessing script currently accepts PDF only. Original materials are never rewritten.

## 4. Open your Agent and initialize the course

Use a file-capable agent application, for example Codex or OpenCode. These are examples, not required providers. Install and authenticate your chosen application using its own instructions. It must be able to read and edit this project, inspect page images, and run local commands with your approval. A chat that cannot access your files cannot perform these steps by itself.

Open **this same project folder** in the agent. Tell it:

> Read AGENTS.md and guides/tools.md. Use uv for this project. My course is [subject]; my goal is [goal or assessment]; teach me in [language]. The first source is materials/[filename.pdf]. Help complete study/COURSE.md. Inspect the source and identify its knowledge units. First show me the unit division and source page ranges; do not write all explanations yet.

Answer questions about your starting knowledge, assessment requirements, and permitted AI use. Confirm that the agent has found the correct file. Access to local files does not imply local model processing: check your provider's data policy before exposing private material.

## 5. Ask for the Notebook framework

Once the source scope and unit division are agreed, say:

> Prepare the PDF with scripts/prepare_pdf.py. Create a lesson spec in study/specs/ following guides/tools.md, then build study/notes/lecture01.ipynb with scripts/nb_build.py. Keep untaught units marked todo. Check the framework. If early pages repeat the previous lecture, verify that against the previous material and keep a recap pointer without deleting any source pages.

The agent runs the scripts; you do not need to author the JSON spec. The framework is a source map and placeholders, **not a completed lesson**. You should receive a Notebook path, covered page range, and validation result.

## 6. Start JupyterLab and find the Notebook

In your project terminal, run:

```sh
uv run jupyter lab
```

Leave that terminal running. JupyterLab normally opens in your browser. If it does not, open the local URL printed in the terminal; do not share its access token. Starting from the project folder makes that folder the file-browser starting point. See [JupyterLab startup](https://jupyterlab.readthedocs.io/en/stable/getting_started/starting.html) and [uv with Jupyter](https://docs.astral.sh/uv/guides/integration/jupyter/).

In JupyterLab's left file browser, open `study`, then `notes`, then double-click `lecture01.ipynb`. Do not open the JSON spec as your study document. Select the project's Python kernel if prompted. `Shift+Enter` runs the selected cell. Only run code you trust: this is normal local Python, not a sandbox.

## 7. Complete one knowledge unit at a time

Return to the Agent window:

> Let's study K01 only. Explain the goal in the source, define new symbols, and connect every intermediate step to the result. Use one concrete example where possible, with figures immediately below their concepts and captions below the figures. Update the Notebook through its spec, run the checks, and leave other units as placeholders. Give me a short change summary rather than repeating the whole lesson here.

Read the updated Notebook in JupyterLab. Make predictions before running experiments. Ask specific follow-ups in the Agent window, for example:

> I cannot see how this input becomes the next object. Show the intermediate result and revise that section of K01, rather than appending a disconnected answer.

When ready, ask to move to K02. For a subject without useful executable experiments, use diagrams, worked reasoning, and retrieval practice instead of artificial code exercises.

Before the agent rebuilds an open Notebook, **save and close its tab**. After the rebuild, reopen it. Write answers in “My response” cells or your own added cells. Generated lesson cells come from the spec: direct edits there cause a rebuild conflict that the agent must reconcile, not overwrite. Rebuilds back up the existing file and preserve learner cells; generated code outputs are cleared and can be rerun. Added cells without a generated identity are retained at the end.

## 8. Finish, resume, and optionally make cards

At the end, say:

> Record what we actually studied, my observed performance, unresolved questions, and the next starting point in study/sessions/. Update the course profile's links. Do not mark mastery just because you generated the notes.

Save your Notebook. To stop JupyterLab, return to its terminal, press `Ctrl+C`, and confirm shutdown if asked. Closing the browser alone need not stop the server. Next time, enter the same folder, run `uv run jupyter lab`, and ask your agent to read `study/COURSE.md`, the latest session, and relevant notes before continuing.

Cards are optional and user-requested:

> Based on these completed notes [paths], and these source sections [paths/pages, if needed], prepare focused review cards. Check the sources, include useful diagrams, and generate an import bundle following guides/anki.md. Do not connect to or modify Anki.

Follow the separate [Anki import guide](anki.md). No Anki installation is needed to generate the files.

## Common problems

| Symptom | What to do |
|---|---|
| `pyproject.toml` cannot be found | Return to the extracted project folder, not `study/` or `.venv/`. |
| A package is missing | Run `uv sync --locked`; start both JupyterLab and scripts with `uv run`. Ask the agent before adding course-specific dependencies with `uv add`. |
| The check reports the wrong kernel | Ask the agent to inspect `uv run jupyter kernelspec list`; select/fix the project kernel rather than deleting global kernels. |
| PDF text is empty or a formula is missing | Inspect the rendered page; extraction is not OCR and may omit formulas. |
| You still see old notes | Save/close before rebuilding, then reopen the file; do not overwrite the external update with an old browser copy. |
| A script fails | Give the agent the full error and exact command. Fix the cause; do not skip the failed check. |

Your sources and study output are private by default. Do not publish `materials/`, `study/`, or `output/` merely because the template itself is open source.
