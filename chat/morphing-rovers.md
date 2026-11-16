# VSI chat pack — Morphing Rovers

> **For students using ChatGPT, Gemini or Claude in the browser or the app.**
> Upload this file to the chat and write: *"Read this file and guide me step by step."*
> 🇦🇱 Ngarkoje këtë skedar në chat dhe shkruaj: *"Lexo këtë skedar dhe më udhëhiq hap pas hapi."*

Project id (slug): `morphing-rovers` · Source: https://optimise.esa.int/challenge/spoc-2-morphing-rovers/About

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
   python -m vsi new morphing-rovers . --force
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

## Problem: ESA SpOC 2 — Morphing Rovers

Source: https://optimise.esa.int/challenge/spoc-2-morphing-rovers/About
Official repo / discussions: https://github.com/esa/SpOC2
Single-objective · continuous, very high-dimensional (neuro-evolution) · GECCO 2023.

### Story in one line
Design one rover with 4 shape "modes" plus the neural network that steers it, so that copies of it reach
30 samples on 6 Mars-like maps as fast as possible.

### Problem
Problem id: `morphing-rovers`. 6 maps × 5 scenarios = 30 scenarios, 500 time steps each.
Data: height maps `https://api.optimize.esa.int/data/spoc2/morphing/Maps/` (`MapX.JPG`), scenarios `https://api.optimize.esa.int/data/spoc2/morphing/coordinates.txt`
(rows `[map, Lx, Ly, Ax, Ay]` = landing site and sample). Default local path `./data/spoc2/morphing`.

### Simulation
- Each mode `i ∈ 0..3` is an 11×11 mask `F(i)`; speed factor `ν = V(F(i), T) ∈ [0,1]` compares it with the 11×11
  terrain under the rover. Position update `r(t+1) = r(t) + ν · v_max · (cos α, sin α)`.
- A neural network (2 conv layers on an 89×89 terrain view + dense layers on the rover state + recurrent layer)
  outputs a mode-switch signal and an angular velocity `ω ∈ [-π/4, π/4]`.
- Stops when the sample is reached (distance ≤ 6), jumps to the end if the rover leaves the map.

### Decision vector (19 133 values)
1. 484 mask values (4 × 11 × 11), in `[-100, 100]`, mask centres in `[1e-16, 100]`.
2. 146 biases + 18 496 weights of the network, in `[-100, 100]` (layer order given on the official page / UDP).
3. 7 integer hyper-parameters `[p1, p2, a1, a2, a3, a4, a5]`: pooling type (0 max, 1 avg) after each conv layer and
   activation functions (0 Sigmoid, 1 Hard Sigmoid, 2 Tanh, 3 Hard Tanh, 4 Softsign, 5 Softplus, 6 ReLU; a5 only 0–4).

### Objective (minimise)
Per scenario `f = (T / T_min) · (1 + d / d0)` — `T` time used, `T_min` straight-line time at max speed,
`d0` start distance, `d` final distance (0 if reached). Score = mean over all scenarios.

### Submission format
JSON file (one decision vector), uploaded at https://optimise.esa.int/submit:
```json
[
  {
    "decisionVector": [ x ],
    "problem": "morphing-rovers",
    "challenge": "spoc-2-morphing-rovers"
  }
]
```
Python: `from submission_helper import create_submission` (https://api.optimize.esa.int/data/tools/submission_helper.py), or `vsi.esa.write_submission`.

### Useful UDP features
`udp.fitness(x)`, `udp.pretty(x)` (table per scenario), `udp.plot(x, plot_modes=True, plot_mode_efficiency=True)`,
`udp.example()`; constants `NUM_BIASES`, `NUM_WEIGHTS`, `NUM_MODES`, `MASK_SIZE`, `MASK_CENTRES`;
`MAPS_PER_EVALUATION` / `SCENARIOS_PER_MAP` to train on fewer scenarios. Gradients are off by default
(remove `self._turn_off_gradients()` to train with gradient descent).

### Why it is hard
~19 000 continuous parameters, a non-differentiable simulator and an expensive fitness. Typical approaches:
evolution strategies (CMA-ES / sep-CMA, OpenAI-ES) on a subset of parameters, hand-designed masks + a simple
controller first, then neuro-evolution.

---

## Requirements checklist (docs/REQUIREMENTS.md)

## Requirements checklist

Tick a box (`[x]`) only when it is done **and** verified. `python tasks.py check` reads this file.

### Problem & data
- [x] Problem statement copied from the official page (docs/PROBLEM.md)
- [ ] Official data + evaluation code downloaded and wired (`python tasks.py data`) <!-- auto:data -->
- [ ] Official packages installed (torch, torchvision, imageio) and udp.example() evaluates
- [ ] udp.example() evaluates and the result is reproduced by our run script
- [ ] Official example / sample solution evaluates to the expected value (test)

### Algorithms
- [ ] Baseline (random search) runs end to end with the official fitness <!-- auto:baseline -->
- [ ] Hand-designed baseline (sensible masks + controller that steers straight to the target)
- [ ] Evolutionary method (GA / ES / CMA-ES) on masks and network parameters
- [ ] Training on a subset of scenarios + validation on all 30
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
