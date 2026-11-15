"""Download a project's official data files (listed in vsi.json, written by `vsi new`)."""

from __future__ import annotations

import json
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


def missing(root: str | Path = ".") -> list[Path]:
    return [local_path(e, root) for e in manifest(root).get("data", []) if not local_path(e, root).exists()]


def download(root: str | Path = ".", timeout: float = 60) -> list[Path]:
    """Download every data file that is not there yet. Returns the files that are present afterwards."""
    present = []
    for entry in manifest(root).get("data", []):
        url = entry if isinstance(entry, str) else entry["url"]
        dest = local_path(entry, root)
        if not dest.exists():
            dest.parent.mkdir(parents=True, exist_ok=True)
            tmp = dest.with_suffix(dest.suffix + ".part")
            print(f"downloading {url}")
            with urllib.request.urlopen(url, timeout=timeout) as response, tmp.open("wb") as out:
                shutil.copyfileobj(response, out)
            tmp.replace(dest)
        present.append(dest)
    return present
