# VSI chat pack — Programmable Cubes

> **For students using ChatGPT, Gemini or Claude in the browser or the app.**
> Upload this file to the chat and write: *"Read this file and guide me step by step."*
> 🇦🇱 Ngarkoje këtë skedar në chat dhe shkruaj: *"Lexo këtë skedar dhe më udhëhiq hap pas hapi."*

Project id (slug): `programmable-cubes` · Source: https://optimise.esa.int/challenge/spoc-3-programmable-cubes/About

## Instructions for the AI (read this first, follow it the whole conversation)

You are helping a university student with an **Algorithm Design & Analysis** project. The student may be a
beginner. **Reply in the student's language** (often Albanian). You cannot see their computer, so:

1. Work in **small steps**. Give the exact commands to copy, then **wait** for the student to paste the output.
2. Before the first command, ask which system they use. Use `python` on **Windows** and `python3` on
   **macOS / Linux** in every command you give.
3. When you write code, give the **complete content of one file** and its path (e.g. `src/algorithms.py`),
   never fragments to merge. After every change the student runs `python tasks.py test`.
4. The algorithms are the **student's own work**: explain the idea, pseudocode and complexity, keep the code
   simple and commented, and check they understand it (they must defend it in front of the professor).
   Do not import solver / optimisation libraries for the core algorithm.
5. Never invent results. Numbers in the report come from `results/metrics.csv`.

### Step 1 — set up the project (once)
1. Python 3.10 or newer: `python --version` (Windows) / `python3 --version` (macOS, Linux).
   If it is missing or older: install it from https://www.python.org/downloads/ (Windows: tick "Add to PATH").
2. Download VSI: https://github.com/andikuqi/vsi → **Code → Download ZIP**, unzip it.
3. Copy the folder **`vsi`** and the file **`AGENTS.md`** into the student's project folder
   (an empty folder or their existing GitHub repo).
4. Open a terminal **in the project folder** (Windows: in the folder, type `cmd` in the address bar and press
   Enter; macOS: right-click the folder → New Terminal at Folder; Linux: right-click → Open in Terminal) and run:
   ```
   python -m vsi new programmable-cubes . --force
   python tasks.py start
   ```
   (`python3` instead of `python` on macOS / Linux.) `start` installs what is needed, downloads the data,
   runs the tests and a first run, makes charts, starts the report and prints **progress + the next step**.
   Ask the student to paste that output, then explain it in a few simple sentences.

### Step 2 — every work session
1. The student runs `python tasks.py context` and uploads the new **`CONTEXT.md`** (their current code,
   progress and results) to this chat.
2. Take the **next step** it shows (first open requirement), explain it, write the code, then:
   `python tasks.py test` → tick the requirement in `docs/REQUIREMENTS.md` → `python tasks.py report`.
3. Useful commands: `python tasks.py run` (experiments), `python tasks.py plots` (charts),
   `python tasks.py check` (progress + next step).

---

## The project (docs/PROBLEM.md)

## Problem: ESA SpOC 3 — Programmable Cubes

Source: https://optimise.esa.int/challenge/spoc-3-programmable-cubes/About
Official code + data + 4 tutorial notebooks: https://github.com/esa/SpOC3/tree/main/Challenge%203%20Programmable%20Cubes
Single-objective (with a secondary length term) · combinatorial / planning · GECCO 2024.

### Story in one line
An ensemble of cubes must reshape itself, one pivoting move at a time, into a target spacecraft,
using as few moves as possible.

### Problems
| Problem id | Target | Cubes | Cube types | Max commands |
|---|---|---|---|---|
| `iss` | International Space Station | 148 | 3 | 6 000 |
| `jwst` | James Webb Space Telescope | 643 | 6 | 30 000 |
| `enterprise` | USS Enterprise | 1 472 | 10 | 100 000 |

Data (initial + target positions and types): `https://api.optimize.esa.int/data/spoc3/cubes/data/ISS`, `.../JWST/`, `.../Enterprise/`,
problem configs `https://api.optimize.esa.int/data/spoc3/cubes/problems/`, move logic `https://api.optimize.esa.int/data/spoc3/cubes/CubeMoveset.py`.
Cubes of the same type are interchangeable.

### Moves
A command picks a cube and rotates it around an edge (pivot around one cube or traverse to a neighbour — chosen automatically):
`0/1` = counter-clockwise / clockwise around z · `2/3` = around x · `4/5` = around y.
A move is legal only if (1) removing the cube keeps the ensemble connected and (2) the cube does not collide and
reconnects at its new place.

### Decision vector
`x = [c0, m0, c1, m1, …, cN, mN, -1]` — cube index then command. Evaluation stops at the first `-1`;
the chromosome must end with `-1`.

### Objective (minimise)
- `C(x)` = cubes on a correct target position (right type), `C_max` = number of cubes
- `L(x)` = commands used, `L_max` = maximum commands
- `F(x) = (1 - α)·C(x)/C_max + α·(1 - L(x)/L_max)`, `α = 0.1`, `F0 = F` with no moves
- `f(x) = -(F(x) - F0) / (1 - F0)` → 0 = unchanged, -1 = theoretical best

### Submission format
JSON file (one decision vector), uploaded at https://optimise.esa.int/submit:
```json
[
  {
    "decisionVector": [ x ],
    "problem": "iss",
    "challenge": "spoc-3-programmable-cubes"
  }
]
```
Python: `from submission_helper import create_submission` (https://api.optimize.esa.int/data/tools/submission_helper.py), or `vsi.esa.write_submission`.

Problem ids: `iss`, `jwst`, `enterprise`.

### Useful UDP features
`udp = programmable_cubes_UDP('ISS')` · `udp.fitness(x)` · `udp.pretty(x)` prints illegal moves ·
`udp.plot('ensemble' | 'target', [types])` · `udp.fitness(x, initial_configuration=cfg)` evaluates from an
intermediate state (much faster for incremental search).

### Dependencies (official)
Python 3.8+, `numba >= 0.56.4`, `numpy >= 1.23.5`, `matplotlib >= 3.6.3`.

### Why it is hard
Modular-robot reconfiguration: the state space is all connected shapes of the ensemble, moves are constrained
(connectivity + collisions) and later moves depend on earlier ones. Shortest reconfiguration is a search/planning
problem far too large for exhaustive search: use heuristic search (greedy matching of cubes to targets, BFS/A* for
single-cube paths, local search on the move sequence).

---

## Requirements checklist (docs/REQUIREMENTS.md)

## Requirements checklist

Tick a box (`[x]`) only when it is done **and** verified. `python tasks.py check` reads this file.

### Problem & data
- [x] Problem statement copied from the official page (docs/PROBLEM.md)
- [ ] Official data + evaluation code downloaded and wired (`python tasks.py data`) <!-- auto:data -->
- [ ] Own loader for the cube configurations (data/spoc3/cubes/...) into our data structures
- [ ] Own state representation + legal-move check, tested against the official UDP on random moves
- [ ] Official example / sample solution evaluates to the expected value (test)

### Algorithms
- [ ] Baseline (random search) runs end to end with the official fitness <!-- auto:baseline -->
- [ ] Greedy constructive planner (move one cube at a time towards a free target cell)
- [ ] Path search for a single cube (BFS / A* over legal pivot moves)
- [ ] Improvement method (remove redundant moves, local search / beam search on the sequence)
- [ ] At least one idea designed or modified by us (documented in DECISIONS.md)

### Analysis
- [ ] Pseudocode for every algorithm (README)
- [ ] Time & space complexity for every algorithm (README)
- [ ] Why the problem is hard / why heuristics are used

### Experiments
- [ ] Metrics recorded: fitness, runtime, peak memory, fitness evaluations <!-- auto:metrics -->
- [ ] Results on every problem instance
- [ ] Algorithm comparison table
- [ ] Convergence plot (best fitness over time) per problem
- [ ] Theory vs measured performance (scaling discussion)

### Delivery
- [ ] Submission JSON per problem, checked with the official fitness function
- [ ] README report complete (all sections filled)
- [ ] Defense preparation: can explain every algorithm and design decision
