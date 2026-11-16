# VSI chat pack — AI-Based Protein Structure Prediction and Optimization

> **For students using ChatGPT, Gemini or Claude in the browser or the app.**
> Upload this file to the chat and write: *"Read this file and guide me step by step."*
> 🇦🇱 Ngarkoje këtë skedar në chat dhe shkruaj: *"Lexo këtë skedar dhe më udhëhiq hap pas hapi."*

Project id (slug): `protein-structure-prediction` · Source: professor brief (see PROBLEM.md)

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
   python -m vsi new protein-structure-prediction . --force
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

## AI-Based Protein Structure Prediction and Optimization

Source: professor's brief (condensed here; keep the original brief next to this file if you have it).

### Goal
Given an amino-acid sequence, find a plausible 2D or 3D structure (lattice positions) that minimises an
energy (or maximises a fitness) function. Exhaustive search is infeasible, so design efficient search.

### Required components
1. Representation: amino acids placed in 2D/3D space; invalid structures (two residues on one cell) are
   detected and rejected.
2. Energy/fitness function, clearly explained, e.g. `E(S) = E_interaction + E_collision + E_structure`
   (attractions, repulsions, collisions, neighbours, compactness).
3. **At least two different search algorithms** (GA, simulated annealing, beam search, A*, branch & bound,
   local search, hybrids), with justification.
4. **At least one search-space reduction** (pruning, bounds, beam width, duplicate elimination, symmetry
   reduction, branch ordering) and its effect on complexity and practice.
5. Local improvement moves that keep validity (rotations, mutations, local moves, segment rearrangement).
6. Time & space complexity analysis; experiments on proteins of different lengths; comparison.

### Input
Sequence (e.g. `ACDEFGHIKLMNPQRSTVWY`), length, energy parameters, time/compute budget, optional constraints.

### Output
Structure, final energy, configurations explored, valid vs invalid configurations, time, memory,
visualisation/text representation, algorithm comparison.

### Metrics
Energy, validity, configurations explored, % search space pruned, time, memory, convergence speed,
scalability with length, solution quality. Graphs and tables vs problem size are required.

### Advanced (optional)
Hybrid pipeline (e.g. GA → beam search → local search/SA) compared experimentally to the single algorithms.

### Important (from the brief)
Using an existing protein-folding library without your own algorithm and analysis does **not** satisfy the project.

### VSI starter
`src/generator.py` creates random sequences and maps them to the HP model (hydrophobic/polar) — a common,
simple energy model you may use or extend.

---

## Requirements checklist (docs/REQUIREMENTS.md)

## Requirements checklist

### Implementation
- [ ] Sequence → lattice representation (2D or 3D) with validity check (no overlaps)
- [ ] Energy / fitness function, documented
- [ ] Algorithm 1 (e.g. genetic algorithm)
- [ ] Algorithm 2 (e.g. simulated annealing / beam search / branch & bound)
- [ ] Search-space reduction technique (pruning / bounds / symmetry / duplicates)
- [ ] Local improvement moves that keep structures valid
- [ ] Structure visualisation (plot or text)
- [ ] At least one idea designed or modified by us (DECISIONS.md)
- [ ] (Optional) Hybrid algorithm compared to the single ones

### Analysis
- [ ] Justification of the chosen algorithms
- [ ] Pseudocode for every algorithm
- [ ] Time & space complexity for every algorithm
- [ ] Effect of the reduction technique on complexity and practice

### Experiments
- [ ] Metrics: energy, explored / valid / invalid configurations, % pruned, time, memory, convergence
- [ ] Proteins of increasing length
- [ ] Algorithm comparison (quality and efficiency), graphs and tables
- [ ] Theory vs measured performance

### Delivery
- [ ] README report complete
- [ ] Defense preparation
