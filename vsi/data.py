"""Download a project's official data files and evaluation code (listed in vsi.json, written by `vsi new`).

data files                                        -> data/<same layout as the official server>
evaluation code (ESA "UDP", one file per problem) -> official/<problem id>.py
"""

from __future__ import annotations

import importlib.util
import json
import re
import shutil
import urllib.request
from pathlib import Path


def manifest(root: str | Path = ".") -> dict:
    """The project's vsi.json (slug, kind, challenge/problem ids, data files)."""
    path = Path(root) / "vsi.json"
    return json.loads(path.read_text(encoding="utf-8")) if path.exists() else {}


def local_path(entry: dict | str, root: str | Path = ".") -> Path:
    """Where a data file goes: data/<path after '/data/' in the URL>, mirroring the official folder layout."""
    if isinstance(entry, str):
        entry = {"url": entry}
    if entry.get("file"):
        rel = entry["file"]
    else:
        url = entry["url"]
        rel = url.split("/data/", 1)[1] if "/data/" in url else url.rstrip("/").rsplit("/", 1)[-1]
    return Path(root) / "data" / rel


def udp_path(problem_id: str, root: str | Path = ".") -> Path:
    """Where the official evaluation code of one problem goes."""
    return Path(root) / "official" / f"{problem_id}.py"


def _targets(root: str | Path) -> list[tuple[str, Path]]:
    man = manifest(root)
    files = [(e if isinstance(e, str) else e["url"], local_path(e, root)) for e in man.get("data", [])]
    files += [(url, udp_path(pid, root)) for pid, url in man.get("udp", {}).items()]
    return files


def missing(root: str | Path = ".") -> list[Path]:
    return [dest for _, dest in _targets(root) if not dest.exists()]


def module_name(requirement: str) -> str:
    """'heyoka==3.2.0' -> 'heyoka', 'pillow' -> 'PIL' (the name to import)."""
    name = re.split(r"[<>=!~ ]", requirement, maxsplit=1)[0].strip()
    return {"pillow": "PIL"}.get(name.lower(), name)


def missing_packages(root: str | Path = ".") -> list[str]:
    """Requirements of the official evaluation code that cannot be imported yet."""
    return [r for r in manifest(root).get("requires", []) if importlib.util.find_spec(module_name(r)) is None]


def download(root: str | Path = ".", timeout: float = 60) -> list[Path]:
    """Download every data / evaluation-code file that is not there yet. Returns the files present afterwards."""
    present = []
    for url, dest in _targets(root):
        if not dest.exists():
            dest.parent.mkdir(parents=True, exist_ok=True)
            tmp = dest.with_suffix(dest.suffix + ".part")
            print(f"downloading {url}")
            with urllib.request.urlopen(url, timeout=timeout) as response, tmp.open("wb") as out:
                shutil.copyfileobj(response, out)
            tmp.replace(dest)
        present.append(dest)
    return present
