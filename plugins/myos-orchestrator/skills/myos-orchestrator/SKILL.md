---
name: myos-orchestrator
description: Run heavy multi-source jobs in a MyOS Workspace without overflowing the context window, using an orchestrator + subagent fleets + dump-to-local-file architecture. Use this skill when the user types /myos-orchestrator, or asks to "rebuild the dashboard from all my sources," "run a big multi-source job," "reconcile figures across email/Docs/Sheets/transcripts," "audit this whole folder," or when a task clearly needs more than one context window of raw input. The orchestrator never ingests raw data: data-gathering subagents dump raw source to files under a scratch folder and return only paths, and update subagents work from those files.
---

# MyOS Orchestrator — heavy jobs without losing the data

The breakthrough that made an AI project manager reliable was an architecture, not a smarter model. The naive setup fed one agent everything and lost information. The first fix was an orchestrator delegating to subagent fleets. The fix that actually worked went deeper: the data-gathering subagents stopped summarizing and **dumped raw source to local files**, and the orchestrator pointed update-subagents at those files by path, so decisions were made on raw data instead of AI recaps, and no single context window ever had to hold the whole corpus.

MyOS is a filesystem, so this pattern is native. This skill runs that flow for any heavy multi-source job. The reference files carry the mechanics:

- `reference-pattern.md` — the architecture in detail: roles, the scratch-folder layout, the subagent contracts, dump format, verification, and cleanup.
- `reference-job-template.md` — the job-spec template (goal, sources, target, done-test).

## Operating rules — read before you act

1. **The orchestrator never reads raw source.** Your context is for planning and coordination. The moment you ingest the emails and transcripts yourself, the pattern is defeated and the context window fills. Coordinate over file paths and one-line manifests.
2. **Dump raw, never summaries.** Each data-gathering subagent writes the source through to a file verbatim (or as close as the tool allows) and returns only the path. Summarizing before the update step is the precise failure this exists to prevent.
3. **Predictable, one-file-per-source layout.** So update subagents can be aimed without guesswork. See the scratch layout in `reference-pattern.md`.
4. **Honor the handbook.** If `ME/handbook.md` defines this job, use its "done" test and escalation rules. Draft-don't-send applies to any outbound action.
5. **Only use this when the job warrants it.** It is real overhead. If the work fits one context window, do it directly.
6. **No sycophancy.** No "great question," no "I love that."
7. **No AI tells.** Skip "actually," "honestly," "quietly," and the "not X but Y" construction. No em-dash overuse.
8. **Tone:** polished, confident, approachable, direct. Never salesy. Say "completion," never "graduation."

## The architecture

```
ORCHESTRATOR (this session)        ← plans, coordinates, verifies. Never ingests raw source.
   │
   ├─ gather subagent → reads source A → DUMPS raw to 00 Inbox/_work/<job>/A.md → returns path
   ├─ gather subagent → reads source B → DUMPS raw to 00 Inbox/_work/<job>/B.md → returns path
   ├─ gather subagent → reads source C → DUMPS raw to .../C.md → returns path
   │
   └─ update subagent(s) → read the dump files BY PATH → edit the target → report done
```

The orchestrator holds only the job spec, the list of dump paths, and the manifests. The raw data lives on disk, read only by the subagents that need it, at the step that needs it.

## The scratch folder

```
<workspace>/00 Inbox/_work/<job-slug>/      # cross-project jobs
   _manifest.md          # the job spec + the list of dumps with one-line descriptions
   <source>.md           # one raw dump per source
   ...
```

For project-scoped work, use the project's own folder instead of `00 Inbox/_work/` so the dumps live with the project. Keep one job per subfolder so cleanup is a single delete.

## Run flow

1. **Define or load the job.** Use `reference-job-template.md`: goal, sources (mapped to connected tools), the target to update, and the explicit "done" test. If `ME/handbook.md` defines this recurring job, pull its definition and done-test from there.
2. **Plan the fleet.** As orchestrator, list the data-gathering subagents (one per source) and the update subagents. Write the job spec to `_manifest.md` in the scratch folder.
3. **Gather — fan out.** Spawn the data-gathering subagents in parallel. Each one: read its assigned source, write the raw content to its dump file, return only the path and a one-line description for the manifest. Instruct them explicitly not to summarize and not to return the content inline.
4. **Update — fan out.** Spawn update subagents pointed at the dump files by path. They read the raw dumps, make the changes against the target (a sheet, a status doc, a dashboard), and report what changed. They work from raw data, not from anything the orchestrator paraphrased.
5. **Verify.** Check the result against the "done" test. If a source was thin or a dump failed, re-run that one subagent rather than the whole job.
6. **Index and clean up.** If `myos-local-search` is installed, run `qmd update && qmd embed` so the dumps are searchable. Then apply the retention rule from `reference-pattern.md`: keep the dumps if they have lasting value (archive the folder), or delete the scratch subfolder if they were transient.

## Why this pairs with the rest of MyOS

- **`myos-handbook`** supplies the job definitions and "done" tests the orchestrator executes.
- **`myos-heartbeat`** can trigger an orchestrated job on a schedule — a Sunday-night dashboard rebuild that fans out, dumps, updates, and leaves the result for Monday.
- **`myos-local-search`** makes the raw dumps searchable after the fact, so a job's gathered source becomes part of the workspace's memory instead of disposable scratch.
