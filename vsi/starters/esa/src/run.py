"""Run every optimiser on every problem instance with the official ESA fitness; save metrics + submissions."""

from __future__ import annotations

import argparse
import random

from vsi.esa import write_submission
from vsi.experiment import run_experiments

from algorithms import ALGORITHMS
from esa_problem import CHALLENGE, PROBLEM_IDS, load_udp


def main(argv=None) -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--budget", type=float, default=10.0, help="seconds per optimiser per problem")
    parser.add_argument("--seed", type=int, default=0)
    args = parser.parse_args(argv)

    problems = PROBLEM_IDS or [None]
    instances = {str(p): load_udp(p) for p in problems}

    def wrap(name, algo):
        def run(udp, meter):
            return algo(udp, args.budget, meter, random.Random(args.seed))
        return run

    def score(inst_name, udp, vectors):
        if not vectors:
            return {"fitness": None}
        fits = [list(udp.fitness(x)) for x in vectors]
        if inst_name != "None":
            write_submission(CHALLENGE, inst_name, vectors[0] if len(vectors) == 1 else vectors,
                             f"results/submission_{inst_name}.json")
        return {"fitness": min(fits)}

    run_experiments({name: wrap(name, algo) for name, algo in ALGORITHMS.items()}, instances, score)


if __name__ == "__main__":
    main()
