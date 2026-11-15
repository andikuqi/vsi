# VSI

**Agent-ready scaffolding for Algorithm Design & Analysis projects** — by Void.

Every project starts from a working base instead of from zero: problem statement, requirements checklist,
data generator or official-data loader, measuring (time, memory, explored states, pruning %), experiments,
charts, report template, and instruction files for **Codex, GitHub Copilot, Gemini, Claude Code and Cursor**.

> 🇦🇱 **Shqip:** VSI i jep çdo studenti një projekt gati për punë: përshkrimin e problemit, listën e
> kërkesave, gjeneruesin e të dhënave, matjet (koha, memoria, gjendjet e eksploruara), grafikët, shabllonin e
> raportit dhe udhëzimet për agjentin AI (Codex, Copilot, Gemini, Claude, Cursor). Studenti merret vetëm me
> algoritmin e vet.

## Install
```
git clone <this repo> vsi
pip install -e vsi
```

## Use
```
vsi list                              # all projects
vsi find torso                        # find yours by name
vsi new torso-decompositions my-proj  # ready project
cd my-proj
python tasks.py setup
python tasks.py test
python tasks.py run
python tasks.py plots
python tasks.py check
```
Already have a repo? Inside it: `vsi new <slug> . --force`.
Using ChatGPT / Copilot 365 / Gemini web? Run `python tasks.py context` and upload `CONTEXT.md`, then follow `docs/PROMPTS.md`.

## Catalog (18 projects)
| Kind | Projects |
|---|---|
| ESA SpOC challenges | Torso Decompositions ✅, Interferometric Mission, Programmable Cubes, Luna Tomato Logistics, Luna Tomato Advertising, Keplerian Tomato TSP, Morphing Rovers, Quantum Communications Constellations, Trappist Tour, Delivery Scheduling, Mining |
| Professor briefs | DNA Genome Reconstruction, Protein Structure Prediction, Chronos Nexus, Multi-Robot Coordination, Time Travel Paradox, Traffic Flow (Dijkstra & A*), Trigger Arc TSP |

✅ = problem statement verified from the official page. ESA entries ship a generic ESA starter (official UDP loader,
random-search baseline, submission writer); unverified ones ask the agent to copy the real spec first.
Briefs ship a data generator for every required size.

## What gets generated
```
my-proj/
├── AGENTS.md  GEMINI.md  CLAUDE.md  .github/copilot-instructions.md  .cursor/rules/vsi.mdc
├── tasks.py                  setup | data | test | run | plots | check | context
├── docs/  PROBLEM.md  REQUIREMENTS.md  PLAN.md  DECISIONS.md  PROMPTS.md
├── src/   run.py  algorithms.py  generator.py (or ESA loader / project package)
├── tests/
└── README.md                 report template
```

## Library
```python
from vsi.measure import Meter               # time, peak memory, meter.count(), meter.prune()
from vsi.experiment import run_experiments  # algorithms x instances -> results/metrics.csv
from vsi.pareto import pareto_filter, hypervolume, select_best
from vsi.esa import load_module, write_submission
```

## Fair use
VSI provides infrastructure, not solutions. Courses require students to design, implement and explain their
own algorithms — check your course rules before sharing work.

License: MIT
