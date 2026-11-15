# Requirements checklist

Tick a box (`[x]`) only when it is done **and** verified. `python tasks.py check` reads this file.

## Problem & data
- [x] Problem formally defined (docs/PROBLEM.md)
- [ ] Graphs downloaded and loaded (easy, medium, hard)
- [x] Reference evaluator implemented and tested against the official example

## Algorithms
- [x] Baseline algorithm (random / identity ordering)
- [ ] Greedy constructive heuristic (e.g. min-degree or min-fill ordering)
- [ ] Improvement method (local search / simulated annealing / tabu)
- [ ] Multi-objective method producing several trade-offs (e.g. sweep of t, evolutionary / NSGA-style)
- [ ] At least one idea designed or modified by us (documented in DECISIONS.md)

## Analysis
- [ ] Pseudocode for every algorithm (README)
- [ ] Time & space complexity for every algorithm (README)
- [ ] Explanation why the problem is NP-hard / why heuristics are used

## Experiments
- [ ] Metrics recorded: runtime, peak memory, solutions evaluated
- [ ] Results on all three graphs
- [ ] Pareto front plot per graph + hypervolume
- [ ] Algorithm comparison table
- [ ] Scaling discussion (theory vs measured)

## Delivery
- [ ] Submission JSON for each problem, verified with the official scorer
- [ ] README report complete (all sections filled)
- [ ] Defense preparation: can explain every algorithm and design decision
