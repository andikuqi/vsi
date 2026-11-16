# VSI chat pack — AI-Powered Multi-Robot Coordination in Dynamic Environments

> **For students using ChatGPT, Gemini or Claude in the browser or the app.**
> Upload this file to the chat and write: *"Read this file and guide me step by step."*
> SQ: Ngarkoje këtë skedar në chat dhe shkruaj: *"Lexo këtë skedar dhe më udhëhiq hap pas hapi."*

Project id (slug): `multi-robot-coordination` · Source: professor brief (see PROBLEM.md)

## Instructions for the AI (read this first, follow it the whole conversation)

You are helping a university student with an **Algorithm Design & Analysis** project. The student may be a
beginner. **Reply in the student's language** (often Albanian). You cannot see their computer, so:

1. Work in **small steps**. Give the exact commands to copy, then **wait** for the student to paste the output.
2. Before the first command, ask which system they use. Use `python` on **Windows** and `python3` on
   **macOS / Linux** in every command you give.
3. When you write code, give the **complete content of one file** and its path (e.g. `src/algorithms.py`),
   never fragments to merge. After every change the student runs `python tasks.py test`.
4. The algorithms are the **student's own work**: explain the idea, pseudocode and complexity, keep the code
   simple and commented, and check they understand it (they must defend it in front of the professor).
   Do not import solver / optimisation libraries for the core algorithm.
5. Never invent results. Numbers in the report come from `results/metrics.csv`.

### Step 1 — set up the project (once)
1. Python 3.10 or newer: `python --version` (Windows) / `python3 --version` (macOS, Linux).
   If it is missing or older: install it from https://www.python.org/downloads/ (Windows: tick "Add to PATH").
2. Download VSI: https://github.com/andikuqi/vsi → **Code → Download ZIP**, unzip it.
3. Copy the folder **`vsi`** and the file **`AGENTS.md`** into the student's project folder
   (an empty folder or their existing GitHub repo).
4. Open a terminal **in the project folder** (Windows: in the folder, type `cmd` in the address bar and press
   Enter; macOS: right-click the folder → New Terminal at Folder; Linux: right-click → Open in Terminal) and run:
   ```
   python -m vsi new multi-robot-coordination . --force
   python tasks.py start
   ```
   (`python3` instead of `python` on macOS / Linux.) `start` installs what is needed, downloads the data,
   runs the tests and a first run, makes charts, starts the report and prints **progress + the next step**.
   Ask the student to paste that output, then explain it in a few simple sentences.

### Step 2 — every work session
1. The student runs `python tasks.py context` and uploads the new **`CONTEXT.md`** (their current code,
   progress and results) to this chat.
2. Take the **next step** it shows (first open requirement), explain it, write the code, then:
   `python tasks.py test` → tick the requirement in `docs/REQUIREMENTS.md` → `python tasks.py report`.
3. Useful commands: `python tasks.py run` (experiments), `python tasks.py plots` (charts),
   `python tasks.py check` (progress + next step).

---

## The project (docs/PROBLEM.md)

## AI-Powered Multi-Robot Coordination in Dynamic Environments

Source: professor's brief.

### Goal
Coordinate a team of robots in a dynamic, obstacle-filled environment to deliver packages, avoid collisions
and re-route when obstacles or new tasks appear.

### Requirements
1. Multi-agent reinforcement learning so robots cooperate (Multi-Agent Deep Q-Learning or PPO).
2. Online path planning with dynamic obstacle updates (A* or RRT*).
3. Priority handling to resolve task conflicts dynamically.
4. Simulated environment with changing conditions (moving obstacles, new tasks).
5. Task allocation with a market-based (auction) algorithm using priority and robot availability.

### Input
Environment map (with dynamic obstacles), initial robot positions and tasks (delivery locations),
reward structure (task completion rewards, penalties for collisions/inefficiency).

### Output
Simulated execution of the robots completing their tasks.

### Metrics
Task completion time, collisions avoided, overall efficiency.

### Challenges
Reward design balancing efficiency, safety and collaboration; high-dimensional states; real-time changes;
scaling to larger teams and environments.

### VSI starter
`src/generator.py` creates grid maps with static and moving obstacles, robots and delivery tasks.

---

## Diagrams

### Problem model

```mermaid
flowchart TD
    w[("Grid: static + moving<br/>obstacles, robots, tasks")]
    a["Task allocation<br/>(auction by priority)"]
    p["Path planning per robot<br/>(A* / RRT*)"]
    c{"Conflict / collision?"}
    r["Resolve by priority<br/>or re-plan"]
    m["Move one time step<br/>(learned policy: MADQL / PPO)"]
    f(["All tasks done:<br/>makespan, collisions, reward"])
    w --> a
    a --> p
    p --> c
    c -->|yes| r
    r --> p
    c -->|no| m
    m -->|new tasks| a
    m -->|done| f
    classDef box fill:#e8f0fe,stroke:#3b6fd8,color:#111
    class a,p,r,m box
    classDef round fill:#e6f6ec,stroke:#2e8b57,color:#111
    class f round
    classDef diamond fill:#fff4e5,stroke:#e08a00,color:#111
    class c diamond
    classDef data fill:#f3e8fd,stroke:#7b3fc4,color:#111
    class w data
```

### Project pipeline

```mermaid
flowchart TD
    d[("src/generator.py<br/>instances small → large")]
    a["src/algorithms.py<br/>YOUR algorithms"]
    e["score() / your evaluator<br/>(validity + cost)"]
    m["tasks.py run<br/>Meter: time, memory, states"]
    c[("results/metrics.csv<br/>history.csv, fronts.json")]
    p["tasks.py plots<br/>scaling, convergence, Pareto"]
    r(["Report<br/>README / docs/REPORT.md"])
    d --> a
    a --> e
    e --> m
    m --> c
    c --> p
    p --> r
    classDef box fill:#e8f0fe,stroke:#3b6fd8,color:#111
    class a,e,m,p box
    classDef round fill:#e6f6ec,stroke:#2e8b57,color:#111
    class r round
    classDef data fill:#f3e8fd,stroke:#7b3fc4,color:#111
    class d,c data
```

---

## Requirements checklist (docs/REQUIREMENTS.md)

## Requirements checklist

### Implementation
- [ ] Grid environment simulator with moving obstacles and new tasks
- [ ] Online path planning (A* or RRT*) with dynamic obstacle updates
- [ ] Auction-based task allocation (priority + availability)
- [ ] Priority / conflict resolution
- [ ] Multi-agent RL (MADQL or PPO) with documented reward structure
- [ ] Collision detection and avoidance
- [ ] Visualisation / animation of the simulation

### Analysis
- [ ] Pseudocode and complexity for planning and allocation
- [ ] Reward design justification
- [ ] Scalability discussion (more robots, bigger maps)

### Experiments
- [ ] Metrics: completion time, collisions avoided, efficiency
- [ ] Comparison (e.g. RL vs planning-only baseline; A* vs RRT*)
- [ ] Increasing team size / map size
- [ ] Graphs and tables in README

### Delivery
- [ ] README report complete
- [ ] Defense preparation
