# Setup tutorial and local study tools

Status: implemented

## Problem

Learners cannot follow the existing entry point from Python installation to a visible Notebook. The private workflow's scripts assume one machine and course. Card creation must not require a running Anki instance or an integration service.

## Decision

Paired Windows tutorials under guides/ explain setup and study. uv manages the project environment through pyproject.toml, uv.lock, and .python-version. Local scripts prepare PDF pages, build declarative Notebooks, run clean-kernel checks, and export cards. The agent operates on files; JupyterLab displays and runs them. Learners start with a framework and progressively fill units. The [tool reference](../../../guides/tools.md) owns commands and formats.

Export UTF-8 TSV plus flattened image assets and import instructions. Keep stable note IDs in the first field of a user-created STS note type. The user performs import and checks a small batch. Do not connect to Anki, install MCP, synchronize, or delete cards.

## Alternatives considered

Copying private scripts unchanged retains fixed paths and course-specific assumptions. Anki packages can bundle media conveniently but require more format-specific tooling; TSV and media need a manual copy step but keep export inspectable and independent of Anki. CSV also works; tabs make prose containing commas easier to inspect. A full example course remains deferred.

## Verification

On Windows, uv 0.12.19 created the isolated environment with Python 3.12.14. `uv run --locked python -m unittest discover -s tests -v` passed 17 tests, covering document links and JSON illustrations, blank-page numbering, source preservation, coverage failures, learner-cell preservation, edit conflicts and reconciliation, local assets, real kernel execution and failures, TSV/media export, CLI invocation, and JupyterLab startup with the expected root directory. Test inputs are synthetic technical fixtures, not private course extracts. No Anki API, database access, or synchronization dependency is present. Desktop Anki import and other operating systems are outside this iteration's acceptance scope.

## Consequences

Extracted text cannot establish visual or mathematical correctness. Notebook execution runs arbitrary code and is not sandboxing. Text import requires one-time note-type setup and a separate media copy. Windows is the documented setup target; the exporter delivers files for user-controlled import, not application integration.

## Evidence

[uv projects](https://docs.astral.sh/uv/guides/projects/), [JupyterLab startup](https://jupyterlab.readthedocs.io/en/stable/getting_started/starting.html), [nbclient execution](https://nbclient.readthedocs.io/en/latest/client.html), [Anki text import](https://docs.ankiweb.net/importing/text-files.html), and [Anki packages](https://docs.ankiweb.net/exporting.html) inform these contracts.
