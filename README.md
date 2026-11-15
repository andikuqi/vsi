# VSI

**Ready-made setup for Algorithm Design & Analysis projects. Your AI agent does the work.**
**Gati për projektet e Dizajnimit dhe Analizës së Algoritmeve. Agjenti yt AI e bën punën.**

---

## 🇦🇱 Si ta përdorësh

1. Lart në këtë faqe kliko **Code → Download ZIP** dhe hape ZIP-in.
2. Kopjo folderin **`vsi`** dhe skedarin **`AGENTS.md`** brenda projektit tënd.
3. Hape projektin në VS Code dhe shkruaji agjentit tënd (Codex, Copilot, Gemini, Claude, Cursor…):

> Lexo vsi dhe fillo projektin tim: **[emri i projektit tënd]**

Kaq. Agjenti e gjen projektin, krijon skedarët, shkarkon të dhënat, teston, bën grafikët e parë, e nis raportin dhe të tregon progresin dhe hapin tjetër.

---

## 🇬🇧 How to use it

1. At the top of this page click **Code → Download ZIP** and unzip it.
2. Copy the **`vsi`** folder and the **`AGENTS.md`** file into your project.
3. Open your project in VS Code and tell your AI agent (Codex, Copilot, Gemini, Claude, Cursor…):

> Read vsi and start my project: **[your project name]**

That's it. The agent finds your project, creates the files, downloads the data, runs the tests, makes the first charts, starts your report and shows your progress and the next step.

---

## 📚 Projects / Projektet

| ESA challenges / Sfidat ESA | | Professor briefs / Detyrat e profesorit | |
|---|:-:|---|:-:|
| Torso Decompositions | ✅ | DNA Genome Reconstruction | ✅ |
| Interferometric Mission | ✅ | Protein Structure Prediction | ✅ |
| Programmable Cubes | ✅ | Chronos Nexus | ✅ |
| Luna Tomato Logistics | ✅ | Multi-Robot Coordination | ✅ |
| Luna Tomato Advertising | ✅ | Time Travel Paradox | ✅ |
| Keplerian Tomato Traveling Salesperson | ✅ | Traffic Flow (Dijkstra & A*) | ✅ |
| Morphing Rovers | ✅ | The Trigger Arc TSP | ⚠️ |
| Quantum Communications Constellations | ✅ | | |
| Trappist Tour | ✅ | | |
| Delivery Scheduling | ✅ | | |
| Mining | ✅ | | |

---

## 🗂️ Your project after setup / Projekti yt pas përgatitjes

```
your-project/
├── vsi/                  📦 the folder you copied (don't edit) / folderi që kopjove (mos e ndrysho)
├── AGENTS.md                 🤖 instructions for your AI agent / udhëzime për agjentin
├── docs/
│   ├── PROBLEM.md            📄 the problem / problemi
│   ├── REQUIREMENTS.md       ☑️ checklist / lista e kërkesave
│   └── PLAN.md  DECISIONS.md
├── src/
│   ├── algorithms.py         ✍️ YOUR ALGORITHMS / ALGORITMET E TUA
│   ├── generator.py          🎲 test data / të dhënat (ESA: esa_problem.py)
│   └── run.py                ▶️ runs everything / ekzekuton gjithçka
├── tests/                    🧪 tests / testet
├── data/                     🎲 official data (downloaded) / të dhënat zyrtare (të shkarkuara)
├── official/                 🛰️ ESA evaluation code (downloaded) / kodi zyrtar i vlerësimit (ESA)
├── results/                  📊 tables + charts: scaling, convergence, Pareto / tabela + grafikë
├── vsi.json              🧾 project info + data links / info e projektit + linqet e të dhënave
├── tasks.py                  ⚙️ commands (the agent uses them) / komandat (i përdor agjenti)
└── README.md                 📝 your report / raporti yt
```

---

## ❓ Good to know / Mirë ta dish

| 🇦🇱 | 🇬🇧 |
|---|---|
| Skedarët e tu nuk fshihen dhe nuk ndryshohen. | Your own files are never deleted or changed. |
| Mos e ndrysho folderin `vsi`. | Don't edit the `vsi` folder. |
| Ke tashmë `AGENTS.md`? Mos e zëvendëso: VSI i shton udhëzimet e veta në fund të tij. Fjalia "Lexo vsi dhe fillo projektin tim" punon njësoj. | Already have an `AGENTS.md`? Keep yours: VSI adds its instructions at the end. The sentence "Read vsi and start my project" works the same. |
| ChatGPT / Copilot 365 / Gemini në web: pasi të përgatitet projekti, ekzekuto `python tasks.py context` dhe ngarko `CONTEXT.md`. | ChatGPT / Copilot 365 / Gemini web: after setup run `python tasks.py context` and upload `CONTEXT.md`. |
| VSI të jep bazën, jo zgjidhjen. Algoritmin e bën ti, dhe duhet ta kuptosh. | VSI gives you the base, not the solution. The algorithm is yours, and you must understand it. |

| Mark | 🇦🇱 | 🇬🇧 |
|:-:|---|---|
| ✅ | Problemi është kontrolluar nga burimi zyrtar. Gati për punë. | Problem checked against the official source. Ready to work. |
| ⚠️ | Problemi nuk është kontrolluar ende. Agjenti duhet ta lexojë fillimisht faqen zyrtare (ose pyete profesorin). | Problem not checked yet. Your agent must read the official page first (or ask your professor). |

License: MIT
