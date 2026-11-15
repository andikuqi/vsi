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


@pytest.mark.parametrize("p", [p for p in catalog.load() if p["kind"] == "esa"], ids=lambda p: p["slug"])
def test_esa_projects_are_verified_and_wired(p, tmp_path):
    assert p["verified"] and p["challenge_id"] and p["problem_ids"]
    target = catalog.scaffold(p["slug"], tmp_path / p["slug"])
    src = (target / "src" / "esa_problem.py").read_text(encoding="utf-8")
    assert f'CHALLENGE = "{p["challenge_id"]}"' in src
    assert all(f'"{pid}"' in src for pid in p["problem_ids"])
    assert "TODO (first task)" not in (target / "docs" / "PROBLEM.md").read_text(encoding="utf-8")


@pytest.mark.parametrize("slug", [p["slug"] for p in catalog.load()])
def test_start_runs_on_every_project(slug, tmp_path):
    """`tasks.py start` end to end, offline: official data / evaluation-code URLs are swapped for local fakes
    (a tiny UDP with the official interface), and no packages are installed."""
    import json
    target = catalog.scaffold(slug, tmp_path / slug)
    man_path = target / "vsi.json"
    man = json.loads(man_path.read_text(encoding="utf-8"))
    fake = tmp_path / "fake_data.txt"
    fake.write_text("1 1 1 1.0\n", encoding="utf-8")
    fake_udp = tmp_path / "fake_udp.py"
    fake_udp.write_text("class P:\n    def fitness(self, x):\n        return [sum(x), -sum(x)]\n"
                        "    def get_nobj(self):\n        return 2\n"
                        "    def get_bounds(self):\n        return ([0.0] * 3, [1.0] * 3)\nudp = P()\n", encoding="utf-8")
    man["data"] = [{"url": fake.as_uri(), "file": f"file{i}.txt"} for i, _ in enumerate(man.get("data", []))]
    man["udp"] = {pid: fake_udp.as_uri() for pid in man.get("udp", {})}
    man["requires"] = []
    man_path.write_text(json.dumps(man), encoding="utf-8")

    res = subprocess.run([sys.executable, "tasks.py", "start"], cwd=target, capture_output=True, text=True,
                         encoding="utf-8")
    out = res.stdout + res.stderr
    assert res.returncode == 0, out
    assert "⚠" not in out, out
    assert "Progress / Progresi:" in out and "Next step" in out
    readme = (target / "README.md").read_text(encoding="utf-8")
    assert "_Run `python tasks.py start` to fill this in._" not in readme
    req = (target / "docs" / "REQUIREMENTS.md").read_text(encoding="utf-8")
    if man["data"]:
        assert all((target / "data" / f"file{i}.txt").exists() for i in range(len(man["data"])))
    # every "data" requirement VSI can verify is ticked (downloaded files / working generator)
    assert not any(line.startswith("- [ ]") and "auto:data" in line for line in req.splitlines()), req
    figures = {p.name for p in (target / "docs" / "figures").glob("*.png")}
    assert "scaling_evaluated.png" in figures, (figures, out)
    if p_kind(slug) == "esa":
        assert "OFFICIAL fitness on" in out, out
        assert all((target / "official" / f"{pid}.py").exists() for pid in man["problem_ids"])
        assert any(f.startswith("front_") for f in figures), figures          # 2 objectives -> Pareto chart
        assert "auto:baseline" not in req or not any(
            line.startswith("- [ ]") and "auto:baseline" in line for line in req.splitlines()), req


def p_kind(slug):
    return catalog.get(slug)["kind"]


def test_auto_tick_only_touches_tagged_lines(tmp_path):
    from vsi import progress
    req = tmp_path / "REQUIREMENTS.md"
    req.write_text("- [ ] Data <!-- auto:data -->\n- [ ] Baseline <!-- auto:baseline -->\n- [ ] My algorithm\n",
                   encoding="utf-8")
    assert progress.auto_tick(req, {"data", "unrelated"}) == ["Data"]
    assert req.read_text(encoding="utf-8").splitlines() == [
        "- [x] Data <!-- auto:data -->", "- [ ] Baseline <!-- auto:baseline -->", "- [ ] My algorithm"]
    assert progress.summary(req) == (1, 3, "Baseline")


def test_report_goes_to_docs_when_readme_is_the_students(tmp_path):
    from vsi import report
    (tmp_path / "README.md").write_text("my own readme", encoding="utf-8")
    (tmp_path / "docs").mkdir()
    (tmp_path / "docs" / "REQUIREMENTS.md").write_text("- [x] a\n- [ ] b\n", encoding="utf-8")
    (tmp_path / "results").mkdir()
    (tmp_path / "results" / "metrics.csv").write_text("instance,algorithm,seconds\nsmall,greedy,0.5\n", encoding="utf-8")
    out = report.update(tmp_path)
    assert out == tmp_path / "docs" / "REPORT.md"
    text = out.read_text(encoding="utf-8")
    assert "| small | greedy | 0.5 |" in text and "Next step / Hapi i radhës:** b" in text
    assert (tmp_path / "README.md").read_text(encoding="utf-8") == "my own readme"
    report.update(tmp_path)  # running twice keeps one copy of each block
    assert out.read_text(encoding="utf-8").count("vsi:results:start") == 1


def test_bootstrap_agents_file_is_replaced_but_students_files_are_kept(tmp_path):
    from pathlib import Path
    bootstrap = (Path(catalog.PKG).parent / "AGENTS.md").read_text(encoding="utf-8")
    (tmp_path / "AGENTS.md").write_text(bootstrap, encoding="utf-8")
    (tmp_path / "CLAUDE.md").write_text("# my own notes\n", encoding="utf-8")
    catalog.scaffold("traffic-flow-optimization", tmp_path, force=True)
    agents = (tmp_path / "AGENTS.md").read_text(encoding="utf-8")
    assert "vsi:bootstrap" not in agents and "Traffic Flow" in agents
    claude = (tmp_path / "CLAUDE.md").read_text(encoding="utf-8")
    assert claude.startswith("# my own notes") and "@AGENTS.md" in claude
    catalog.scaffold("traffic-flow-optimization", tmp_path, force=True)    # second run: block refreshed, not duplicated
    assert (tmp_path / "CLAUDE.md").read_text(encoding="utf-8").count("vsi:agents:start") == 1


def test_experiment_writes_convergence_and_fronts(tmp_path, monkeypatch):
    import json
    from vsi import plots
    from vsi.experiment import run_experiments
    monkeypatch.chdir(tmp_path)

    def algo(inst, meter):
        for v in (5, 3, 1):
            meter.count()
            meter.record(v)
        return v

    run_experiments({"a": algo}, {"small": 1, "large": 2},
                    lambda name, inst, res: {"cost": res, "_front": [[1, 3], [2, 1]]})
    assert (tmp_path / "results" / "history.csv").exists()
    assert "small/a" in json.loads((tmp_path / "results" / "fronts.json").read_text())
    names = {p.name for p in plots.main()}
    assert {"scaling_evaluated.png", "quality_cost.png", "convergence_small.png", "front_large.png"} <= names
