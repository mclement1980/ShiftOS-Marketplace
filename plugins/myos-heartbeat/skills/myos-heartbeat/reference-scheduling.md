# Reference — scheduling and safety

The heartbeat is headless Claude Code on a schedule. This file has the exact command, the two scheduling paths, and the safety model. Read it before wiring anything.

---

## The headless command

`claude -p` (print mode) runs one task with no human in the loop, to completion, then exits.

```bash
cd "/path/to/ShiftOS Workspace" \
  && /usr/local/bin/claude -p "$(cat heartbeat/routines/daily-brief.md)" \
       --allowedTools "Read,Write,Glob,Grep,mcp__mail__*,mcp__calendar__*" \
       --permission-mode acceptEdits \
       >> "heartbeat/log/$(date +%Y-%m-%d).md" 2>&1
```

Key parts:

- **`cd` into the workspace first** — so the root `CLAUDE.md` contract and `ME/` files load and the run knows who it serves.
- **`-p "$(cat ...)"`** — the routine prompt is read from its file, so you edit the routine without touching the schedule.
- **`--allowedTools`** — the leash. The run can use only what's listed. For a draft-only routine, list read/write and the mail/calendar tools but **never** the send/trash/delete tools.
- **`--permission-mode acceptEdits`** — lets it write files (the brief) without prompting, while still gated to the allowlist. This is the controlled middle ground.
- **`>> log 2>&1`** — capture stdout and errors to the day's log so every run is auditable.

### About `--dangerously-skip-permissions`

This flag removes the permission gate entirely. OpenClaw runs this way by default; Claude Code does not. Use it only for a fully sandboxed, read-only routine where you've decided the blast radius is zero, and never in combination with tools that send, pay, post, or delete. For real back-office work, prefer a tight `--allowedTools` allowlist plus `acceptEdits`. Walk the participant through this choice; do not set it silently.

---

## Path A — cron (always-on machine, e.g. a Mac Mini)

Cron runs a command on a schedule. It needs a machine that's always on, which is exactly why an AI employee like Claudie runs on a Mac Mini instead of a laptop.

Edit the crontab:

```bash
crontab -e
```

Add the daily brief at 6 a.m.:

```cron
0 6 * * *  cd "/path/to/ShiftOS Workspace" && /usr/local/bin/claude -p "$(cat heartbeat/routines/daily-brief.md)" --allowedTools "Read,Write,Glob,Grep,mcp__mail__*,mcp__calendar__*" --permission-mode acceptEdits >> "heartbeat/log/$(date +\%Y-\%m-\%d).md" 2>&1
```

Cron field order is `minute hour day-of-month month day-of-week`. In a crontab, escape every `%` as `\%`. Use the **absolute** path to `claude` (find it with `which claude`) — cron's PATH is minimal. On macOS, the Terminal (or whatever runs cron) may need Full Disk Access for the agent to read mail and files.

Common cadences:

```cron
0 6 * * *      # every day at 6 a.m.
*/30 * * * *   # every 30 minutes (e.g. keep the search index fresh)
0 8 * * 1      # Mondays at 8 a.m. (weekly review)
```

Verify with `crontab -l`. To pause a routine, comment its line with `#`.

---

## Path B — Claude Code on the web (no always-on machine)

Claude Code on the web runs in the cloud, so there's no laptop or Mac Mini to keep awake. It supports **scheduled triggers**: define a schedule and a prompt, and it spins up a headless session on its own against your repo/workspace. This is the right path for a participant who won't run a cron daemon.

Set it up by creating a scheduled trigger on the workspace that runs the routine prompt on the cadence you want. The routine file, the draft-only rules, and the logging all work the same; the cloud session writes its output back to the workspace. See the Claude Code on the web docs: https://code.claude.com/docs/en/claude-code-on-the-web

Trade-off: cron on a Mac Mini gives direct access to local files and locally-installed tools (including a local qmd index); the web path is zero-maintenance but reaches your data through connected integrations rather than the local disk. Pick per the participant's setup.

---

## The safety model (non-negotiable defaults)

An autonomous agent with your email and calendar is powerful and, unguarded, dangerous. The defaults:

1. **Draft, never send.** Routines create email drafts (`create_or_update_draft`), not sends (`send_draft`). Calendar items are tentative holds, not confirmed invites. The participant approves every outbound action. This is enforced twice: the routine's **Never** block and the `--allowedTools` allowlist, which must exclude send/trash/delete tools.
2. **Least privilege per routine.** Each routine gets the narrowest allowlist that does its job. The daily brief reads mail and writes files; it cannot delete a thread or post to Slack.
3. **Everything logged.** `>> heartbeat/log/<date>.md` on every run, plus a one-line summary the routine writes itself. You can reconstruct any night.
4. **Prove before you schedule.** Run every new routine by hand and read its output before the cron/trigger takes over. Never let an unproven routine run unattended.
5. **One surface, written down.** `heartbeat/README.md` lists every scheduled routine, its time, its tool scope, and its send policy — so the entire autonomous footprint is visible in one file the participant can audit and edit.
6. **Cost awareness.** Each run loads the contract + `ME/` (roughly 2,000–5,000 tokens) plus its work. A daily brief is cheap; a once-a-minute heartbeat is mostly idle checks and adds up. Start daily, tighten the interval only where it earns its keep.

---

## Keeping search fresh from the same scheduler

If `myos-local-search` (qmd) is installed, the same cron can keep its index current so the morning brief can recall everything:

```cron
*/30 * * * *  /usr/local/bin/qmd update && /usr/local/bin/qmd embed
```

That makes the heartbeat and the search engine one system: scheduled work that can remember and recall.
