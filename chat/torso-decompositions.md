# VSI chat pack — Torso Decompositions

> **For students using ChatGPT, Gemini or Claude in the browser or the app.**
> Upload this file to the chat and write: *"Read this file and guide me step by step."*
> 🇦🇱 Ngarkoje këtë skedar në chat dhe shkruaj: *"Lexo këtë skedar dhe më udhëhiq hap pas hapi."*

Project id (slug): `torso-decompositions` · Source: https://optimise.esa.int/challenge/spoc-3-torso-decompositions/About

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
   python -m vsi new torso-decompositions . --force
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

## Problem: ESA SpOC 3 — Torso Decompositions

Source: https://optimise.esa.int/challenge/spoc-3-torso-decompositions/About
Official code (scorer, submission helper): https://github.com/esa/SpOC3
Discussions: https://github.com/esa/SpOC3/discussions

### Input
A connected, undirected, simple graph `G` given as an edge list (one `u v` per line).
Vertices are `0 … n-1`. Three instances:

| Problem id     | File        | URL |
|----------------|-------------|-----|
| `small-graph`  | `easy.gr`   | https://api.optimize.esa.int/data/spoc3/torso/easy.gr |
| `medium-graph` | `medium.gr` | https://api.optimize.esa.int/data/spoc3/torso/medium.gr |
| `large-graph`  | `hard.gr`   | https://api.optimize.esa.int/data/spoc3/torso/hard.gr |

### Decision vector
`x = [p1, p2, …, pn, t]` — a permutation of all `n` vertices followed by a threshold `t ∈ {0, …, n-1}`.

### Semantics
1. **Orientation:** edge `{u, v}` is oriented `u → v` iff `u` comes before `v` in the permutation.
2. **Fill-in:** scan the permutation left to right. When at vertex `u`, for every two out-neighbours
   `v, w` of `u` that are not adjacent, add edge `{v, w}` (oriented by the permutation).
   (This is the classic *elimination game*; the result is a chordal completion of `G`.)
3. **Torso:** the last `n - t` vertices of the permutation. **Size** = `n - t`.
4. **Width:** the maximum out-degree (counting fill edges) of any vertex in the torso.

Worked example (from the official page) — edges `0-1 0-2 1-6 2-8 3-8 3-9 4-5 4-6 4-7`,
`x = [0,1,2,4,5,3,6,8,9,7, 6]` → torso `[6,8,9,7]`, size 4, width 2 — use it as the first test of your evaluator.

### Objectives (bi-objective)
- **Maximise torso size** ⇔ minimise `t`.
- **Minimise torso width.**

Submit up to **20** decision vectors approximating the Pareto front. Quality is measured with the
**hypervolume indicator**. The width of the whole permutation is guaranteed/required to be ≤ 500;
worse solutions are scored as width 501.

### Submission format
```json
[
  {
    "decisionVector": [ x1, x2, ..., x20 ],
    "problem": "small-graph",
    "challenge": "spoc-3-torso-decompositions"
  }
]
```
`vsi.esa.write_submission` writes this file. For final scoring, verify with the official UDP from `esa/SpOC3`.

### Why it is hard
Choosing the ordering is equivalent to choosing an elimination ordering; minimising the width of an
elimination ordering is the treewidth problem, which is NP-hard. Hence heuristics / metaheuristics.

---

## Requirements checklist (docs/REQUIREMENTS.md)

﻿# Requirements checklist

Tick a box (`[x]`) only when it is done **and** verified. `python tasks.py check` reads this file.

### Problem & data
- [x] Problem formally defined (docs/PROBLEM.md)
- [ ] Official graphs downloaded (`python tasks.py data`) <!-- auto:data -->
- [ ] Graph loader (edge list -> adjacency) with tests
- [ ] Reference evaluator implemented and tested against the official example (4, 2)

### Algorithms
- [ ] Baseline (random search) runs end to end with the official fitness <!-- auto:baseline -->
- [ ] Greedy constructive heuristic (e.g. min-degree or min-fill ordering)
- [ ] Improvement method (local search / simulated annealing / tabu)
- [ ] Multi-objective method producing several trade-offs (e.g. sweep of t, evolutionary / NSGA-style)
- [ ] At least one idea designed or modified by us (documented in DECISIONS.md)

### Analysis
- [ ] Pseudocode for every algorithm (README)
- [ ] Time & space complexity for every algorithm (README)
- [ ] Explanation why the problem is NP-hard / why heuristics are used

### Experiments
- [ ] Metrics recorded: runtime, peak memory, solutions evaluated <!-- auto:metrics -->
- [ ] Results on all three graphs
- [ ] Pareto front plot per graph + hypervolume
- [ ] Algorithm comparison table
- [ ] Scaling discussion (theory vs measured)

### Delivery
- [ ] Submission JSON for each problem, verified with the official scorer
- [ ] README report complete (all sections filled)
- [ ] Defense preparation: can explain every algorithm and design decision
