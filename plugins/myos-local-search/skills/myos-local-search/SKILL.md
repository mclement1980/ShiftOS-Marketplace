---
name: myos-local-search
description: Give a MyOS / ShiftOS Workspace a local search engine and teach every session to use it. Use this skill when the user types /myos-search, or asks to "set up local search," "give MyOS a search engine," "index my workspace," "search across my meetings/transcripts/sessions," "find that across everything," or "make MyOS remember." Installs and configures qmd (a local-first full-text + semantic search CLI), builds four collections that mirror the MyOS layers (workspace, transcripts, sessions, docs), and wires the calibration layer and the root contract so sessions search before they say "I don't know." Falls back to Claude Code Grep when qmd can't be installed.
---

# MyOS Local Search — give the workspace a memory

A MyOS Workspace can recall what's in the files it loads at the start of a session. It cannot, on its own, find the decision buried in a meeting from March, the number from a session three weeks ago, or the precedent sitting in `04 Archives/`. `ME/context-map.md` says *where* things live; it does not *search* them. Claude Code's Grep searches the open folder, by exact keyword only.

This skill closes that gap. It installs [qmd](https://github.com/tobi/qmd) — a local CLI that runs full-text (BM25), vector semantic, and LLM re-ranked search, entirely on the machine — and points it at four corpora that mirror how MyOS is already organized. Then it does the part that matters most: it teaches MyOS to reach for the engine by default, so the workspace stops forgetting.

The job has two halves. **Setup** (build the engine and wire it in) and the **Search protocol** (how a session uses it during normal work). Read both reference files before running setup:

- `reference-collections.md` — the canonical definitions of the four collections and the exact qmd commands to build and maintain them.
- `reference-search-protocol.md` — the wiring blocks to insert into `ME/context-map.md` and the root `CLAUDE.md`, plus the in-session behavior they install.

## Operating rules — read before you act

1. **Confirm paths before you index.** Every machine lays out its folders differently. Show the participant the four paths you intend to point qmd at and get a yes before creating any collection. Never guess a path and run.
2. **Local stays local.** qmd downloads small models once and runs them on-device; no document leaves the machine. State this when it's relevant — it's why this is safe for board, partner, and council material.
3. **Cite sources.** Every answer you return from a search names the file it came from (and a line range where it helps), so the participant can open the original.
4. **Degrade gracefully, never silently.** If qmd cannot be installed, fall back to Grep-over-workspace and tell the participant exactly what they're giving up. Do not pretend a keyword grep is semantic search.
5. **No sycophancy.** No "great question," no "I love that."
6. **No AI tells.** Skip "actually," "honestly," "quietly," and the "not X but Y" construction. No em-dash overuse.
7. **Tone:** polished, confident, approachable, direct. Never salesy. Say "completion," never "graduation."

## The four collections

qmd organizes content into named collections you can search together or one at a time. These four map onto the MyOS layers, so a participant who knows the workspace already knows the engine:

| Collection | Points at | The question it answers |
|---|---|---|
| `workspace` | the ShiftOS Workspace root — `ME/`, `00`–`04`, `KNOWLEDGE/` | "What did I conclude about X? Where's that project file? What's the precedent in Archives?" |
| `transcripts` | wherever the notetaker drops meeting notes (e.g. `03 Resources/Meetings/`, or a Granola/Fathom/Otter export folder) | "What did the board chair actually say about the budget in March?" |
| `sessions` | the Claude Code / Cowork session logs (JSONL transcripts of past conversations) | "What did we decide last week? Where did that draft go?" |
| `docs` | work documents outside the workspace the participant wants searchable (Downloads, a synced Drive folder) | "Find that partner agreement I never filed." |

Exact `qmd collection add` commands, masks, and the JSONL handling for `sessions` are in `reference-collections.md`.

## Setup flow

### 1. Confirm the environment

- Run `qmd doctor` (or `qmd --version`). If qmd is already installed and healthy, skip to step 3.
- If qmd is missing, check for a runtime: `node --version` then `bun --version`. qmd installs via either.
  - **Node or bun present** → continue to step 2 (install).
  - **Neither present, and the participant can install software** → point them to install [Node](https://nodejs.org) (LTS) or [bun](https://bun.sh), then continue.
  - **Neither present and the machine is locked down** → go to **Graceful fallback** below. Do not dead-end the participant.
- Confirm you're standing in (or can locate) the ShiftOS Workspace root: a folder with `CLAUDE.md`, `ME/`, and the numbered sections. The `workspace` collection points here.

### 2. Install qmd

```bash
npm install -g @tobilu/qmd
# or, if they use bun:
bun install -g @tobilu/qmd
```

Then `qmd doctor` to confirm it resolves and can fetch its models. The first run downloads small GGUF models (embedding + reranker) once; tell the participant this is a one-time download.

### 3. Build the four collections

Walk the participant through the four paths, confirm each, then create the collections and index. Use the exact commands in `reference-collections.md`. In short:

```bash
qmd collection add "<workspace-root>"        --name workspace
qmd collection add "<meetings-folder>"       --name transcripts
qmd collection add "<session-logs-folder>"   --name sessions    --mask "**/*.jsonl"
qmd collection add "<external-docs-folder>"  --name docs
qmd update          # index everything
qmd embed           # generate vector embeddings for semantic search
qmd status          # confirm it's healthy
```

Skip any collection the participant doesn't have a source for (not everyone keeps meeting transcripts). `workspace` is the one that must exist.

### 4. Wire MyOS to use it

This is what turns an installed CLI into a workspace that searches by default. Apply both edits from `reference-search-protocol.md`:

- **`ME/context-map.md`** — add the **Local search** entry that names the four collections and the rule to query before answering "where / when / did we ever" questions.
- **Root `CLAUDE.md`** — insert the **search-first** block (it carries the `<!-- myos-local-search -->` marker the command uses for detection). The block tells every session: when you need something that isn't in the files already loaded, run a qmd search before falling back to Grep or saying you don't know.

Show both edits before saving. If a `specialist-routing.md` exists, add a one-line bench entry for local search there too.

### 5. Keep it fresh

The index is a snapshot; it goes stale as the participant works. Offer one of:

- **On demand** — re-run `qmd update && qmd embed` from `/myos-search` → "Re-index" whenever they want current results.
- **Automatic** — a `qmd watch` process, or a cron entry (`*/30 * * * * qmd update && qmd embed`) so it refreshes itself. Setting up cron is the natural bridge to the heartbeat pattern; mention it if they want hands-off freshness.

### 6. Confirm completion

Run one real search the participant cares about (`qmd query "<their topic>" -n 5`), show the results with sources, and confirm the wiring is live. Close with what changed: MyOS can now search across everything indexed, every session knows to use it, and nothing left the machine.

## Search protocol

Once the engine is wired, this is how a session uses it during normal work. The full behavior block lives in `reference-search-protocol.md`; the essentials:

- **Reach for it before guessing.** When the answer to a "where / when / what did we decide / did we ever" question isn't in the loaded files, search before you say you don't know.
- **Pick the collection by the question.** A past decision or precedent → `workspace`. A meeting → `transcripts`. A prior conversation → `sessions`. An outside document → `docs`. Searching across all of them → drop the `-c` flag.
- **Use `qmd query` for quality.** It runs hybrid search with re-ranking. Reserve `qmd search` (fast keyword) and `qmd vsearch` (pure semantic) for when you specifically want one mode.
- **Read, then cite.** `qmd query "..." -c workspace -n 5` returns ranked snippets with paths. Pull the source with `qmd get "<path>"` when you need the full context, and name the file in your answer.

```bash
qmd query "lodging tax argument that landed with council" -c workspace -n 5
qmd query "board chair budget concerns" -c transcripts
qmd query "what did we decide about the spring co-op" -c sessions
qmd query "partner agreement renewal terms"          # across all collections
```

## Graceful fallback (no qmd)

If qmd can't be installed, MyOS still gets a search-first habit, just a narrower one. Do this:

1. **Wire the contract anyway**, with the fallback variant of the block in `reference-search-protocol.md`: when a session needs something not in the loaded files, run a Grep/Glob sweep across the workspace folder before saying it doesn't know.
2. **State the limits plainly.** Grep covers the open workspace, by exact keyword. It does not reach past sessions, meeting transcripts outside the folder, or outside documents, and it can't match on meaning. That coverage and semantic search are exactly what qmd would add.
3. **Leave the upgrade path.** One line in `ME/context-map.md`: "Local search is keyword-only (Grep). Install qmd and run `/myos-search` to upgrade to full semantic search across meetings, sessions, and outside docs."

That way the participant gets value now and a clear, single step to the full engine when their machine allows it.
