# Reference — the handbook template

The structure for `ME/handbook.md`. Fill every section from the participant's answers and their existing `ME/` files. Keep it operational: how the work is done and what "done" looks like, not who the participant is. Use plain Markdown so it stays inspectable and editable.

---

```markdown
# Employee Handbook — [Seat / role name]

**Version:** 1.0  ·  **Updated:** [date]  ·  **For:** [participant / the seat this covers]

> Required reading. Every session reads this in full before doing any work. This is the operational ground truth for the seat — see `master-profile.md` for who I am and `role-master-prompt.md` for the deep expertise.

## Success criteria

What good output looks like for this seat, concretely enough to grade against:

- [e.g. Board updates lead with the decision needed, then the numbers, then context. One page. No hedging.]
- [e.g. Partner follow-ups go out within one business day and reference the specific commitment made.]
- [The bar, in 3–6 lines.]

## The cast

Who the work involves and what each needs (kept current here; sourced from `master-profile.md`):

- **[Name, role]** — [what they care about, how they like things delivered, what to never do]
- **[Name, role]** — [...]

## Recurring jobs

Each repeated job, defined so it can run the same way every time.

### [Job name — e.g. Weekly client-status update]
- **Trigger:** [schedule or event]
- **Inputs:** [sources — email, transcripts, a sheet, a CRM; map to the connected tools]
- **Steps:** [the sequence, briefly]
- **Output goes to:** [exact path — e.g. `02 Areas/Board Reporting/` or `00 Inbox/`]
- **Done means:** [the explicit completion test — what must be true for this to be finished]

### [Job name]
- **Trigger:** ...
- **Inputs:** ...
- **Steps:** ...
- **Output goes to:** ...
- **Done means:** ...

## Escalation rules

When to stop and ask me instead of proceeding. The most important section for any unattended run:

- Escalate before [sending anything to the board / committing a figure I haven't confirmed / replying to (named person)].
- Escalate when [a number doesn't reconcile across sources / a deadline conflicts / a request falls outside the defined jobs].
- When in doubt, draft it and flag it for me. Never send, delete, or commit on a judgment call.

## Standards and guardrails

- Never invent or estimate figures. If a number isn't in a source, say so.
- Outbound (email, messages) is drafted, never sent, unless the job explicitly says otherwise.
- Board- and partner-facing work is final-polish quality before it reaches me.
- [Seat-specific rules.]

## Change log

- v1.0 ([date]) — handbook created.
```

---

## Filling it well

- **Steal from the calibration layer first.** The cast and standards are usually already in `master-profile.md`; pull them forward rather than re-asking.
- **Make "Done means" a test, not a vibe.** "Every active client has a status, a next action, and an owner, and nothing is older than this week" beats "the dashboard is updated."
- **Escalation is where autonomy gets safe.** The more the heartbeat and orchestrator run unattended, the more this section earns its place. Be specific about the lines that must not be crossed without a human.
- **Keep it short enough to be read every time.** This loads at the start of every session. One to two pages. If a recurring job needs a long procedure, put the detail in that project's `CLAUDE.md` and reference it here.
