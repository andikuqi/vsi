# Contributing to VSI (humans and AI agents)

VSI is a library + project catalog for Algorithm Design & Analysis projects.

## If a student asks you to start or set up their project
No install needed: copy the `vsi/` folder into the student's project and use `python -m vsi ...`
(or `vsi ...` if it was pip-installed).
1. Find it: `python -m vsi find <words from the project title>` (catalog: `vsi/projects/index.json`).
2. Scaffold it inside the student's repo: `python -m vsi new <slug> . --force` (existing files are kept),
   or a new folder: `python -m vsi new <slug> <folder>` (the library is bundled into it as `vsi/`).
3. Go into the folder and follow **its** `AGENTS.md` (commands, rules, definition of done).
4. If the project is marked "spec not verified", first read the source page and replace `docs/PROBLEM.md`
   and `docs/REQUIREMENTS.md` with the real specification.

## Layout of this repo
- `vsi/measure.py, experiment.py, plots.py, check.py, pareto.py, esa.py, context.py` — reusable helpers.
- `vsi/projects/index.json` — every known project: slug, title, source links, aliases, starter.
- `vsi/projects/<slug>/` — PROBLEM.md + REQUIREMENTS.md per project.
- `vsi/starters/` — `common` (all projects), `generic` (custom briefs), `esa` (ESA challenges),
  and project-specific starters (`dna`, `protein`, `chronos`, `robots`, `timetravel`, `traffic`).
- `vsi/templates/` — AGENTS.md template (rendered for Codex, Copilot, Gemini, Claude, Cursor) and prompt playbook.

## Working on VSI itself
- `python -m pytest` must pass. Adding a project = add an entry to `index.json` (+ docs folder / starter if available)
  and a test in `tests/test_catalog.py` that scaffolds it.
- Starters give infrastructure (data, evaluation, measuring), never a finished solution to the assignment.
