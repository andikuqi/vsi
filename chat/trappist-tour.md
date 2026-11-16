# VSI chat pack — Trappist Tour

> **For students using ChatGPT, Gemini or Claude in the browser or the app.**
> Upload this file to the chat and write: *"Read this file and guide me step by step."*
> 🇦🇱 Ngarkoje këtë skedar në chat dhe shkruaj: *"Lexo këtë skedar dhe më udhëhiq hap pas hapi."*

Project id (slug): `trappist-tour` · Source: https://optimise.esa.int/challenge/spoc-trappist-tour/About

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
   python -m vsi new trappist-tour . --force
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

## Problem: ESA SpOC — Trappist Tour

Source: https://optimise.esa.int/challenge/spoc-trappist-tour/About (evaluation code / UDP linked from the problem page)
**Bi-objective** · mixed integer + continuous · GECCO 2022.

### Story in one line
Fly a spacecraft from 10 AU into the TRAPPIST-1 system and visit all 7 planets once, trading total ΔV against
total mission time.

### Problem
Problem id: `trappist-tour`. No data file: the planets are inside the UDP.

### Decision vector (34 values)
- Entry leg `[u, v, T0]` — entry angles and duration of the first leg.
- 6 planet-to-planet legs `[beta, rp/rP, eta, T]` — flyby geometry, fraction of the leg before the deep-space
  manoeuvre, leg duration (in the order of the sequence).
- Planet sequence `[s0 … s6]`, integers `0..6` = planets b, c, d, e, f, g, h — must be a permutation.
- Bounds: `lb, ub = udp.get_bounds()`. Example: `udp.example()`. Encoding based on pykep `mga_1dsm`.

### Constraints
- Sequence is a permutation (equality constraint = 0).
- Closest approach to the star ≥ 834 840 km (inequality ≤ 0).

### Objectives (both minimised)
- Total impulsive ΔV [m/s]; total mission time [days].
- `DV, T, eq_constraint, ineq_constraint = udp.fitness(x)`.

Score: **hypervolume** with reference point `[2500, 4000]` — only solutions with ΔV < 2500 m/s and T < 4000 days count.
Up to **100** vectors. Score 0 = no submitted vector inside the reference box.

### Submission format
JSON file (a list of decision vectors), uploaded at https://optimise.esa.int/submit:
```json
[
  {
    "decisionVector": [ x1, x2, ... ],
    "problem": "trappist-tour",
    "challenge": "spoc-trappist-tour"
  }
]
```
Python: `from submission_helper import create_submission` (https://api.optimize.esa.int/data/tools/submission_helper.py), or `vsi.esa.write_submission`.

### Why it is hard
The planet order is a permutation problem (7! = 5 040 orders) and, for each order, the trajectory is a nonlinear
continuous optimisation with many local optima. Typical approach: enumerate / prune orders, optimise the continuous
legs per order (DE / CMA-ES / multi-start local search), then build the Pareto front.

---

## Requirements checklist (docs/REQUIREMENTS.md)

## Requirements checklist

Tick a box (`[x]`) only when it is done **and** verified. `python tasks.py check` reads this file.

### Problem & data
- [x] Problem statement copied from the official page (docs/PROBLEM.md)
- [ ] Official data + evaluation code downloaded and wired (`python tasks.py data`) <!-- auto:data -->
- [ ] Official packages installed (pykep, pygmo) and udp.example() evaluates
- [ ] udp.example() evaluates; own Pareto filter + hypervolume (ref [2500, 4000]) tested
- [ ] Official example / sample solution evaluates to the expected value (test)

### Algorithms
- [ ] Baseline (random search) runs end to end with the official fitness <!-- auto:baseline -->
- [ ] Order selection (enumerate the 5 040 sequences with a cheap estimate, or a permutation GA)
- [ ] Continuous optimiser for a fixed order (DE / CMA-ES / multi-start local search)
- [ ] Multi-objective method (NSGA-II, or weighted sum / ε-constraint sweep)
- [ ] At least one idea designed or modified by us (documented in DECISIONS.md)
- [ ] Several trade-off solutions per run (Pareto front), hypervolume computed with the official reference point

### Analysis
- [ ] Pseudocode for every algorithm (README)
- [ ] Time & space complexity for every algorithm (README)
- [ ] Why the problem is hard / why heuristics are used

### Experiments
- [ ] Metrics recorded: fitness, runtime, peak memory, fitness evaluations <!-- auto:metrics -->
- [ ] Results on every problem instance
- [ ] Algorithm comparison table
- [ ] Pareto front plot + hypervolume per problem
- [ ] Theory vs measured performance (scaling discussion)

### Delivery
- [ ] Submission JSON per problem, checked with the official fitness function
- [ ] README report complete (all sections filled)
- [ ] Defense preparation: can explain every algorithm and design decision
