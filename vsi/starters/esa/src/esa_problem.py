"""Load the official ESA problem (UDP) for this challenge.

Setup (once):
  1. Open the challenge page (docs/PROBLEM.md -> Source) and find its GitHub repository and data files.
  2. Clone the repo next to this project, e.g.  git clone <official repo> official
  3. Set UDP_FILE and UDP_CLASS below to the Python file / class that defines the problem.
     Most SpOC UDPs offer: fitness(x), get_bounds(), get_nobj(), get_nix(), pretty(x), plot(x), example().
  4. Some UDPs need a data file in their constructor: set UDP_ARGS.

Then `python tasks.py run` runs the baseline against the official fitness function.
"""

from __future__ import annotations

from pathlib import Path

from vsi.esa import load_module

ROOT = Path(__file__).resolve().parent.parent

CHALLENGE = "{slug_esa}"          # id used in submission files
PROBLEM_IDS = []                  # TODO: e.g. ["easy", "medium", "hard"] — see the challenge page
UDP_FILE = ROOT / "official" / "TODO_path_to_udp.py"
UDP_CLASS = "TODO_ClassName"
UDP_ARGS: dict = {}


def load_udp(problem_id: str | None = None):
    if not UDP_FILE.exists():
        raise SystemExit(f"Official UDP not found at {UDP_FILE}. Follow the setup steps in src/esa_problem.py.")
    module = load_module(UDP_FILE)
    return getattr(module, UDP_CLASS)(**UDP_ARGS)
