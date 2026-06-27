# Reference — heartbeat routines

A routine is a prompt file the headless run executes. It lives in `heartbeat/routines/`. Every routine follows the same shape; personalize the content to the participant's seat and connected tools. Start the participant on the **daily brief** alone; add the rest only once that one is trusted.

## The shape every routine follows

```markdown
# Routine: <name>

## Goal
<one sentence — what this run produces>

## Read
- <source 1, mapped to a connected MCP tool>
- <source 2>

## Do
1. <step>
2. <step>

## Write
- Save the output to <path in the workspace, usually 00 Inbox/>
- Append a one-line entry to heartbeat/log/<today>.md
- Log anything worth keeping to ME/memory.md

## Never
- Send any email (drafts only)
- Delete anything
- Act on anything outside the sources listed above
```

The **Never** block is not decoration. It's the in-prompt half of the safety model; the `--allowedTools` allowlist is the other half. Both must agree.

---

## Routine 1 — Daily brief (the first one, 6 a.m.)

`heartbeat/routines/daily-brief.md`:

```markdown
# Routine: Daily brief

## Goal
A short, scannable briefing waiting in 00 Inbox/ before the participant wakes, covering what happened overnight and what needs them today.

## Read
- Overnight email since 5 p.m. yesterday (mail MCP)
- Today's calendar (calendar MCP)
- Today's tasks due (task manager MCP)
- Anything dropped in 00 Inbox/ since the last run

## Do
1. Summarize overnight email: who wrote, what they need, urgency. Group by thread.
2. Lay out today's calendar with any prep each meeting needs.
3. List today's tasks, flag the two or three that actually matter.
4. For messages that clearly need a reply, draft one in the participant's voice (read ME/voice-profile.md and writing-rules.md first). Leave it as a draft.
5. If the myos-local-search engine is installed, search past sessions/meetings for context before drafting anything that references prior decisions.

## Write
- Save as 00 Inbox/YYYY-MM-DD Daily Brief.md, sections: Overnight, Today, Needs You, Drafts queued.
- Append a one-line summary to heartbeat/log/YYYY-MM-DD.md.
- Log any new standing fact (a new contact, a changed deadline) to ME/memory.md.

## Never
- Send any email. Drafts only — the participant approves and sends.
- Create or move calendar events without marking them tentative.
- Delete anything.
```

Allowlist for this routine: `Read,Write,Glob,Grep,mcp__mail__*,mcp__calendar__*,mcp__tasks__*` (substitute the participant's actual server names; exclude any `send`/`trash`/`delete` tool).

---

## Routine 2 — Inbox triage (add after the brief is trusted)

Sorts the inbox into act / read / archive-candidate, drafts replies for the "act" pile, and proposes (does not execute) archives. Same draft-only, log-everything rules. Allowlist adds nothing that sends or trashes — archive proposals go in the brief as a list the participant approves.

## Routine 3 — Pipeline / dashboard update

For a seat that tracks engagements or a sales pipeline: reads the source of truth (a sheet, a CRM via MCP, a project tool), updates the running status doc in `02 Areas/`, and flags what's stalled. Writes to the workspace; does not push changes to the external system unless the participant explicitly enables write-back for this routine.

## Routine 4 — Weekly review (Mondays)

Reads the week's `heartbeat/log/` entries, the `00 Inbox/` accumulation, and `ME/memory.md`, then writes a "last week / this week" review to `02 Areas/` and surfaces anything that's been sitting untouched. Lower frequency, broader scope.

---

## Personalization

Before writing any routine, read the participant's `ME/master-profile.md` (their seat, their people), `voice-profile.md`, and `writing-rules.md` so drafts sound like them. Map each "Read" source to a tool they actually have connected — do not reference a CRM or notetaker they don't use. If a source has no connected tool, leave it out and note the gap rather than inventing a step that will fail at 6 a.m.
