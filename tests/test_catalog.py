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
