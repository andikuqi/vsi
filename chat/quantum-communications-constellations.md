# VSI chat pack — Quantum Communications Constellations

> **For students using ChatGPT, Gemini or Claude in the browser or the app.**
> Upload this file to the chat and write: *"Read this file and guide me step by step."*
> 🇦🇱 Ngarkoje këtë skedar në chat dhe shkruaj: *"Lexo këtë skedar dhe më udhëhiq hap pas hapi."*

Project id (slug): `quantum-communications-constellations` · Source: https://optimise.esa.int/challenge/spoc-2-quantum-communications-constellations/About

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
   python -m vsi new quantum-communications-constellations . --force
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

## Problem: ESA SpOC 2 — Quantum Communications Constellations

Source: https://optimise.esa.int/challenge/spoc-2-quantum-communications-constellations/About
Official repo / discussions: https://github.com/esa/SpOC2 ·
UDP: https://api.optimize.esa.int/media/problems/spoc-2-quantum-communications-constellations-quantum-communications-constellatio_DhZfx09.py
**Bi-objective** · mixed integer + continuous · GECCO 2023.

### Story in one line
Design two Walker constellations and choose 4 rover sites so that quantum links from 7 motherships to the rovers
are cheap, while keeping the number and quality of satellites (cost) low.

### Problem
Problem id: `quantum-communications-constellations`.
Data: 100 candidate rover positions (lat, lon in rad) `https://api.optimize.esa.int/data/spoc2/constellations/rovers.txt`
(local path expected `./data/spoc2/constellations/rovers.txt`).

### Decision vector (20 values)
`x = [a1, e1, i1, w1, eta1] + [a2, e2, i2, w2, eta2] + [S1, P1, F1] + [S2, P2, F2] + [r1, r2, r3, r4]`
- Constellation 1: `a1 ∈ [1.06, 1.8]` (normalised), `e1 ∈ [0, 0.02]`, `i1 ∈ [0, π]`, `w1 ∈ [0, 2π]`, `eta1 ∈ [1, 1000]`.
- Constellation 2: `a2 ∈ [2, 3.5]`, `e2 ∈ [0, 0.1]`, `i2 ∈ [0, π]`, `w2 ∈ [0, 2π]`, `eta2 ∈ [1, 1000]`.
- Walker parameters (integers): satellites per plane `S ∈ [4, 10]`, planes `P ∈ [2, 10]`, phasing `F ∈ [0, 9]`.
- Rovers: 4 line indices `r ∈ [0, 99]` in `rovers.txt`.

### Constraints (satisfied when ≤ 0)
- Any two selected rovers at least 3 000 km apart.
- Two satellites can be part of a path only if at least 50 km apart.

### Objectives (both minimised, normalised)
- `J1` = average over mothership–rover pairs and 10 years of the cheapest path cost
  `QC = Σ ( -log(η_(i+1)) + 2·log(L_i) ) + 1 / sin(π/2 - θ_Z)`, with line of sight on every link and zenith angle
  `θ_Z ≤ π/3` on the last link.
- `J2 = η1·S1·P1 + η2·S2·P2` (cost of the constellations).

`J1, J2, c1, c2 = udp.fitness(x)`.
Score: **hypervolume** of the submitted set with reference point `[1.2, 1.4]`, × 10 000. Up to **100** vectors.

### Submission format
JSON file (a list of decision vectors), uploaded at https://optimise.esa.int/submit:
```json
[
  {
    "decisionVector": [ x1, x2, ... ],
    "problem": "quantum-communications-constellations",
    "challenge": "spoc-2-quantum-communications-constellations"
  }
]
```
Python: `from submission_helper import create_submission` (https://api.optimize.esa.int/data/tools/submission_helper.py), or `vsi.esa.write_submission`.

### Why it is hard
Mixed integer/continuous, two conflicting objectives, constraints, and an expensive simulation
(shortest paths in a time-varying graph over 10 years). Typical approach: multi-objective EA (NSGA-II / MOEA/D)
or a sweep over the integer Walker parameters with continuous local optimisation, plus Pareto filtering.

---

## Requirements checklist (docs/REQUIREMENTS.md)

## Requirements checklist

Tick a box (`[x]`) only when it is done **and** verified. `python tasks.py check` reads this file.

### Problem & data
- [x] Problem statement copied from the official page (docs/PROBLEM.md)
- [ ] Official data + evaluation code downloaded and wired (`python tasks.py data`) <!-- auto:data -->
- [ ] Official packages installed (pykep, pygmo, sgp4, networkx) and udp.example() evaluates
- [ ] udp.example() evaluates; own Pareto filter + hypervolume (ref [1.2, 1.4]) match pygmo on a test set
- [ ] Official example / sample solution evaluates to the expected value (test)

### Algorithms
- [ ] Baseline (random search) runs end to end with the official fitness <!-- auto:baseline -->
- [ ] Rover-site selection respecting the 3 000 km constraint (greedy / exhaustive on a shortlist)
- [ ] Multi-objective method (NSGA-II / MOEA/D or weighted-sum sweep)
- [ ] Sweep of integer Walker parameters (S, P, F) with continuous optimisation of the orbits
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
