# Try it once: from source material to your own notes

English · [简体中文](first-session.zh-CN.md)

Complete [setup in the README](../README.md), restart your Agent, and open a new session in the same project folder. Send the prompts below to **your Agent**; read the notes in **JupyterLab**. You do not need to write scripts or lesson specifications yourself.

## 1. Generate a Notebook framework

Use the bundled [central tendency example PDF](../examples/central-tendency/README.md); no personal course files are needed. Send:

> Please preprocess summarizing_distributions.pdf.

The Agent follows the project skill to prepare the source, divide it into units, and create a Notebook framework. If it asks about your goals or requests confirmation of the unit division, just answer normally.

Open a terminal in the project folder (the one containing `pyproject.toml`) and run:

```sh
uv run jupyter lab
```

Leave the terminal running. In JupyterLab's left file browser, enter `study/notes/` and open the file the Agent gives you. Look at the unit division: for example K01 and K02, their titles, and source pages. This is the framework; the explanations have not been filled in yet.

## 2. Ask the Agent to teach K01

Save and close the Notebook tab, then send:

> Let's start with K01.

When the Agent finishes, reopen the same Notebook and read the explanation of K01.

## 3. Ask questions and improve the notes

Ask about anything unclear in your own words. There is no required wording. For example:

> Why can the same dataset have different “centers”? I don't quite get it.

You could also ask “What does this symbol mean?”, “How did you calculate this step?”, or “What happens if we change one number?”. **Save and close the Notebook tab before sending a request that changes it.**

The Agent will improve the notes based on your question. When it finishes, reopen the same file and see what changed.

## 4. Run the code

Click a code cell and press **Ctrl+Enter**. Results or figures appear below. Run cells from top to bottom the first time, and wait while a cell shows `[*]`. See the default shortcuts in [JupyterLab's official documentation](https://jupyterlab.readthedocs.io/en/stable/user/commands.html).

If code is confusing or fails, ask the Agent about it too. Only run code you trust.

## 5. Move on when you are ready

Keep asking about anything unclear; the Agent will keep improving the notes. When you feel you have learned this unit, save and close the Notebook, then say:

> That makes sense now. Let's move on to K02.

Use this cycle for each unit; you do not need a whole course's explanations at once. For your own course, place the source in `materials/`, tell the Agent its path, your goal, and your starting knowledge, and begin with the framework again.
