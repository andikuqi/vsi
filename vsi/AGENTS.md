# VSI — read this first (for AI agents)

The student copied this `vsi/` folder into their project so that you (the AI agent) can set it up for them.
The student may be a beginner: do the commands yourself and explain each step in simple words
(reply in the student's language — often Albanian).

## Setup (do this once)
Run from the student's project root (the folder that contains `vsi/`):

1. Find their project: `python -m vsi find <words from the project title>`
   If you are unsure which one it is, run `python -m vsi list` and ask the student.
2. Add the project files: `python -m vsi new <slug> . --force`
   - The student's existing files are never overwritten.
   - This creates `AGENTS.md` in the project root: **from now on follow that file**.
3. `python tasks.py setup` then `python tasks.py test` (must pass).
4. Tell the student, in a few short sentences, what was created and what the next step is
   (read `docs/PROBLEM.md`, then the first algorithm).

## Rules
- Do not edit anything inside `vsi/` — it is a library. Import from it (`from vsi.measure import Meter`, …).
- Keep `vsi/` committed in the project so classmates and other agents have it.
- VSI gives infrastructure, not solutions: the algorithms are the student's work. Help them understand every line.
