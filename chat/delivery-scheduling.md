# VSI chat pack — Delivery Scheduling

> **For students using ChatGPT, Gemini or Claude in the browser or the app.**
> Upload this file to the chat and write: *"Read this file and guide me step by step."*
> 🇦🇱 Ngarkoje këtë skedar në chat dhe shkruaj: *"Lexo këtë skedar dhe më udhëhiq hap pas hapi."*

Project id (slug): `delivery-scheduling` · Source: https://optimise.esa.int/challenge/spoc-delivery-scheduling/About

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
   python -m vsi new delivery-scheduling . --force
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

## Problem: ESA SpOC — Delivery Scheduling

Source: https://optimise.esa.int/challenge/spoc-delivery-scheduling/About (evaluation code / UDP linked from the problem page)
Single-objective · **purely combinatorial** (no astrodynamics needed) · GECCO 2022.

### Story in one line
Assign 340 asteroids to 12 processing stations (choosing one transfer opportunity each) and give every station
one non-overlapping activity window, so that the poorest station/material gets as much mass as possible.

### Problem
Problem id: `delivery-scheduling`. Data: `https://api.optimize.esa.int/data/spoc/scheduling/candidates.txt`
(local path `./data/spoc/scheduling/candidates.txt`), a dictionary
`{asteroid_id: {station_id: [[T_arr, mA, mB, mC], …]}}`.
Asteroids `1..340`, stations `1..12`, opportunity ids `1..8` (1-based, order in the list). Horizon 80 days.

### Decision vector (1 044 values)
`[T1i, T1f, …, T12i, T12f]` (24 window epochs in `[0, 80]`, by station id) followed by 340 triples
`[asteroid_id, station_id, opportunity_id]`; `station_id = 0` = not delivered.
`convert_to_chromosome()` fills in missing asteroids as unassigned.

### Constraints
- `0 ≤ Tki ≤ Tkf ≤ 80`; windows do not overlap; at least **1 day** between consecutive windows.
- Each asteroid assigned once, and `(asteroid, station, opportunity)` must exist in the database.
- Every delivered asteroid's arrival time lies inside its station's window.

### Objective (maximise)
`M_min = min over stations i, min over materials j ∈ {A, B, C} of M_(j,i)`.
`M_min, eq1, eq2, ineq1, ineq2 = udp.fitness(x)` (equalities satisfied at 0, inequalities at ≤ 0).

### Submission format
JSON file (one decision vector), uploaded at https://optimise.esa.int/submit:
```json
[
  {
    "decisionVector": [ x ],
    "problem": "delivery-scheduling",
    "challenge": "spoc-delivery-scheduling"
  }
]
```
Python: `from submission_helper import create_submission` (https://api.optimize.esa.int/data/tools/submission_helper.py), or `vsi.esa.write_submission`.

### Hint from the page
Given a valid assignment, the windows can always be set from the first to the last arrival at each station.

### Why it is hard
Max-min assignment with a scheduling (window ordering) layer — a generalised assignment / bin-balancing problem,
NP-hard. Typical approach: choose a station order and window boundaries, greedily assign asteroids to the currently
poorest station/material, then improve with swaps / moves (local search, simulated annealing, tabu) or an ILP on a
reduced model.

---

## Requirements checklist (docs/REQUIREMENTS.md)

## Requirements checklist

Tick a box (`[x]`) only when it is done **and** verified. `python tasks.py check` reads this file.

### Problem & data
- [x] Problem statement copied from the official page (docs/PROBLEM.md)
- [ ] Official data + evaluation code downloaded and wired (`python tasks.py data`) <!-- auto:data -->
- [ ] Own loader for candidates.txt into our data structures (asteroid -> station -> opportunities)
- [ ] Own evaluator (M_min + all constraints) equals udp.fitness on udp.example() and random solutions
- [ ] Official example / sample solution evaluates to the expected value (test)

### Algorithms
- [ ] Baseline (random search) runs end to end with the official fitness <!-- auto:baseline -->
- [ ] Greedy constructive (assign to the poorest station/material within windows)
- [ ] Window / station-order optimisation
- [ ] Improvement method (move / swap local search, simulated annealing or tabu)
- [ ] (Optional) exact model (ILP) on a small sub-instance to measure the optimality gap
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
