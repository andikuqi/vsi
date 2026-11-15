import subprocess
import sys

import pytest

from vsi import catalog


def test_catalog_has_all_projects_with_unique_slugs():
    projects = catalog.load()
    slugs = [p["slug"] for p in projects]
    assert len(projects) == 18
    assert len(set(slugs)) == len(slugs)


@pytest.mark.parametrize("query,slug", [
    ("Torso Decompositions", "torso-decompositions"),
    ("dna assembly", "dna-genome-reconstruction"),
    ("protein folding", "protein-structure-prediction"),
    ("Keplerian Tomato Traveling Salesperson", "keplerian-tomato-tsp"),
    ("time travel", "time-travel-paradox"),
    ("dijkstra traffic", "traffic-flow-optimization"),
])
def test_find(query, slug):
    assert catalog.find(query)[0][1]["slug"] == slug


@pytest.mark.parametrize("slug", [p["slug"] for p in catalog.load()])
def test_scaffold_every_project_and_its_tests_pass(slug, tmp_path):
    target = catalog.scaffold(slug, tmp_path / slug)
    for f in ["AGENTS.md", "GEMINI.md", "CLAUDE.md", ".github/copilot-instructions.md", ".cursor/rules/vsi.mdc",
              "tasks.py", "docs/PROBLEM.md", "docs/REQUIREMENTS.md", "docs/PROMPTS.md", "src/run.py", "README.md"]:
        assert (target / f).exists(), f
    assert "[[" not in (target / "AGENTS.md").read_text(encoding="utf-8")
    result = subprocess.run([sys.executable, "-m", "pytest", "-q"], cwd=target, capture_output=True, text=True)
    assert result.returncode == 0, result.stdout + result.stderr


@pytest.mark.parametrize("slug", ["dna-genome-reconstruction", "protein-structure-prediction", "chronos-nexus",
                                  "multi-robot-coordination", "time-travel-paradox", "traffic-flow-optimization"])
def test_generated_projects_run_end_to_end(slug, tmp_path):
    target = catalog.scaffold(slug, tmp_path / slug)
    result = subprocess.run([sys.executable, "tasks.py", "run", "--sizes", "small"], cwd=target,
                            capture_output=True, text=True)
    assert result.returncode == 0, result.stdout + result.stderr
    assert (target / "results" / "metrics.csv").exists()


def test_generated_project_uses_its_own_bundled_vsi(tmp_path):
    target = catalog.scaffold("traffic-flow-optimization", tmp_path / "p")
    assert (target / "vsi" / "__main__.py").exists()
    assert (target / "vsi" / "projects" / "index.json").exists()
    assert not list((target / "vsi").rglob("__pycache__"))
    found = subprocess.run([sys.executable, "-c", "import vsi; print(vsi.__file__)"], cwd=target,
                           capture_output=True, text=True).stdout
    assert str(target.resolve()) in found


def test_copied_folder_runs_without_install(tmp_path):
    import shutil
    shutil.copytree(catalog.PKG, tmp_path / "vsi", ignore=shutil.ignore_patterns("__pycache__"))
    run = lambda *a: subprocess.run([sys.executable, "-m", "vsi", *a], cwd=tmp_path, capture_output=True, text=True)
    assert "time-travel-paradox" in run("find", "time", "travel").stdout
    assert run("new", "time-travel-paradox", ".", "--force").returncode == 0
    assert (tmp_path / "tasks.py").exists() and (tmp_path / "vsi" / "measure.py").exists()


def test_force_keeps_the_students_existing_files(tmp_path):
    (tmp_path / "README.md").write_text("my own readme", encoding="utf-8")
    (tmp_path / ".gitignore").write_text("secret.txt", encoding="utf-8")
    catalog.scaffold("dna-genome-reconstruction", tmp_path, force=True)
    assert (tmp_path / "README.md").read_text(encoding="utf-8") == "my own readme"
    assert (tmp_path / ".gitignore").read_text(encoding="utf-8") == "secret.txt"
    assert (tmp_path / "tasks.py").exists() and (tmp_path / "AGENTS.md").exists()
