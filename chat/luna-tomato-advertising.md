# VSI chat pack — Luna Tomato Advertising

> **For students using ChatGPT, Gemini or Claude in the browser or the app.**
> Upload this file to the chat and write: *"Read this file and guide me step by step."*
> 🇦🇱 Ngarkoje këtë skedar në chat dhe shkruaj: *"Lexo këtë skedar dhe më udhëhiq hap pas hapi."*

Project id (slug): `luna-tomato-advertising` · Source: https://optimise.esa.int/challenge/spoc-4-luna-tomato-advertising/About

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
   python -m vsi new luna-tomato-advertising . --force
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

## Problem: ESA SpOC 4 — Luna Tomato Advertising

Source: https://optimise.esa.int/challenge/spoc-4-luna-tomato-advertising/About
Official repo / discussions: https://github.com/esa/SpOC4 (UDP class `celestial_morse_code`)
Single-objective with a feasibility threshold · mixed integer + continuous.

### Story in one line
Spacecraft passing in front of the Moon dim its light; schedule a fleet so the dimming spells the Morse code of
"Tomatoes for sale" — with as few spacecraft as possible.

### Problem
Problem id: `tie-breaker` (dimension 4 674).

Orbit databases (CR3BP, Earth–Moon): 188 DRO, 291 Lyapunov, 300 Axial → `N = 779` orbit slots,
at most `max_per_orbit = 5` spacecraft per orbit. Each database row:
`[x, y, z, vx, vy, vz, period_rad, occultation_frequency, occultation_amplitude]`;
`period_days = period_rad / (2π) · 27.8511`.

Morse timing (units of one occultation width 0.1036 days): dot 2, dash 5, intra-character gap 2,
letter gap 5, word gap 7. Target: `t, target = udp.morse_to_signal(" Tomatoes for sale ")`, time grid of 2 710 samples.

### Decision vector (length N + 5N = 4 674)
- `sel = x[:N]` — integers in `[0, 5]`: number of spacecraft in orbit slot i (order: DRO, Lyapunov, Axial).
- `phs = x[N:]` — for slot i, phases `phs[5i : 5i+5]`, the first `sel[i]` are used, each in `[0, 2π)`.

### Objective
`obj, num_selected, mse = udp.fitness(x, postprocess=True)`; ranking:
1. Feasible (`mse ≤ 0.05`) beats infeasible.
2. Among feasible: fewer spacecraft is better.
3. Among infeasible: lower MSE-based penalty is better.

### Submission format
JSON file (one decision vector), uploaded at https://optimise.esa.int/submit:
```json
[
  {
    "decisionVector": [ x ],
    "problem": "tie-breaker",
    "challenge": "spoc-4-luna-tomato-advertising"
  }
]
```
Python: `from submission_helper import create_submission` (https://api.optimize.esa.int/data/tools/submission_helper.py), or `vsi.esa.write_submission`.

**Check the challenge id:** the page's own helper example uses `"spoc-4-luna-tomato-advertisment"` while the page
URL is `spoc-4-luna-tomato-advertising`. Confirm which one the platform accepts before the final submission.

### Dependencies (official)
`numpy`, `heyoka`, `matplotlib`.

### Hints from the page
Start feasible (many spacecraft), then remove spacecraft; with `sel` fixed, optimise phases to lower the MSE;
validate often with `udp.plot_signal(x)` / `udp.plot_orbits(x)`; keep `mse < 0.05` during edits.

### Why it is hard
Choosing which orbits to use is a set-cover-like combinatorial problem (minimise assets covering all pulses of the
signal), coupled with continuous phase tuning. Natural approaches: greedy cover of the Morse pulses,
then pruning + local search on phases.

---

## Requirements checklist (docs/REQUIREMENTS.md)

## Requirements checklist

Tick a box (`[x]`) only when it is done **and** verified. `python tasks.py check` reads this file.

### Problem & data
- [x] Problem statement copied from the official page (docs/PROBLEM.md)
- [ ] Official data + evaluation code downloaded and wired (`python tasks.py data`) <!-- auto:data -->
- [ ] Official packages installed (heyoka) and the target Morse signal generated
- [ ] Own signal reconstruction / MSE matches udp.fitness on sample solutions
- [ ] Official example / sample solution evaluates to the expected value (test)

### Algorithms
- [ ] Baseline (random search) runs end to end with the official fitness <!-- auto:baseline -->
- [ ] Constructive heuristic: greedily add (orbit, phase) occultations that cover target pulses
- [ ] Pruning step: remove spacecraft while mse ≤ 0.05
- [ ] Phase optimisation for fixed selection (local search / SA / CMA-ES)
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
