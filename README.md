# Source to Study

English · [简体中文](README.zh-CN.md)

A reusable workspace for studying your own course materials with an AI tutor. Start with a source, build an explanation you can verify, practise without the answer, and keep track of what you can reproduce independently.

## Start your course

1. Download or clone this template. Put materials you are allowed to use in a local `materials/` directory.
2. Open the workspace with an AI assistant that can read local files. Ask it to read [AGENTS.md](AGENTS.md); if your tool does not load that file automatically, supply it explicitly.
3. Send the following prompt, filling in the brackets:

> Read AGENTS.md. Help me set up a course using templates/course.md in study/COURSE.md. My subject is [subject], my goal or assessment is [goal], and my preferred teaching language is [language]. My materials are in [path]. Ask about missing learning requirements, inspect the materials, and create a source map. Do not start teaching until we agree on the scope and starting point.

4. After agreeing on the starting point, ask: “Teach the first unit and maintain my notes using templates/lesson.md. Pause for my questions before advancing.”
5. At the end of a real study session, ask the assistant to record your next step and actual performance using [the session template](templates/session.md). In a new chat, ask it to read your course profile and latest session before resuming.

Your assistant creates the local `study/` directory. It contains your course profile, source map, notes, review questions, and session records. These are your working files, not contributions to this public template.

## What a study session produces

A lesson connects the source's goal to definitions, intermediate steps, a worked example, and a checkable result. Figures sit beside the explanation they support. Your questions help identify missing links; they do not turn the notes into a chat transcript.

Use [review questions](templates/review.md) to practise recall separately from reading. Tell the tutor whether you are preparing for a written exam, oral exam, project, or self-study: no assessment format is assumed.

Markdown templates work without a build system. This repository does not yet provide source-extraction scripts, a Notebook builder, or Anki export. The tutor must not invent commands or claim those capabilities exist.

## Files you use

- [Course profile](templates/course.md): goals, sources, language, assessment rules, and scope.
- [Lesson](templates/lesson.md): source-grounded teaching notes.
- [Review](templates/review.md): retrieval questions and separate answers.
- [Session](templates/session.md): observed performance and the next starting point.
- [Small original example](examples/README.md): how a learning unit is organized.

The forms contain English and Chinese field guidance; fill them in once in your chosen learning language.

## Keep your materials private

`materials/`, `study/`, `private/`, `cache/`, `work/`, and `output/` are ignored by Git. Ignoring files is not an access-control system: check your AI provider's data handling before sharing material, and inspect tracked files and history before publishing your workspace.

The [MIT license](LICENSE) applies to this template, not automatically to your course materials. Use only material you are entitled to use and follow your institution's AI rules.

Maintaining the template itself? See [developer documentation](docs/README.md).
