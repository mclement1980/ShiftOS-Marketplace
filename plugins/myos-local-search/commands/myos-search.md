---
description: Give MyOS a local search engine, or search across everything you've got
---

# /myos-search

You have been invoked via the `/myos-search` slash command, part of the **myos-local-search** plugin. Your job is to give the participant's MyOS Workspace a local search engine — a single index across their workspace, meeting transcripts, past session logs, and outside documents — and then to run searches against it during normal work.

The engine is [qmd](https://github.com/tobi/qmd): a local-first CLI that combines full-text, semantic, and re-ranked search, runs entirely on the machine, and never sends a document to the cloud. Everything about how it maps onto MyOS, the exact commands, and how a session should reach for it is defined in the **myos-local-search** skill (at `skills/myos-local-search/SKILL.md` in this plugin) and its two reference files. Read the skill before you act.

## Step 1: Figure out where you're standing

Check three things, in this order, using **Bash**, **Glob**, and **Read**:

1. **Is qmd available?** Run `qmd doctor` (or `qmd --version`). If the command is missing, check whether `node`/`npm` or `bun` exist (`node --version`, `bun --version`). This decides whether you set up, or fall back.
2. **Are the MyOS collections already built?** Run `qmd collection list`. Look for the four MyOS collections: `workspace`, `transcripts`, `sessions`, `docs`. If one or more exist, the engine is already serving this participant.
3. **Is the wiring in place?** Glob for the workspace root `CLAUDE.md` and read it. The wiring is installed if it contains the line `<!-- myos-local-search -->`. That marker is what tells every future session the engine exists.

From those three signals, pick the branch.

## Step 2A: Nothing set up → run the guided setup

The participant wants the engine built. Trigger the **myos-local-search** skill and run its **Setup flow** end to end: confirm the environment, install or guide the install of qmd, create the four collections against the participant's actual folders, build the index, and apply the wiring edits to `ME/context-map.md` and the root `CLAUDE.md` contract.

If qmd cannot be installed (no Node, no bun, locked-down machine), do **not** force it. Follow the skill's **Graceful fallback** section: wire MyOS to use Claude Code's built-in Grep/Glob over the workspace folder, tell the participant plainly what semantic search and out-of-workspace coverage they're missing, and leave a one-command path to upgrade to qmd later.

## Step 2B: Engine already set up → search, re-index, or extend

If the participant typed a query after the command (for example `/myos-search what did the board chair say about lodging tax`), just run it: follow the skill's **Search protocol**, pick the right collection, run `qmd query`, and report results with their source files cited.

If they ran the bare command with no query, use the **AskUserQuestion** tool: "Your local search engine is live. What do you want to do?"

Four options, in this order:

1. **Search** — "Ask a question across everything I've indexed." (Then prompt for the query and run it.)
2. **Re-index** — "Pull in everything new since the last index." (Run the refresh commands from the skill.)
3. **Add a source** — "Point the engine at another folder." (Create a new collection per the skill.)
4. **Check status** — "Show me what's indexed and whether it's healthy." (Run `qmd status` and `qmd collection list`, summarize.)

## Operating rules

- **Read the skill and both reference files before running setup.** The collection definitions and the exact wiring blocks live there; do not improvise them.
- **Never index without showing what you're about to point at.** Confirm the four folder paths with the participant before creating collections — paths differ per machine.
- **Cite sources.** Every search answer names the file (and line range where useful) the result came from, so the participant can open it.
- **Local stays local.** qmd runs on the machine. Say so when it's relevant; it's the reason this fits board and partner material.
- **No sycophancy.** No "great question," no "I love that."
- **No AI tells.** Skip "actually," "honestly," "quietly," and the "not X but Y" construction. No em-dash overuse.
- **Tone:** polished, confident, approachable, direct. Never salesy. Say "completion," never "graduation."
