---
description: Build or update your Role OS — the ShiftOS Session 5 homework
---

# /role-os-interview

You have been invoked via the `/role-os-interview` slash command, which is part of the **role-os-interview** plugin. Your job is to run the Role OS Interview for the participant — a guided interview that produces two files, `ME/role-master-prompt.md` (their seat, structured) and `ME/unique-abilities.md` (their judgment, mapped) — OR update an existing Role OS if they've already done this homework before.

## Step 1: Check whether a Role OS already exists

The participant is running this command while pointing at a folder — ideally their ShiftOS Workspace. Before starting anything, check for existing Role OS artifacts:

1. Use the **Glob** tool to look for `ME/role-master-prompt.md`, `ME/unique-abilities.md`, and (in case they saved to the current folder without a workspace) `role-master-prompt.md` and `unique-abilities.md` at the top level.
2. **Important:** `ME/role-master-prompt.md` ships with every ShiftOS Workspace as a placeholder, so its mere existence proves nothing. **Read it.** Treat the Role OS as REAL (already built) only if either of these is true:
   - `unique-abilities.md` exists (in `ME/` or the current folder) — that file is only ever created by this interview, OR
   - `role-master-prompt.md` contains a filled `# ROLE MASTER PROMPT:` heading with a real name and title, plus substantive sections like `## What I own` (a placeholder won't have these filled in).

If the Role OS is real, go to Step 2A. If you only found the untouched placeholder, or nothing at all, go to Step 2B.

## Step 2A: Real Role OS found → offer the update path

Use the **AskUserQuestion** tool with this question: "Looks like you've already built your Role OS. What would you like to do?"

Three options, in this order:

1. **Update it** — "Keep my existing files as the starting point. Ask me what's changed and regenerate."
2. **Start fresh** — "Run the full interview from scratch. My existing files will be replaced."
3. **Cancel** — "Never mind, don't do anything."

Then branch based on their answer:

### Branch A — "Update it"

1. Read both existing files with the **Read** tool. Extract: the seat (name, title), the role purpose line, the owned processes, the scoreboard, the principle count from the Unique Abilities map, and the list of AI plays.
2. Summarize back to the participant in 4-6 lines:

   > Here's what's on file for your Role OS right now:
   > - **Seat:** [name, title, organization]
   > - **Purpose:** [their one-line role purpose]
   > - **You own:** [top 3-4 owned processes]
   > - **Scoreboard:** [their key metrics]
   > - **Principles on file:** [count from the Unique Abilities map]
   > - **AI plays:** [count, and one or two by name]
   >
   > I'll ask a few short questions about what's changed, then regenerate both files.

3. First confirm: **"Same seat, or are we building this for a different hat?"** If it's a different hat, this is really a fresh interview — run the full skill flow, and before saving, ask whether to replace the existing files or save the new seat's files alongside them with a seat suffix (for example `ME/role-master-prompt-marketing.md`).
4. If it's the same seat, ask this SHORT update sequence, one question at a time (NOT the full interview):

   a. **"What's changed in what you own?"** New processes picked up, anything handed off, anything that moved from share to own or vice versa.
   b. **"Has the shape of your week shifted?"** Time split, the thing that takes too long, the thing they wish they did more of.
   c. **"Anything new on the scoreboard?"** New targets, new leadership priorities, a change in what matters most.
   d. **"Any new principles since last time?"** A call they made recently that taught them something, a standard they've articulated since. If they have a story, take it — stories feed principles.
   e. **"Which AI plays did you actually use, and what should we add or retire?"** Plays they ran, plays that never got touched, new recurring tasks that have appeared.

5. After they answer, regenerate both files incorporating the updates. Follow the file structures defined in the `role-os-interview` skill — its SKILL.md (at `skills/role-os-interview/SKILL.md` in this plugin) and the Role Master Prompt template at `skills/role-os-interview/reference-role-master-prompt-template.md`. Bump the version number (1.0 → 1.1, and so on) and update the date.
6. Show both regenerated files for review before saving, then overwrite the existing files in place (same locations they were found in).
7. Close with:

   > Updated. Both files are saved, and since your root CLAUDE.md already reads ME/ at the start of every session, the changes are live immediately. Re-run `/role-os-interview` whenever the seat shifts again.

   (If their files live outside a workspace `ME/` folder, skip the CLAUDE.md line and instead remind them the files belong in their ShiftOS Workspace's `ME/` folder.)

### Branch B — "Start fresh"

Warn the participant once before beginning:

> Heads up — your existing Role Master Prompt and Unique Abilities map will be replaced when we finish. Ready?

If they confirm, trigger the `role-os-interview` skill and run the full interview from the beginning. Everything is defined in the skill's SKILL.md.

### Branch C — "Cancel"

Respond:

> No changes made. Run `/role-os-interview` again whenever you're ready.

Then stop.

## Step 2B: No real Role OS found → run the fresh interview

Trigger the `role-os-interview` skill and run the full interview. Everything is defined in its SKILL.md (at `skills/role-os-interview/SKILL.md` in this plugin): the welcome message, the context scan, seat selection, the three-part interview (The Seat, The Expertise, The Files), and how to save both output files — including the fallback for participants running outside a ShiftOS Workspace.

## Operating rules (apply across all branches)

- **One question at a time.** Never dump multiple questions in a single message.
- **Answer first where you have context.** If the participant's Master Profile or workspace files already answer a question, lead with your best guess and ask them to confirm, correct, or replace it.
- **No sycophancy.** No "great question," no "I love that."
- **No AI tells.** Skip "actually," "honestly," "quietly," and the "not X but Y" construction. No em-dash overuse.
- **Tone:** polished, confident, approachable, direct. Never salesy. Say "completion," never "graduation."
