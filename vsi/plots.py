"""Charts from results/metrics.csv and results/fronts.json."""

from __future__ import annotations

import csv
import json
from collections import defaultdict
from pathlib import Path

import matplotlib

matplotlib.use("Agg")  # no window needed, just save PNGs
import matplotlib.pyplot as plt

RESULTS = Path("results")


def metric_bars(metric: str, csv_path: Path = RESULTS / "metrics.csv") -> Path:
    """Grouped bar chart of one metric (e.g. seconds, peak_mb, hypervolume) per instance/algorithm."""
    rows = list(csv.DictReader(csv_path.open()))
    instances = list(dict.fromkeys(r["instance"] for r in rows))
    algos = list(dict.fromkeys(r["algorithm"] for r in rows))
    width = 0.8 / max(len(algos), 1)
    fig, ax = plt.subplots(figsize=(7, 4))
    for i, algo in enumerate(algos):
        vals = [float(next((r[metric] for r in rows if r["instance"] == inst and r["algorithm"] == algo), 0))
                for inst in instances]
        ax.bar([x + i * width for x in range(len(instances))], vals, width, label=algo)
    ax.set_xticks([x + width * (len(algos) - 1) / 2 for x in range(len(instances))], instances)
    ax.set_ylabel(metric)
    ax.set_title(f"{metric} by instance and algorithm")
    ax.legend()
    out = RESULTS / f"{metric}.png"
    fig.tight_layout()
    fig.savefig(out, dpi=150)
    plt.close(fig)
    return out


def pareto_fronts(json_path: Path = RESULTS / "fronts.json", x: str = "f1", y: str = "f2") -> list[Path]:
    """One plot per instance, one staircase per algorithm.

    results/fronts.json format: {"<instance>/<algorithm>": [{"f1": ..., "f2": ...}, ...], ...}
    (pass x/y to use other key names). Both objectives are shown as stored.
    """
    fronts = json.loads(json_path.read_text())
    by_instance = defaultdict(dict)
    for key, points in fronts.items():
        inst, algo = key.split("/", 1)
        by_instance[inst][algo] = points
    outs = []
    for inst, algos in by_instance.items():
        fig, ax = plt.subplots(figsize=(6, 4))
        for algo, pts in algos.items():
            pts = sorted(pts, key=lambda p: p[x])
            ax.step([p[x] for p in pts], [p[y] for p in pts], where="post", marker="o", label=algo)
        ax.set_xlabel(x)
        ax.set_ylabel(y)
        ax.set_title(f"Pareto fronts — {inst}")
        ax.legend()
        out = RESULTS / f"front_{inst}.png"
        fig.tight_layout()
        fig.savefig(out, dpi=150)
        plt.close(fig)
        outs.append(out)
    return outs


def numeric_metrics(csv_path: Path = RESULTS / "metrics.csv") -> list[str]:
    """Columns of metrics.csv that contain numbers in every row and are not all zero (nothing to chart)."""
    rows = list(csv.DictReader(csv_path.open()))
    out = []
    for col in rows[0] if rows else []:
        if col in ("instance", "algorithm"):
            continue
        try:
            values = [float(r[col]) for r in rows]
            if any(values):
                out.append(col)
        except (TypeError, ValueError):
            pass
    return out


def main() -> None:
    """Chart every numeric metric, plus Pareto fronts if results/fronts.json exists."""
    csv_path = RESULTS / "metrics.csv"
    if not csv_path.exists():
        raise SystemExit("results/metrics.csv not found — run `python tasks.py run` first.")
    for m in numeric_metrics(csv_path):
        print(metric_bars(m, csv_path))
    if (RESULTS / "fronts.json").exists():
        for p in pareto_fronts():
            print(p)


if __name__ == "__main__":
    main()
