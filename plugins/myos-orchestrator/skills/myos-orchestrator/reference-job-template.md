# Reference — the job-spec template

Define a job before running it. A vague job produces vague fan-out. This template is small on purpose; the discipline is in filling every line concretely. For recurring jobs, store the filled spec in `ME/handbook.md` (under Recurring jobs) and load it instead of re-defining each time.

---

```markdown
# Job: [name]

## Goal
[One sentence. What is true when this is finished?]

## Sources
[Every place raw input lives, each mapped to the connected tool that reads it. One row = one gather subagent = one dump file.]
- [Source] → [tool] → dumps to `_work/<job>/<file>.md`
- [Source] → [tool] → dumps to `_work/<job>/<file>.md>`
- ...

## Target
[Exactly what gets updated — the sheet, the status doc, the dashboard, the file path or tool.]

## Done when
[The explicit test. Concrete enough that a subagent can check it. Not "the dashboard is updated" but "every active client has a status, a next action, and an owner, and nothing is older than this week."]

## Escalate if
[The lines that stop the job and go to the participant: a figure that won't reconcile, a missing source, anything outside the defined scope. Pull from ME/handbook.md if the job lives there.]

## Outbound policy
[Default: draft, never send. Note any exception this specific job is authorized for.]
```

---

## Worked example — weekly client-status rebuild

```markdown
# Job: Weekly client-status rebuild

## Goal
The client-status dashboard reflects reality across every active engagement as of this week.

## Sources
- Overnight + this-week email → Gmail MCP → `_work/client-status/email.md`
- Client call transcripts since last run → transcripts/Granola → `_work/client-status/transcripts.md`
- Deal pipeline → CRM MCP → `_work/client-status/crm.md`
- Current dashboard → the Sheet → `_work/client-status/current.md`

## Target
The client-status Google Sheet (Dashboard tab).

## Done when
Every active client has: current status, next action, owner, and last-touch date. Nothing older than this week. Any figure that disagrees across sources is flagged, not silently picked.

## Escalate if
A client's status can't be determined from the sources, a revenue figure disagrees across CRM and email, or a new client appears with no record.

## Outbound policy
Draft, never send. The dashboard is updated in place; no client emails go out from this job.
```

## Notes

- **One source, one row, one dump, one subagent.** Keep the mapping clean so the fan-out and the update step line up.
- **Write the "Done when" test before you run anything.** It's what the verification step checks and what keeps the job from finishing on a half-built result.
- **Recurring jobs belong in the handbook.** Define once in `ME/handbook.md`, then `/myos-orchestrator` loads it. That's also what lets `myos-heartbeat` schedule the same job.
