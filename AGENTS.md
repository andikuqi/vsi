<!-- vsi:bootstrap -->
# This project uses VSI

Instructions for AI agents (Codex, Copilot, Gemini, Claude, Cursor, …). Read them before doing anything else.

The `vsi/` folder in this project is **VSI**: a library + catalog that sets up Algorithm Design & Analysis
projects (problem statement, requirements, data, tests, experiments, charts, report).

## If the project is not set up yet (there is no `tasks.py` next to this file)
When the student says anything like "start", "fillo puno", "set up my project", "help me with my project":
1. Read `vsi/AGENTS.md` and follow its **Setup** steps (find the project, `python -m vsi new <slug> . --force`,
   `python tasks.py start`). If you do not know the project title, ask the student for it.
2. Setup replaces this file with the project's own instructions. From then on, follow the new `AGENTS.md`.

## If the project is already set up (`tasks.py` exists)
Follow the instructions in this file's replacement; if you still see this text, run
`python -m vsi agents <slug> .` (slug in `vsi.json`) to regenerate them.

---
_Working on the VSI repository itself (it has `tests/test_catalog.py`)? See CONTRIBUTING.md._
