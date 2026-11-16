# VSI chat pack — Chronos Nexus: Autonomous Interstellar Civilization Optimization

> **For students using ChatGPT, Gemini or Claude in the browser or the app.**
> Upload this file to the chat and write: *"Read this file and guide me step by step."*
> 🇦🇱 Ngarkoje këtë skedar në chat dhe shkruaj: *"Lexo këtë skedar dhe më udhëhiq hap pas hapi."*

Project id (slug): `chronos-nexus` · Source: professor brief (see PROBLEM.md)

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
   python -m vsi new chronos-nexus . --force
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

## Chronos Nexus: Autonomous Interstellar Civilization Optimization

Source: professor's brief (condensed here; the original is long — keep it next to this file if you have it).

### Goal
Manage an interstellar civilization on a large **dynamic weighted graph** (planets, colonies, stations,
spacecraft, resources, routes, wormholes, missions, hazards). Continuously make high-quality decisions while
minimising computational cost. Decompose into subproblems; several are NP-hard.

### Model (minimum attributes)
- **Route (edge):** distance, travel time, fuel, risk, capacity, reliability/failure probability, availability.
- **Planet:** population, production, consumption, storage, technology, defense, strategic importance, location.
- **Resources:** food, water, energy, fuel, medicine, rare minerals, construction materials.
- **Spacecraft:** location, cargo capacity, fuel capacity, speed, current fuel, availability, reliability, cost.
- **Mission:** origin, destination, cargo type/amount, deadline, priority, importance, required capabilities.
- **Infrastructure:** cost, resource/population/energy impact, strategic value, construction time.

### Subproblems
1. **Multi-objective routing:** `Cost = w1·Distance + w2·Fuel + w3·Time + w4·Risk`, weights per mission
   (Dijkstra, A*, bidirectional, Pareto/multi-objective, dynamic shortest paths).
2. **Resource allocation:** minimise transport cost + shortage penalty + risk + waste (max-flow, min-cost flow…).
3. **Mission scheduling:** assign ships, departure, route, cargo, priority, delays (greedy, B&B, local search, GA…).
4. **Colony development:** choose facilities under budget (knapsack, facility location, DP, B&B).
5. **Dynamic events:** wormhole collapse, blocked/dangerous routes, ship loss, emergencies, production drops,
   new colonies… → **incremental re-planning** (only recompute what became invalid).
6. **Prediction:** e.g. food 10,000, net −400/day → shortage in 25 days → schedule delivery proactively.
7. **Uncertainty:** variable travel times, failure probabilities.

### Hard requirements (selection)
- ≥ 3 fundamentally different algorithmic techniques; ≥ 1 designed or significantly modified by the team.
- Own implementations (no "just call a solver"); search-space reduction (pruning, memoization, dominance,
  beam, bounds…); solution within a time/memory budget.
- Complexity (best/average/worst, space) + measured performance; correctness arguments; identify NP-hard parts.
- Datasets: small (100 planets/500 routes/50 missions), medium (1k/10k/500), large (10k/100k/5k),
  extreme (100k+/1M+/50k+). Final evaluation on a hidden galaxy, score ≈ αQ − βT − γM − δR.

### Output
Plan, ship assignments, allocation plan, mission schedule, routes, construction decisions, predicted shortages,
re-planning decisions, civilization score, detailed statistics (nodes/states explored, % search space reduced,
events handled, average re-planning time, total time, peak memory…).

### Deliverables
Modular source code with docs and tests; **technical report as the GitHub README**; experimental evaluation.

### VSI starter
`src/generator.py` builds random galaxies (planets, routes, ships, missions, events) at the four required sizes.

---

## Requirements checklist (docs/REQUIREMENTS.md)

## Requirements checklist

### Model & data
- [ ] Galaxy graph with all route / planet / ship / mission / infrastructure attributes
- [ ] Dataset generator: small, medium, large, extreme <!-- auto:data -->
- [ ] Dynamic event stream

### Algorithms (≥ 3 different techniques, ≥ 1 own design)
- [ ] Multi-objective route planning (Dijkstra / A* / Pareto)
- [ ] Resource allocation (min-cost flow or alternative)
- [ ] Mission scheduling (greedy / local search / GA / B&B)
- [ ] Infrastructure selection under budget (knapsack / DP / B&B)
- [ ] Incremental dynamic re-planning (only affected decisions)
- [ ] Shortage prediction + proactive scheduling
- [ ] Uncertainty handling (risk / failure probability / variable times)
- [ ] Search-space reduction (pruning, dominance, memoization, beam…)
- [ ] Algorithm designed or significantly modified by us (DECISIONS.md)
- [ ] (Advanced) Meta-optimisation layer choosing algorithms
- [ ] (Advanced) Hybrid pipeline compared experimentally

### Analysis
- [ ] Formal problem definition + mathematical formulation + scoring function with justified weights
- [ ] Pseudocode, correctness arguments, complexity (best/avg/worst, space) per algorithm
- [ ] NP-hard components identified and justified heuristics

### Experiments
- [ ] All required statistics reported (score, deliveries, shortages, states explored, re-planning time, memory…)
- [ ] Scalability across all dataset sizes
- [ ] Algorithm comparison, worst-case behaviour, pruning effectiveness
- [ ] Respects time/memory budget

### Delivery
- [ ] Technical report in GitHub README (all sections)
- [ ] Build/run instructions and tests
- [ ] Defense preparation
