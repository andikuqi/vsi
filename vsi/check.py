"""Progress report from docs/REQUIREMENTS.md checkboxes."""

from __future__ import annotations

import re
from pathlib import Path


def check(path: str | Path = "docs/REQUIREMENTS.md") -> int:
    done, todo = [], []
    for line in Path(path).read_text(encoding="utf-8").splitlines():
        m = re.match(r"\s*- \[( |x|X)\] (.+)", line)
        if m:
            (done if m.group(1).lower() == "x" else todo).append(m.group(2))
    total = len(done) + len(todo)
    print(f"{len(done)}/{total} requirements done ({100 * len(done) // max(total, 1)}%)")
    for item in todo:
        print(f"  [ ] {item}")
    return len(todo)


if __name__ == "__main__":
    check()
