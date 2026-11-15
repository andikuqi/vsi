"""Run every algorithm on every instance, measure it, and save a metrics table.

Generic: `algorithms` maps name -> fn(instance, meter) -> result, and `score` turns a result into a
dict of quality numbers. Writes results/metrics.csv and returns the rows.
"""

from __future__ import annotations

import csv
from pathlib import Path
from typing import Callable

from .measure import Meter


def run_experiments(
    algorithms: dict[str, Callable],
    instances: dict[str, object],
    score: Callable[[str, object, object], dict],
    out_csv: str | Path = "results/metrics.csv",
) -> list[dict]:
    rows = []
    for inst_name, instance in instances.items():
        for algo_name, algo in algorithms.items():
            with Meter() as meter:
                result = algo(instance, meter)
            row = {"instance": inst_name, "algorithm": algo_name, **meter.report(),
                   **score(inst_name, instance, result)}
            rows.append(row)
            print(row)
    out = Path(out_csv)
    out.parent.mkdir(parents=True, exist_ok=True)
    if rows:
        fields = list(dict.fromkeys(k for r in rows for k in r))
        with out.open("w", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=fields)
            writer.writeheader()
            writer.writerows(rows)
    return rows
