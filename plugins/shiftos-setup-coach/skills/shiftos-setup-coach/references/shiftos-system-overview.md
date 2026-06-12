# ShiftOS Workspace — System Overview

The Setup Coach reads this when a user asks for the deeper picture before or during setup. Share it conversationally — pull the parts that answer their actual question, never dump the whole thing.

---

## What the workspace is

The ShiftOS Workspace is a folder system that turns any Claude session into a colleague who already knows you. Instead of re-explaining your DMO, your board, and your preferences in every conversation, you maintain a small set of files that explain it once — and every session reads them before doing anything.

The architecture has three layers and a contract.

## The calibration layer — `ME/`

Six identity files plus one placeholder, each with a distinct job:

- **`master-profile.md`** — who you are: your seat, your destination, how your DMO is funded and governed, how you think, the cast of people around your work, and a closing "Working With Me" section of direct instructions to any AI. The most-read file in the workspace.
- **`writing-rules.md`** — the mechanics of your writing: banned words, AI patterns to kill on sight, formatting law, and your own phrases. Checked before any writing ships.
- **`voice-profile.md`** — the person behind the mechanics: what you believe, the perspective your content carries, and how you sound to your three audiences — board, partners, colleagues. Writing rules stop drafts from sounding like a machine; this file makes them sound like you.
- **`context-map.md`** — where your information lives: storage, CRM, board portal, and the source of truth for the numbers that matter. Saves every session the "where's that file?" round trip.
- **`specialist-routing.md`** — the bench: which ShiftOS plugins own which jobs as the program ships them, plus the domains you want covered next.
- **`memory.md`** — the running notebook. Corrections, preferences, and decisions worth keeping get logged here automatically, and every session reads it. Week six runs smarter than week one because of this file.
- **`role-master-prompt.md`** — placeholder until Session 5, when the Role OS interview fills it with the deep expertise of your seat.

## The work layer — the numbered sections

- **`00 Inbox/`** — capture, unsorted on purpose. Fast and messy at the moment of capture; structure happens at triage.
- **`01 Projects/`** — active work with an end state. Every project carries its own brief (a `CLAUDE.md` that auto-loads), its own running memory, and an `outputs/` folder that finished artifacts ship from.
- **`02 Areas/`** — the seat's ongoing responsibilities: board reporting, convention sales, partner relations, co-op program. No finish lines here, just standards to maintain.
- **`03 Resources/`** — what you collected, unedited: reports, brand guidelines, templates, and your `MY SKILLS/` library of installed coaches.
- **`04 Archives/`** — finished and dormant work. Nothing in a ShiftOS Workspace gets deleted; it gets archived, because last year's board packet is this year's precedent.

## The knowledge layer — `KNOWLEDGE/`

What you concluded, in your own words: the lodging-tax argument that actually lands with your council, what your board chair reads first, why the spring co-op underperforms. Resources is what you collected; KNOWLEDGE is what you know. It has its own operating manual (`KNOWLEDGE/CLAUDE.md`) and goes fully live with Session 3.

## The contract — root `CLAUDE.md`

The operating contract every session obeys: read the ME/ files first, follow the project pattern, log to memory, never invent figures, treat board-facing work as final-polish. Setup adds a personal layer — your always-do and never-do rules and your format defaults — in its **My Operating Preferences** section.

## How a session actually runs

1. Session opens in the workspace → contract loads → ME/ files are read → the session knows who it's working with.
2. You ask for something → if it belongs to a project, that project's brief and memory load too → work happens calibrated to all of it.
3. You correct something worth keeping → it's logged to memory → the next session starts smarter.

That loop is the whole product. The files make the first draft good; the memory makes the tenth draft better.

## The plugins

ShiftOS ships session companions through the ShiftOS Marketplace (`mclement1980/ShiftOS-Marketplace`). Each owns a job: the Setup Coach (Session 1) builds and maintains this calibration layer; the capture-system coach (Session 3) designs what flows into the Inbox and how; the Role OS interview (Session 5) extracts seat expertise into `role-master-prompt.md`; the AI-ready project companion (Session 6) takes a real workflow through the scoping moves. Install each when its session arrives — same marketplace, one click, and updates flow automatically.

## Why files instead of a smarter chatbot

Files are inspectable — you can open any of them and see exactly what the system believes about you. Files are correctable — fix the file, fix every future session at once. And files compound — each one you sharpen raises the floor of everything produced after. A DMO team that maintains this layer covers more board intelligence, more partner follow-through, and more campaign ground with the same people — which is the entire point.
