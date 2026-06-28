---
name: myos-heartbeat
description: Give a MyOS / ShiftOS Workspace a heartbeat — scheduled, headless Claude Code work that runs while the participant sleeps. Use this skill when the user types /myos-heartbeat, or asks to "set up a heartbeat," "run Claude Code on a schedule," "draft my morning briefing automatically," "triage my inbox overnight," "make MyOS work while I sleep," or "build the OpenClaw heartbeat with Claude Code." Interviews for routines, writes routine prompt files into the workspace, wires cron or a Claude Code on the web trigger, and installs draft-don't-send safety defaults. The heartbeat is headless Claude Code (claude -p) plus a scheduler — nothing more exotic.
---

# MyOS Heartbeat — work that runs while you sleep

OpenClaw's calling-card feature is the heartbeat: a process that runs on a clock, decides what needs doing, and does it, so at 6 a.m. the daily brief is written and the replies are drafted before the participant looks at their phone. Underneath, it's a cron job running a headless agent. Claude Code has the same two pieces — a headless mode (`claude -p`, a task with no human in the loop) and the ability to run inside the workspace so it already knows who it serves. Wire them to a scheduler and MyOS works overnight.

This skill builds that. It does the part that makes it safe and durable: routines live as files in the workspace, every run is scoped and logged, and email goes out as drafts the participant approves, not as autonomous sends.

Two halves: **Setup** (write routines, schedule them, install safety) and the **runtime contract** (what a routine prompt actually contains). Read both reference files before setup:

- `reference-routines.md` — ready-to-use routine prompts (daily brief, inbox triage, pipeline update, weekly review) and the structure every routine follows.
- `reference-scheduling.md` — the headless command, the two scheduling paths (cron and Claude Code on the web), and the full safety model.

## Operating rules — read before you act

1. **Start with one routine.** The 6 a.m. daily brief. Prove it runs and the output is good before adding anything. A pile of cron jobs installed on day one is how trust dies.
2. **Draft, never send, by default.** Replies become drafts; calendar items can be tentative holds. The participant approves every outbound action. Relax this only per-routine, only when they ask.
3. **Scope every run.** Each routine gets an explicit `--allowedTools` allowlist matching its job. Never hand a scheduled job blanket permissions without walking the participant through the consequences.
4. **Log everything.** Every run appends to `heartbeat/log/`. If you can't audit what ran overnight, you can't trust it.
5. **It runs inside the workspace.** The heartbeat `cd`s into the workspace root so the root `CLAUDE.md` contract and `ME/` files load — the routine inherits who the participant is, their voice, their memory.
6. **No sycophancy.** No "great question," no "I love that."
7. **No AI tells.** Skip "actually," "honestly," "quietly," and the "not X but Y" construction. No em-dash overuse.
8. **Tone:** polished, confident, approachable, direct. Never salesy. Say "completion," never "graduation."

## What the heartbeat is made of

```
claude -p "<routine prompt>"      ← headless: one task, no human, runs to completion and exits
        +
cron (or a web trigger)            ← fires that command on a schedule
        =
work that happens while you sleep
```

Everything else is what you put in the routine prompt and how tightly you scope it.

## The folder it builds

The heartbeat lives in the workspace so it's inspectable and version-controllable alongside everything else:

```
<workspace>/heartbeat/
  README.md            # what's scheduled, when, and the safety rules in force
  routines/
    daily-brief.md     # the prompt for the 6 a.m. run
    inbox-triage.md    # optional, added later
    pipeline-update.md # optional
  log/
    2026-06-27.md      # what each run did, appended per run
```

## Setup flow

### 1. Locate the workspace and confirm headless works

- Find the ShiftOS Workspace root (`CLAUDE.md`, `ME/`, numbered sections). Routines run from here.
- Confirm `claude --version` resolves on the machine that will run the schedule.
- Identify the machine. An always-on box (a Mac Mini is the canonical choice — it doesn't depend on a laptop being open) points to **cron**. No always-on machine points to **Claude Code on the web** scheduled triggers, which run in the cloud. Pick the path with the participant; details in `reference-scheduling.md`.

### 2. Interview for the first routine

Keep it to the daily brief for now. Ask, one at a time:

- **What should the 6 a.m. brief cover?** Overnight email, today's calendar, today's tasks, anything pulled forward from `00 Inbox/`. Map each to a connected MCP tool (mail, calendar, task manager) the participant actually has.
- **What time?** Default 6 a.m. local.
- **What may it do without asking?** Default: read everything, write the brief to `00 Inbox/`, draft replies. Nothing sends.

### 3. Write the routine file

Create `heartbeat/routines/daily-brief.md` from the template in `reference-routines.md`, personalized to their tools and seat. The routine prompt tells the headless run exactly what to read, what to produce, where to save it, and what it must not do (no sends).

### 4. Wire the schedule

Use `reference-scheduling.md`. In short, for cron on an always-on Mac:

```cron
0 6 * * *  cd "/path/to/ShiftOS Workspace" && /usr/local/bin/claude -p "$(cat heartbeat/routines/daily-brief.md)" --allowedTools "Read,Write,mcp__mail__*,mcp__calendar__*" --permission-mode acceptEdits >> "heartbeat/log/$(date +\%Y-\%m-\%d).md" 2>&1
```

For Claude Code on the web, create a scheduled trigger on this repo/workspace that runs the same routine prompt. Either way, the run is headless, scoped, and logged.

### 5. Install the safety defaults

- Confirm the allowlist excludes send/delete tools for any draft-only routine.
- Confirm output is written to `00 Inbox/` and the log, not emailed.
- Write `heartbeat/README.md` recording what's scheduled, when, the tool scope, and the draft-don't-send rule, so the participant (and any future session) can see the whole autonomous surface in one file.

### 6. Prove it once, live

Run the routine by hand first: `cd <workspace> && claude -p "$(cat heartbeat/routines/daily-brief.md)" --allowedTools "..."`. Read the brief it produces with the participant. Fix the routine prompt until the output is good. *Then* let the schedule take over. Never let an unproven routine run unattended.

### 7. Expand deliberately

Once the daily brief is trusted, add routines one at a time from `reference-routines.md` (inbox triage, pipeline update, weekly review), each with its own file, schedule entry, and scope.

## The compounding advantage

A MyOS heartbeat beats a generic one because it runs inside a file-based workspace:

- **It already knows the participant** — the contract and `ME/` files load at the start of every run.
- **It remembers** — routines log to `heartbeat/log/` and to `ME/memory.md`, so each run inherits the last.
- **It can recall** — paired with the `myos-local-search` plugin (qmd), a routine can search every past session and meeting before it drafts, so it never re-asks what's already decided.

Heartbeat (does work on a clock) + memory (remembers across runs) + search (recalls everything) is the combination that turns scheduled scripts into something that feels like an employee.

## Pause / teardown

To pause: comment out the cron lines (`#`) or disable the web trigger. Leave the routine files — they're the participant's IP. To remove a routine entirely: delete its `routines/*.md` file and its schedule entry, and note it in `heartbeat/README.md`.
