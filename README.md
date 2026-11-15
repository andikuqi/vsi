# VSI

**Agent-ready scaffolding for Algorithm Design & Analysis projects**
**Infrastrukturë e gatshme për agjentët AI në projektet e Dizajnimit dhe Analizës së Algoritmeve**

> 🇬🇧 Start your project from a working base, not from zero. VSI gives you the problem statement, a requirements checklist, data, measuring, charts, a report template, and instructions for your AI agent. You only write **your algorithm**.
>
> 🇦🇱 Fillo projektin nga një bazë që punon, jo nga zero. VSI të jep përshkrimin e problemit, listën e kërkesave, të dhënat, matjet, grafikët, shabllonin e raportit dhe udhëzimet për agjentin AI. Ti shkruan vetëm **algoritmin tënd**.

---

## 📦 What you get / Çfarë merr

| | English | Shqip |
|---|---|---|
| 📄 | Problem statement + requirements checklist | Përshkrimi i problemit + lista e kërkesave |
| 🎲 | Data generator or official data loader | Gjenerues të dhënash ose ngarkues i të dhënave zyrtare |
| ⏱️ | Measuring: time, memory, explored states, pruning % | Matje: koha, memoria, gjendjet e eksploruara, % e prerjeve |
| 🧪 | Experiments + tests | Eksperimente + teste |
| 📊 | Charts (PNG) ready for the report | Grafikë (PNG) gati për raportin |
| 📝 | README report template | Shabllon raporti në README |
| 🤖 | Instructions for Codex, Copilot, Gemini, Claude, Cursor, ChatGPT | Udhëzime për Codex, Copilot, Gemini, Claude, Cursor, ChatGPT |

---

## 🚀 Install / Instalimi

**Requirements / Kërkesat:** Python 3.10+ and Git / Python 3.10+ dhe Git

| Step / Hapi | Command / Komanda |
|---|---|
| 1. Download / Shkarko | `git clone https://github.com/andikuqi/vsi.git` |
| 2. Install / Instalo | `pip install -e vsi` |
| 3. Check / Kontrollo | `vsi list` |

---

## 🧭 Use / Përdorimi

### 1. Find your project / Gjej projektin tënd

```
vsi find traffic
```

### 2. Create it / Krijoje

| Situation / Situata | Command / Komanda |
|---|---|
| New folder / Folder i ri | `vsi new <slug> my-project` |
| Repo you already have / Repo që e ke tashmë | `cd my-repo` → `vsi new <slug> . --force` |

`<slug>` = project name from the table below / emri i projektit nga tabela më poshtë.

### 3. Work / Puno

```
cd my-project
python tasks.py setup
```

| Command / Komanda | English | Shqip |
|---|---|---|
| `python tasks.py setup` | Create venv + install packages | Krijon venv + instalon paketat |
| `python tasks.py data` | Generate / download data | Gjeneron / shkarkon të dhënat |
| `python tasks.py test` | Run tests | Ekzekuton testet |
| `python tasks.py run` | Run all algorithms → `results/metrics.csv` | Ekzekuton algoritmet → `results/metrics.csv` |
| `python tasks.py plots` | Make charts → `results/*.png` | Krijon grafikët → `results/*.png` |
| `python tasks.py check` | Check what is missing before submitting | Kontrollon çfarë mungon para dorëzimit |
| `python tasks.py context` | Build `CONTEXT.md` for chat AIs | Krijon `CONTEXT.md` për AI në chat |

---

## 🤖 With your AI agent / Me agjentin tënd AI

| Agent | How / Si |
|---|---|
| **Codex, Cursor** | Reads `AGENTS.md` automatically / E lexon `AGENTS.md` vetë |
| **GitHub Copilot** | Reads `.github/copilot-instructions.md` / E lexon vetë |
| **Gemini CLI** | Reads `GEMINI.md` / E lexon vetë |
| **Claude Code** | Reads `CLAUDE.md` / E lexon vetë |
| **ChatGPT, Copilot 365, Gemini web** | Run `python tasks.py context`, upload `CONTEXT.md`, follow `docs/PROMPTS.md` / Ekzekuto `python tasks.py context`, ngarko `CONTEXT.md`, ndiq `docs/PROMPTS.md` |

**Example prompt / Shembull:**
> "Read AGENTS.md and docs/REQUIREMENTS.md. Implement a greedy algorithm in src/algorithms.py, then run `python tasks.py test` and `python tasks.py run`."

---

## 📚 Catalog / Katalogu (18 projects / projekte)

### ESA SpOC challenges / Sfidat ESA SpOC

| Project / Projekti | Slug | Spec |
|---|---|---|
| Torso Decompositions | `torso-decompositions` | ✅ |
| Interferometric Mission | `interferometric-mission` | ⚠️ |
| Programmable Cubes | `programmable-cubes` | ⚠️ |
| Luna Tomato Logistics | `luna-tomato-logistics` | ⚠️ |
| Luna Tomato Advertising | `luna-tomato-advertising` | ⚠️ |
| Keplerian Tomato Traveling Salesperson | `keplerian-tomato-tsp` | ⚠️ |
| Morphing Rovers | `morphing-rovers` | ⚠️ |
| Quantum Communications Constellations | `quantum-communications-constellations` | ⚠️ |
| Trappist Tour | `trappist-tour` | ⚠️ |
| Delivery Scheduling | `delivery-scheduling` | ⚠️ |
| Mining | `mining` | ⚠️ |

### Professor briefs / Detyrat nga profesori

| Project / Projekti | Slug | Starter |
|---|---|---|
| DNA Genome Reconstruction | `dna-genome-reconstruction` | DNA reads generator / gjenerues leximesh |
| Protein Structure Prediction | `protein-structure-prediction` | HP-model sequences / sekuenca |
| Chronos Nexus | `chronos-nexus` | Dynamic galaxy graph / graf galaktik |
| Multi-Robot Coordination | `multi-robot-coordination` | Grid with obstacles / rrjetë me pengesa |
| Time Travel Paradox | `time-travel-paradox` | Event graph with cycles / graf ngjarjesh |
| Traffic Flow (Dijkstra & A*) | `traffic-flow-optimization` | City grid with traffic / rrjet qyteti |
| The Trigger Arc TSP | `trigger-arc-tsp` | Generic / i përgjithshëm |

| Mark | English | Shqip |
|---|---|---|
| ✅ | Spec verified from the official page | Specifikimi u verifikua nga faqja zyrtare |
| ⚠️ | Your agent must copy the real spec from the source page first | Agjenti duhet ta kopjojë specifikimin e vërtetë nga faqja burimore |

---

## 🗂️ Generated project / Projekti që krijohet

```
my-project/
├── AGENTS.md  GEMINI.md  CLAUDE.md      ← AI instructions / udhëzime për AI
├── .github/copilot-instructions.md
├── .cursor/rules/vsi.mdc
├── tasks.py                             ← all commands / të gjitha komandat
├── docs/
│   ├── PROBLEM.md                       ← the problem / problemi
│   ├── REQUIREMENTS.md                  ← checklist / lista e kërkesave
│   ├── PLAN.md  DECISIONS.md  PROMPTS.md
├── src/
│   ├── algorithms.py                    ← YOUR CODE HERE / KODI YT KËTU
│   ├── run.py  generator.py
├── tests/
├── results/                             ← CSV + charts / CSV + grafikë
└── README.md                            ← report template / shabllon raporti
```

---

## 🐍 Library / Libraria

```python
from vsi.measure import Meter               # time, memory, meter.count(), meter.prune()
from vsi.experiment import run_experiments  # algorithms × instances → results/metrics.csv
from vsi.pareto import pareto_filter, hypervolume, select_best
from vsi.esa import load_module, write_submission
```

---

## ⚖️ Fair use / Përdorimi i ndershëm

| English | Shqip |
|---|---|
| VSI gives **infrastructure, not solutions**. You must design, implement and explain your own algorithm. | VSI jep **infrastrukturë, jo zgjidhje**. Algoritmin duhet ta dizajnosh, implementosh dhe shpjegosh vetë. |
| Check your course rules before sharing work. | Kontrollo rregullat e lëndës para se të ndash punën. |

## 🤝 Contribute / Kontribuo

| English | Shqip |
|---|---|
| Add a project: an entry in `vsi/projects/index.json` + a test in `tests/test_catalog.py`. `python -m pytest` must pass. | Shto një projekt: një rresht në `vsi/projects/index.json` + një test në `tests/test_catalog.py`. `python -m pytest` duhet të kalojë. |

License / Licenca: MIT
