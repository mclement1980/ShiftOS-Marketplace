# Reference — the four MyOS collections

The canonical definitions. Build the engine from these; don't improvise paths or masks. qmd's CLI is `qmd` (package `@tobilu/qmd`); config lives at `~/.config/qmd/index.yml`.

Confirm every path with the participant before running — layouts differ per machine. Skip any collection they have no source for. `workspace` is the only one that must exist.

---

## 1. `workspace` — the ShiftOS Workspace itself

Everything the participant and their sessions produce: the `ME/` identity files, the numbered work sections, and `KNOWLEDGE/`.

```bash
qmd collection add "/path/to/ShiftOS Workspace" --name workspace --mask "**/*.md"
```

Notes:
- Point at the **workspace root**, the folder that holds `CLAUDE.md`, `ME/`, `00 Inbox/` … `04 Archives/`, `KNOWLEDGE/`. One collection covers all of it.
- Default mask is markdown, which is what the workspace is made of. Widen to `"**/*.{md,txt}"` if they keep plain-text notes too.
- `04 Archives/` is a feature, not noise — last year's board packet is this year's precedent. Index it. Only exclude a subfolder if the participant asks.

## 2. `transcripts` — meeting notes

Wherever the notetaker drops meeting transcripts and summaries.

```bash
qmd collection add "/path/to/meetings" --name transcripts --mask "**/*.{md,txt}"
```

Notes:
- Common locations: `03 Resources/Meetings/` inside the workspace, or an export folder from Granola, Fathom, Otter, or Zoom.
- If transcripts already sit inside the workspace folder, they're covered by `workspace`; a separate `transcripts` collection is worth it only when they live elsewhere, or when the participant wants to search meetings in isolation.

## 3. `sessions` — past conversation logs

The Claude Code / Cowork session history, so MyOS can recall what was discussed and decided in earlier conversations.

```bash
qmd collection add "/path/to/session-logs" --name sessions --mask "**/*.jsonl"
```

Notes:
- Claude Code stores per-project session transcripts as JSONL, typically under `~/.claude/projects/<encoded-project-path>/`. Point at the relevant project folder, or at `~/.claude/projects/` to cover all of them.
- The `--mask "**/*.jsonl"` override matters — qmd defaults to markdown and would otherwise skip these.
- This is the same move qmd documents for indexing agent session history: the logs become searchable memory of past work.

## 4. `docs` — outside work documents

Work documents the participant never filed into the workspace but wants searchable.

```bash
qmd collection add "/path/to/Documents-or-Drive" --name docs --mask "**/*.{md,txt}"
```

Notes:
- Common locations: a synced Google Drive / Dropbox folder, or `~/Downloads`.
- qmd indexes text. For PDFs and Office files, convert to text/markdown first (or keep a notetaker's text export); don't point qmd at a folder of raw binaries and expect hits.

---

## Index, embed, verify

After the collections exist:

```bash
qmd update     # crawl all collections and build the full-text index
qmd embed      # generate vector embeddings (enables semantic + hybrid search)
qmd status     # show index health and document counts
qmd collection list   # confirm all four collections are registered
```

`qmd embed -f` forces a full re-embed if results look stale or the model changed.

## Keep it fresh

The index is a snapshot. Pick a refresh strategy with the participant:

- **On demand:** `qmd update && qmd embed` — run from `/myos-search` → "Re-index."
- **Watch:** `qmd watch` — re-indexes as files change, while the process runs.
- **Cron (hands-off):** every 30 minutes —
  ```cron
  */30 * * * * /usr/local/bin/qmd update && /usr/local/bin/qmd embed
  ```
  Use the absolute path from `which qmd`. This cron step is also the on-ramp to the heartbeat pattern — the same scheduler that keeps search fresh can run scheduled MyOS work.

## Maintenance

```bash
qmd doctor     # diagnose install + model fetch problems
qmd cleanup    # clear cache and orphaned index data
qmd collection remove <name>   # drop a source
qmd collection rename <old> <new>
```
