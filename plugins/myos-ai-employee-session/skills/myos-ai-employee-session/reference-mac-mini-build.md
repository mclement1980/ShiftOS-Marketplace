# Reference: running MyOS as a 24/7 AI employee on a Mac Mini

**Pilot — validate with a test run before cohort rollout.**

This is the concrete build reference for the capstone. It turns the MyOS Workspace into an always-on AI employee, the way Claudie runs on Claude Code. Work top to bottom. The phasing section at the end is the order to actually do it in; everything above it is the parts list.

The model: Claudie is Claude Code plus a thin chat bridge (about 1,100 lines of Python) running 24/7 on a Mac Mini. Nothing here is more exotic than that.

---

## 1. Hardware and account

- **A Mac Mini kept always-on.** Disable sleep so scheduled jobs actually fire:

  ```bash
  sudo pmset -a sleep 0 disablesleep 1
  ```

  Confirm with `pmset -g` (look for `sleep 0` and `disablesleep 1`). Set the machine to power back on automatically after a power loss (System Settings → Energy, "Start up automatically after a power failure").

- **A Claude Max plan.** A 24/7 employee makes many calls; Max is the plan that supports continuous use without per-call metering surprises.

- **Full Disk Access for the terminal running Claude Code.** System Settings → Privacy & Security → Full Disk Access → add Terminal (or iTerm). Without it, headless runs cannot read parts of the workspace or attached folders.

- **Install the CLI and the four plugins.**

  ```bash
  # Claude Code CLI
  npm install -g @anthropic-ai/claude-code
  claude --version

  # From the marketplace, the four capability plugins:
  #   myos-handbook        (/myos-handbook)
  #   myos-local-search    (/myos-search)
  #   myos-heartbeat       (/myos-heartbeat)
  #   myos-orchestrator    (/myos-orchestrator)
  ```

  Each plugin owns its own install flow; run them from inside the workspace (next section).

---

## 2. Whole-workspace context

Always run Claude Code from the **MyOS Workspace root** — the folder that holds `CLAUDE.md`, `ME/`, the numbered work folders (`00 Inbox/` .. `04 Archives/`), and `KNOWLEDGE/`:

```bash
cd ~/MyOS          # wherever the workspace root lives
claude             # interactive, or `claude -p "..."` headless
```

Running from root is what makes this an employee instead of a chatbot. The root `CLAUDE.md` contract loads, the calibrated `ME/` files load, and the required-reading handbook (wired by `myos-handbook`) loads with them. The employee knows who it serves before it does anything.

---

## 3. The chat surface

Claudie's chat surface is a thin bridge: roughly 1,100 lines of Python that take a Slack (or iMessage) message, hand it to `claude -p`, and stream the reply back. The bridge holds no intelligence; it is a pipe.

Minimal shape of the bridge:

```python
# pseudocode — the real bridge handles threads, auth, and streaming
def on_message(text, channel):
    result = run(["claude", "-p", text,
                  "--allowedTools", "Read,Grep,mcp__gmail__create_or_update_draft"],
                 cwd="/Users/you/MyOS", capture_output=True, text=True)
    post(channel, result.stdout)
```

Build the chat surface late (Phase 3). The **scheduled-jobs** half of an AI employee — the clock — is already handled by `myos-heartbeat`, so you do not need the bridge to start getting value. A drafted 6 a.m. brief landing in the workspace is useful with no chat surface at all.

---

## 4. MCP integrations — the DMO stack

Connect the tools the employee needs to do the actual work. For a DMO seat that typically means:

- **Google Workspace** (Gmail, Drive, Docs)
- **Calendar**
- **CRM / Asana** (pipeline, partner records, tasks)
- **Meeting transcripts** (the source for follow-ups and recaps)

Add each as an MCP server in Claude Code's config, then **record the full stack in `ME/context-map.md`** so every session and scheduled run knows what is wired and what each tool is for:

```markdown
# ME/context-map.md
## Connected tools (MCP)
- Google Workspace — email + Drive. Drafts only by default.
- Calendar — read for briefs; tentative holds only, never auto-accept.
- Asana — pipeline + partner tasks. Read freely; writes need a named task.
- Transcripts — meeting source for recaps and follow-ups (read-only).
```

The context map is part of the job description. Keep it current; it is how the employee knows its own reach.

---

## 5. Memory — three layers

The employee remembers in three layers. Know which does what:

1. **Contract and briefs** — `CLAUDE.md` and `ME/handbook.md`. Loaded every run. This is policy and standing instruction: who it serves, what good looks like, escalation rules.
2. **Working memory** — Claude Code's built-in session memory plus `ME/memory.md`. Durable facts and decisions the employee should carry forward across runs.
3. **Retrieval** — qmd via `myos-local-search`, searching `workspace`, `transcripts`, `sessions`, and `docs`. This is recall: pulling the relevant past from everything, not just what is open in context.

```bash
qmd collection list          # confirm the four collections resolve
qmd search "partner renewal terms"   # retrieval in action
```

Layer 1 is required reading. Layer 2 is what it learns. Layer 3 is how it finds what it already knew.

---

## 6. Phasing — the order to build in

Do not wire everything on day one. Promote the employee as it earns trust.

**Phase 0 — Manual single-session.** Run `claude` from the workspace root. Do real jobs by hand, interactively. Write and wire the handbook now (`/myos-handbook`) and install retrieval (`/myos-search`). Goal: prove the employee does one job well with a human watching.

**Phase 1 — Heartbeat plus cron.** Add the clock with `/myos-heartbeat`. Start with **one** drafted routine — the 6 a.m. daily brief — on cron:

```bash
crontab -e
# 6 a.m. daily brief, headless, drafts only, logged
0 6 * * * cd /Users/you/MyOS && /usr/local/bin/claude -p "$(cat heartbeat/daily-brief.md)" \
  --allowedTools "Read,Grep,mcp__gmail__create_or_update_draft" \
  >> heartbeat/log/daily-brief.log 2>&1
```

Prove it for a week before adding a second routine.

**Phase 2 — Orchestration for heavy jobs.** Bring in `/myos-orchestrator` for the multi-source jobs (market scans, partner reviews). Subagents dump raw source under `00 Inbox/_work/<job>/`; the orchestrator decides on raw source and never ingests the raw dumps itself.

**Phase 3 — Chat surface plus promotion.** Stand up the thin Slack/iMessage bridge so the employee is reachable in real time. With the brief, retrieval, scheduled routines, and orchestration all proven, promote it from project manager to chief of staff: widen scope, loosen permissions deliberately, and start the parallel org chart for the next hire.

---

## 7. Safety and cost

**Least privilege.** Every run gets exactly the tools its job needs, via `--allowedTools`, and nothing more:

```bash
claude -p "$(cat heartbeat/triage.md)" \
  --allowedTools "Read,Grep,mcp__gmail__create_or_update_draft"
```

**Draft, never send, by default.** Email goes out as drafts the participant approves. Calendar items are tentative holds, not accepts. Relax this only per-routine, only when the routine has proven itself.

**`--dangerously-skip-permissions` is reserved.** Use it only for a proven, isolated setup you fully understand. It is not the default for a 24/7 employee, and never for a routine that can send mail, spend money, or delete anything.

**Cost is real and recurring.** A 24/7 Claude Max plan plus a Mac Mini kept always-on is ongoing spend. If the employee only needs to run on a clock and not hold real-time chat, **Claude Code on the web scheduled triggers** can do the heartbeat half with no Mac Mini and no always-on machine. Choose the Mac Mini build when you genuinely need the chat surface and continuous local presence; choose web triggers when scheduled jobs are all you need.
