# Reference — the orchestration pattern

The mechanics of the orchestrator + subagent-fleet + dump-to-file architecture. This is the part that has to be exactly right, because the whole reliability gain comes from where the raw data lives and who reads it.

## The roles

**Orchestrator** (the session running `/myos-orchestrator`):
- Holds the job spec, the manifest, and the list of dump paths. Nothing else.
- Plans the fleet, spawns subagents, verifies the result.
- Never reads raw source. If it ever ingests the emails/transcripts/rows itself, the context window fills and the pattern has failed.

**Data-gathering subagents** (one per source):
- Read exactly one assigned source.
- Write the raw content to a dump file, verbatim or as close as the tool allows.
- Return only: the file path and a one-line description for the manifest. No inline content, no summary.

**Update subagents:**
- Receive dump file paths.
- Read the raw dumps and make the changes against the target.
- Report what changed, not what they read.

## The scratch layout

```
<workspace>/00 Inbox/_work/<job-slug>/
   _manifest.md            # job spec + table of dumps
   email-overnight.md      # one raw dump per source
   transcript-2026-06-25.md
   crm-pipeline.md
   current-dashboard.md
```

Rules:
- **One job per subfolder**, slugged from the job name, so cleanup is one delete.
- **One file per source**, named for the source, so update subagents can be aimed by path.
- For project-scoped jobs, put the folder inside the project (e.g. `01 Projects/<project>/_work/`) so dumps live with the work.

## The manifest

`_manifest.md` is the orchestrator's index — the one file it keeps in context:

```markdown
# Job: [name]
**Goal:** [one line]   **Target:** [what gets updated]   **Done when:** [the test]

## Dumps
| File | Source | Note |
|---|---|---|
| email-overnight.md | Gmail, since 5pm | 14 threads, 3 need replies |
| transcript-2026-06-25.md | Granola, client X call | action items + attendees |
| crm-pipeline.md | CRM export | 22 active deals |
| current-dashboard.md | the sheet being updated | current state |
```

## The subagent contracts

**Gather subagent prompt shape:**
> Read [specific source] using [tool]. Write the raw content to `[exact dump path]` using the Write tool — full content, do not summarize, do not abridge. Return only the file path and a one-line description (count, date range, what's notable). Do not return the content in your reply.

**Update subagent prompt shape:**
> Read these dump files by path: [paths]. Using their raw contents, update [target] so that [done-test]. Make the edits directly. Report only what you changed (rows touched, fields updated, anything you couldn't reconcile). Do not send or commit anything outbound — leave drafts for approval.

## Why dump-to-file and not relay

If a gather subagent returns its findings inline, two things go wrong: the orchestrator's context fills with raw source (the original failure), and the subagent is tempted to summarize to stay under its own limit, so the update step runs on a recap instead of the source. Writing to disk fixes both. The orchestrator stays light; the update step reads ground truth.

## Verification

- Check the result against the job's explicit "done" test, not a vibe.
- If one source was thin or a dump failed, re-run that single gather subagent — don't redo the whole fan-out.
- Surface anything that couldn't be reconciled (a figure that disagrees across sources) for the participant rather than guessing. This is an escalation per `ME/handbook.md`.

## Retention and cleanup

Decide per job:
- **Keep** — if the gathered source has lasting value, run `qmd update && qmd embed` (if `myos-local-search` is installed) so it's searchable, then move the folder to `04 Archives/_work/<job>-<date>/`.
- **Discard** — if the dumps were transient, delete the scratch subfolder once the target is updated and verified.

Never leave orphaned `_work/` folders accumulating in `00 Inbox/`. State which choice you made when you report completion.

## Cost and limits

Each subagent is its own context and its own spend. Fan out by source, not by arbitrary slices — one subagent per real source keeps the count proportional to the job. For very large single sources (a 200-page transcript set), have one gather subagent dump in segments to separate files rather than spawning many that each hold part in context.
