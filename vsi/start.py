"""`python tasks.py start`: take a fresh project as far as VSI can, in one command.

Steps: packages -> data -> tests -> first run -> charts -> requirement ticks -> report -> progress + next step.
Every step reports ✅ done, ⏭ skipped (with the reason) or ⚠️ problem, and never stops the others.
"""

from __future__ import annotations

import importlib
import importlib.util
import subprocess
import sys
from pathlib import Path

from . import data, progress, report

OK, SKIP, WARN = "✅", "⏭ ", "⚠️ "


def _say(icon: str, label: str, detail: str = "") -> None:
    print(f"{icon} {label:<31} {detail}")


def _packages(root: Path) -> None:
    missing = [m for m in ("pytest", "matplotlib") if importlib.util.find_spec(m) is None]
    if not missing:
        _say(OK, "Packages / Paketat", "pytest, matplotlib")
        return
    code = subprocess.call([sys.executable, "-m", "pip", "install", "-q", "-r", str(root / "requirements.txt")])
    importlib.invalidate_caches()
    _say(OK if code == 0 else WARN, "Packages / Paketat", "installed" if code == 0 else "pip install failed — run `python tasks.py setup`")


def _data(root: Path, man: dict) -> None:
    if man.get("data"):
        try:
            files = data.download(root)
            _say(OK, "Data / Të dhënat", f"{len(files)} official file(s) in data/")
        except Exception as exc:  # network problems must not stop the rest
            _say(WARN, "Data / Të dhënat", f"download failed ({exc}); retry with `python tasks.py data`")
    elif man.get("kind") == "esa":
        _say(SKIP, "Data / Të dhënat", "no direct download: data comes with the official repo (docs/PROBLEM.md)")
    elif "data" in progress.facts(root):
        _say(OK, "Data / Të dhënat", "instance generator works (src/generator.py)")
    else:
        _say(WARN, "Data / Të dhënat", "src/generator.py does not produce an instance yet")


def _tests(root: Path) -> None:
    if importlib.util.find_spec("pytest") is None:
        _say(SKIP, "Tests / Testet", "pytest not installed")
        return
    res = subprocess.run([sys.executable, "-m", "pytest", "-q"], cwd=root, capture_output=True, text=True)
    last = (res.stdout.strip().splitlines() or ["no output"])[-1]
    _say(OK if res.returncode == 0 else WARN, "Tests / Testet", last)


def _first_run(root: Path, man: dict) -> None:
    try:
        if man.get("kind") == "esa":
            esa_problem = importlib.import_module("esa_problem")
            if not esa_problem.UDP_FILE.exists():
                _say(SKIP, "First run / Ekzekutimi i parë",
                     "needs the official UDP: set it up in src/esa_problem.py (your agent can do it)")
                return
            importlib.import_module("run").main(["--budget", "2"])
            _say(OK, "First run / Ekzekutimi i parë", "random-search baseline with the official fitness")
        else:
            gen = importlib.import_module("generator")
            importlib.import_module("run").main(["--sizes", next(iter(gen.SIZES))])
            _say(OK, "First run / Ekzekutimi i parë",
                 "pipeline works (src/algorithms.py `baseline` is still a placeholder — your first algorithm goes there)")
    except SystemExit as exc:
        _say(WARN, "First run / Ekzekutimi i parë", str(exc))
    except Exception as exc:
        _say(WARN, "First run / Ekzekutimi i parë", f"{type(exc).__name__}: {exc}")


def _charts(root: Path) -> None:
    if not (root / "results" / "metrics.csv").exists():
        _say(SKIP, "Charts / Grafikët", "no results yet")
        return
    try:
        import contextlib
        import io

        from . import plots
        with contextlib.redirect_stdout(io.StringIO()):
            plots.main()
        n = len(list((root / "results").glob("*.png")))
        _say(OK, "Charts / Grafikët", f"{n} chart(s) -> docs/figures/")
    except Exception as exc:
        _say(WARN, "Charts / Grafikët", f"{type(exc).__name__}: {exc}")


def main(root: str | Path = ".") -> int:
    root = Path(root).resolve()
    man = data.manifest(root)
    print(f"\nVSI start — {man.get('title', root.name)}\n")
    _packages(root)
    _data(root, man)
    _tests(root)
    _first_run(root, man)
    _charts(root)

    req = root / "docs" / "REQUIREMENTS.md"
    if req.exists():
        ticked = progress.auto_tick(req, progress.facts(root))
        _say(OK, "Requirements / Kërkesat", f"{len(ticked)} ticked automatically" if ticked else "nothing new to tick")
    written = report.update(root)
    _say(OK, "Report / Raporti", f"{written.relative_to(root)} (status + results)")

    if req.exists():
        done, total, nxt = progress.summary(req)
        print(f"\nProgress / Progresi: {progress.bar(done, total)}")
        if nxt:
            print(f"Next step / Hapi i radhës: {nxt}")
            print(f'Tell your agent / Thuaji agjentit: "Do the next step: {nxt}. Explain it to me simply."')
    return 0
