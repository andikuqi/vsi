# VSI

**Ready-made setup for Algorithm Design & Analysis projects. Your AI does the work around your algorithm.**
**Gati për projektet e Dizajnimit dhe Analizës së Algoritmeve. AI-ja jote bën punën rreth algoritmit tënd.**

Works on / Punon në: **Windows · macOS · Linux** — Python 3.10+

---

## SQ · Si ta përdorësh

**A) Me agjent në VS Code** (Codex, Copilot, Gemini, Claude Code, Cursor…)

1. Lart në këtë faqe kliko **Code → Download ZIP** dhe hape ZIP-in.
2. Kopjo folderin **`vsi`** dhe skedarin **`AGENTS.md`** brenda projektit tënd.
3. Hape projektin në VS Code dhe shkruaji agjentit:

> Lexo vsi dhe fillo projektin tim: **[emri i projektit tënd]**

Kaq. Agjenti e gjen projektin, krijon skedarët, shkarkon të dhënat, teston, bën grafikët e parë, e nis raportin dhe të tregon progresin dhe hapin tjetër.

**B) Me ChatGPT, Gemini ose Claude në web / aplikacion** (pa qasje në skedarët e tu)

1. Hap folderin **[`chat/`](chat/)** dhe shkarko skedarin e projektit tënd (p.sh. `traffic-flow-optimization.md`).
2. Ngarkoje në chat dhe shkruaj:

> Lexo këtë skedar dhe më udhëhiq hap pas hapi.

AI-ja të tregon saktë cilat komanda t'i kopjosh në terminal dhe pret përgjigjen tënde. Çdo herë që vazhdon punën: `python tasks.py context` dhe ngarko `CONTEXT.md` në chat.

---

## EN · How to use it

**A) With an agent in VS Code** (Codex, Copilot, Gemini, Claude Code, Cursor…)

1. At the top of this page click **Code → Download ZIP** and unzip it.
2. Copy the **`vsi`** folder and the **`AGENTS.md`** file into your project.
3. Open your project in VS Code and tell your agent:

> Read vsi and start my project: **[your project name]**

That's it. The agent finds your project, creates the files, downloads the data, runs the tests, makes the first charts, starts your report and shows your progress and the next step.

**B) With ChatGPT, Gemini or Claude in the browser / app** (no access to your files)

1. Open the **[`chat/`](chat/)** folder and download your project's file (e.g. `traffic-flow-optimization.md`).
2. Upload it to the chat and write:

> Read this file and guide me step by step.

The AI gives you the exact commands to paste in a terminal and waits for your output. Each time you continue: `python tasks.py context` and upload `CONTEXT.md` to the chat.

---

## 💻 Windows · macOS · Linux

| | Windows | macOS / Linux |
|---|---|---|
| Command / Komanda | `python` | `python3` |
| Example / Shembull | `python tasks.py start` | `python3 tasks.py start` |
| Python missing / Mungon Python | [python.org](https://www.python.org/downloads/) (tick "Add to PATH") | macOS: [python.org](https://www.python.org/downloads/) · Ubuntu/Debian: `sudo apt install python3 python3-venv` |

If your system Python blocks installs (Ubuntu, Debian, Homebrew), `start` creates a `.venv` in the project by itself.
Nëse Python-i i sistemit nuk lejon instalime, `start` krijon vetë një `.venv` në projekt.

---

## 📚 Projects / Projektet

Click a name for its chat pack / Kliko emrin për skedarin e chat-it.

| ESA challenges / Sfidat ESA | | Professor briefs / Detyrat e profesorit | |
|---|:-:|---|:-:|
| [Torso Decompositions](chat/torso-decompositions.md) | ✅ | [DNA Genome Reconstruction](chat/dna-genome-reconstruction.md) | ✅ |
| [Interferometric Mission](chat/interferometric-mission.md) | ✅ | [Protein Structure Prediction](chat/protein-structure-prediction.md) | ✅ |
| [Programmable Cubes](chat/programmable-cubes.md) | ✅ | [Chronos Nexus](chat/chronos-nexus.md) | ✅ |
| [Luna Tomato Logistics](chat/luna-tomato-logistics.md) | ✅ | [Multi-Robot Coordination](chat/multi-robot-coordination.md) | ✅ |
| [Luna Tomato Advertising](chat/luna-tomato-advertising.md) | ✅ | [Time Travel Paradox](chat/time-travel-paradox.md) | ✅ |
| [Keplerian Tomato Traveling Salesperson](chat/keplerian-tomato-tsp.md) | ✅ | [Traffic Flow (Dijkstra & A*)](chat/traffic-flow-optimization.md) | ✅ |
| [Morphing Rovers](chat/morphing-rovers.md) | ✅ | [The Trigger Arc TSP](chat/trigger-arc-tsp.md) | ⚠️ |
| [Quantum Communications Constellations](chat/quantum-communications-constellations.md) | ✅ | | |
| [Trappist Tour](chat/trappist-tour.md) | ✅ | | |
| [Delivery Scheduling](chat/delivery-scheduling.md) | ✅ | | |
| [Mining](chat/mining.md) | ✅ | | |

---

## 🗂️ Your project after setup / Projekti yt pas përgatitjes

```
your-project/
├── vsi/               📦 the folder you copied (don't edit) / folderi që kopjove (mos e ndrysho)
├── AGENTS.md          🤖 instructions for your AI agent / udhëzime për agjentin
├── docs/
│   ├── PROBLEM.md     📄 the problem / problemi
│   ├── REQUIREMENTS.md ☑️ checklist / lista e kërkesave
│   ├── DIAGRAMS.md    🧭 ready diagrams: pipeline, problem, algorithms / diagrame gati
│   ├── diagrams/      🖼️ the same as pictures + your instance / si figura + instanca jote
│   └── PLAN.md  DECISIONS.md
├── src/
│   ├── algorithms.py  ✍️ YOUR ALGORITHMS / ALGORITMET E TUA
│   ├── generator.py   🎲 test data / të dhënat (ESA: esa_problem.py)
│   └── run.py         ▶️ runs everything / ekzekuton gjithçka
├── tests/             🧪 tests / testet
├── data/              🎲 official data (downloaded) / të dhënat zyrtare (të shkarkuara)
├── official/          🛰️ ESA evaluation code (downloaded) / kodi zyrtar i vlerësimit (ESA)
├── results/           📊 tables + charts: scaling, convergence, Pareto / tabela + grafikë
├── vsi.json           🧾 project info + data links / info e projektit + linqet e të dhënave
├── tasks.py           ⚙️ commands (the agent uses them) / komandat (i përdor agjenti)
└── README.md          📝 your report / raporti yt
```

---

## ❓ Good to know / Mirë ta dish

| SQ | EN |
|---|---|
| Skedarët e tu nuk fshihen dhe nuk ndryshohen. | Your own files are never deleted or changed. |
| Mos e ndrysho folderin `vsi`. | Don't edit the `vsi` folder. |
| Ke tashmë `AGENTS.md`? Mos e zëvendëso: VSI i shton udhëzimet e veta në fund të tij. | Already have an `AGENTS.md`? Keep yours: VSI adds its instructions at the end. |
| VSI të jep bazën, jo zgjidhjen. Algoritmin e bën ti, dhe duhet ta kuptosh. | VSI gives you the base, not the solution. The algorithm is yours, and you must understand it. |

| Mark | SQ | EN |
|:-:|---|---|
| ✅ | Problemi është kontrolluar nga burimi zyrtar. Gati për punë. | Problem checked against the official source. Ready to work. |
| ⚠️ | Problemi nuk është kontrolluar ende. Agjenti duhet ta lexojë fillimisht faqen zyrtare (ose pyete profesorin). | Problem not checked yet. Your agent must read the official page first (or ask your professor). |

License: MIT
