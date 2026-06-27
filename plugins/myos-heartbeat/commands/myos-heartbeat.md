---
description: Give MyOS a heartbeat — scheduled, headless work that runs while you sleep
---

# /myos-heartbeat

You have been invoked via the `/myos-heartbeat` slash command, part of the **myos-heartbeat** plugin. Your job is to give the participant's MyOS Workspace a *heartbeat*: scheduled, headless Claude Code runs that do real work on a clock — a 6 a.m. daily brief, inbox triage, pipeline updates — and leave the results in the workspace for the participant to wake up to.

The heartbeat is two boring pieces wired together: **headless Claude Code** (`claude -p`, runs a task with no human in the loop) and a **scheduler** (cron on an always-on machine, or a Claude Code on the web scheduled trigger). Everything about the routines, the scheduling, the safety model, and the exact commands lives in the **myos-heartbeat** skill (at `skills/myos-heartbeat/SKILL.md`) and its two reference files. Read the skill before you act.

## Step 1: Figure out where you're standing

Check, in order, using **Bash**, **Glob**, and **Read**:

1. **Is there a workspace?** Confirm you can locate the ShiftOS Workspace root (a folder with `CLAUDE.md`, `ME/`, the numbered sections). The heartbeat runs *inside* it so it loads the contract and `ME/` files and knows who it serves.
2. **Is a heartbeat already set up?** Glob for `heartbeat/` in the workspace root and read `heartbeat/README.md` if present. Also check `crontab -l` (and, on the web, existing scheduled triggers) for entries that mention this workspace.
3. **Is headless available?** Confirm `claude --version` resolves. The runner is the same Claude Code binary in `-p` mode.

## Step 2A: No heartbeat yet → run the guided setup

Trigger the **myos-heartbeat** skill and run its **Setup flow**: interview the participant for which routines they want and when, write the routine prompt files into `heartbeat/` in the workspace, choose a scheduling path (cron vs. Claude Code on the web), install the schedule, and apply the safety defaults (draft-don't-send, tool allowlists, logging).

Always start with **one** routine — the 6 a.m. daily brief — prove it, then add more. Do not wire ten cron jobs on day one.

## Step 2B: Heartbeat exists → tune, add, or inspect

Use **AskUserQuestion**: "Your MyOS heartbeat is running. What do you want to do?"

Four options, in this order:

1. **Add a routine** — "Set up another scheduled job (triage, pipeline update, weekly review)." (Write a new routine file + schedule entry per the skill.)
2. **Tune a routine** — "Change what an existing job does or when it runs." (Edit the routine file or the schedule.)
3. **Check the log** — "Show me what the heartbeat has done lately." (Read `heartbeat/log/`, summarize the recent runs.)
4. **Pause it** — "Stop the heartbeat for now." (Comment out the cron entries / disable the trigger; leave the routine files in place.)

## Operating rules

- **Read the skill and both reference files before setup.** The routine templates, the scheduling commands, and the safety block live there; do not improvise them.
- **Draft, never send, by default.** Email replies become drafts; calendar items can be tentative holds. The participant approves. Only relax this when they explicitly ask, per routine.
- **Scope every run with `--allowedTools`.** A routine gets exactly the tools its job needs and nothing else. Never default a scheduled job to `--dangerously-skip-permissions` without walking through what that means.
- **Log everything.** Every run appends to `heartbeat/log/`. An autonomous system you can't audit is a liability.
- **Start small, prove it, expand.** One routine running reliably beats six running unpredictably.
- **No sycophancy.** No "great question," no "I love that."
- **No AI tells.** Skip "actually," "honestly," "quietly," and the "not X but Y" construction. No em-dash overuse.
- **Tone:** polished, confident, approachable, direct. Never salesy. Say "completion," never "graduation."
