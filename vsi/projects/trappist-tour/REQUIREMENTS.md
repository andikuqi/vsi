# Requirements checklist

Tick a box (`[x]`) only when it is done **and** verified. `python tasks.py check` reads this file.

## Problem & data
- [x] Problem statement copied from the official page (docs/PROBLEM.md)
- [ ] Official UDP downloaded from the problem page and wired in src/esa_problem.py (pykep installed)
- [ ] udp.example() evaluates; own Pareto filter + hypervolume (ref [2500, 4000]) tested
- [ ] Official example / sample solution evaluates to the expected value (test)

## Algorithms
- [ ] Baseline (random search) runs end to end with the official fitness <!-- auto:baseline -->
- [ ] Order selection (enumerate the 5 040 sequences with a cheap estimate, or a permutation GA)
- [ ] Continuous optimiser for a fixed order (DE / CMA-ES / multi-start local search)
- [ ] Multi-objective method (NSGA-II, or weighted sum / ε-constraint sweep)
- [ ] At least one idea designed or modified by us (documented in DECISIONS.md)
- [ ] Several trade-off solutions per run (Pareto front), hypervolume computed with the official reference point

## Analysis
- [ ] Pseudocode for every algorithm (README)
- [ ] Time & space complexity for every algorithm (README)
- [ ] Why the problem is hard / why heuristics are used

## Experiments
- [ ] Metrics recorded: fitness, runtime, peak memory, fitness evaluations <!-- auto:metrics -->
- [ ] Results on every problem instance
- [ ] Algorithm comparison table
- [ ] Pareto front plot + hypervolume per problem
- [ ] Theory vs measured performance (scaling discussion)

## Delivery
- [ ] Submission JSON per problem, checked with the official fitness function
- [ ] README report complete (all sections filled)
- [ ] Defense preparation: can explain every algorithm and design decision
