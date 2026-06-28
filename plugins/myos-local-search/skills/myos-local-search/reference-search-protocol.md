# Reference — the search-first wiring

Installing qmd gives MyOS a search engine. These two edits give MyOS the *habit* of using it. Without them, the engine sits idle because no session knows it exists. Apply both during setup. Show each edit before saving.

---

## Edit 1 — `ME/context-map.md`

`context-map.md` is where MyOS records where its information lives. Add a **Local search** section so every session learns the engine is the front door to all of it. Append this block (adjust the collection list to whatever was actually created):

```markdown
## Local search

This workspace has a local search engine: **qmd**, running on this machine (nothing leaves it). It indexes four collections:

- `workspace` — this whole workspace (ME/, 00–04, KNOWLEDGE/)
- `transcripts` — meeting notes
- `sessions` — past Claude / Cowork conversation logs
- `docs` — outside work documents

**Rule:** before answering any "where / when / what did I conclude / did we ever" question from memory, search first — `qmd query "<question>" -c <collection>`. Drop `-c` to search everything. Cite the source file in the answer. Re-index with `qmd update && qmd embed` if results look stale.
```

---

## Edit 2 — root `CLAUDE.md` (the contract)

The contract is what every session obeys. Insert this block so search becomes a default reflex, not an afterthought. **Keep the marker comment** — `/myos-search` uses it to detect that wiring is installed.

```markdown
<!-- myos-local-search -->
## Local search (search before you guess)

This workspace has a local search engine (qmd) indexing the workspace, meeting transcripts, past session logs, and outside documents — all on this machine.

When you need something that is **not** in the files already loaded this session — a past decision, an old number, a meeting outcome, a precedent in Archives, something from a prior conversation — **run a search before you say you don't know and before you fall back to plain Grep**:

- `qmd query "<what you're looking for>" -c <collection> -n 5` — hybrid, re-ranked (best quality)
- Collections: `workspace`, `transcripts`, `sessions`, `docs`. Omit `-c` to search all.
- Pull full context with `qmd get "<path>"`. Always cite the source file you used.

If `qmd` is unavailable, fall back to Grep/Glob across the workspace folder and note that results are keyword-only and limited to the open workspace.
<!-- /myos-local-search -->
```

Place it after the existing "read ME/ first / project pattern / log to memory" rules, alongside the other standing instructions.

---

## Edit 3 (optional) — `ME/specialist-routing.md`

If the workspace has a `specialist-routing.md` bench, add one line so search shows up as a named capability:

```markdown
- **Local search** (`myos-local-search`) — qmd-powered search across the workspace, meetings, past sessions, and outside docs. Run `/myos-search`.
```

---

## Fallback variant (no qmd)

When qmd can't be installed, wire the habit anyway with the narrower engine. Use this block in the root `CLAUDE.md` instead of Edit 2:

```markdown
<!-- myos-local-search -->
## Local search (search before you guess)

When you need something not in the files already loaded this session, run a Grep/Glob sweep across the workspace folder before saying you don't know.

This is keyword-only and limited to the open workspace — it does not reach past sessions, meeting transcripts outside this folder, or outside documents, and it can't match on meaning. To upgrade to full semantic search across all of those, install qmd (`npm install -g @tobilu/qmd`) and run `/myos-search`.
<!-- /myos-local-search -->
```

And one line in `ME/context-map.md`:

```markdown
## Local search

Keyword search only (Grep), limited to this workspace folder. Install qmd and run `/myos-search` to upgrade to semantic search across meetings, past sessions, and outside documents.
```

---

## How a session should actually search

The behavior the wiring installs, in practice:

1. **Trigger.** A question whose answer isn't in the loaded files: "where did we land on…", "what was the Q1 number", "did the board ever discuss…", "what did I write about…".
2. **Route.** Decision/precedent/conclusion → `workspace`. Meeting → `transcripts`. Prior conversation → `sessions`. Outside file → `docs`. Unsure → search all (no `-c`).
3. **Query.** `qmd query "<natural-language question>" -c <collection> -n 5`. Use `qmd search` only when you want fast exact-keyword, `qmd vsearch` only when you want pure semantic.
4. **Open.** Read the top hits; pull full context with `qmd get "<path>"` when a snippet isn't enough.
5. **Answer with a citation.** Name the file (and line range where useful) so the participant can verify and open it.
