"""Your optimisers for the ESA problem. Each one: fn(udp, budget_seconds, meter, rng) -> list of decision vectors.

The baseline samples random vectors inside the UDP bounds. Replace / extend with your own methods
(greedy construction, local search, simulated annealing, genetic algorithm, …) and register them.
"""

from __future__ import annotations

import time


def random_vector(udp, rng):
    lower, upper = udp.get_bounds()
    n_int = udp.get_nix() if hasattr(udp, "get_nix") else 0
    n = len(lower)
    x = []
    for i in range(n):
        if i >= n - n_int:   # pygmo convention: integer variables are the last get_nix() entries
            x.append(rng.randint(int(lower[i]), int(upper[i])))
        else:
            x.append(rng.uniform(lower[i], upper[i]))
    return x


def random_search(udp, budget_seconds, meter, rng):
    best_x, best_f = None, None
    deadline = time.perf_counter() + budget_seconds
    while time.perf_counter() < deadline:
        x = random_vector(udp, rng)
        f = udp.fitness(x)
        meter.count()
        if best_f is None or list(f) < list(best_f):
            best_x, best_f = x, f
    return [best_x] if best_x is not None else []


ALGORITHMS = {
    "random_search": random_search,
}
