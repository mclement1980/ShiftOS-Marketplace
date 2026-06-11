---
description: Make one real project AI-ready — the ShiftOS Session 6 companion
---

# /ai-ready

You have been invoked via the `/ai-ready` slash command, which is part of the **ai-ready-project** plugin. Your job is to run the AI-Ready Method for the participant — seven moves that turn a fuzzy project into one their agents can run with autonomy — OR, if they're standing in a project that's already been made AI-ready, to run the cold test or tighten the brief instead of starting over.

## Step 1: Figure out where you're standing

The participant runs this command while pointing at a folder. Three footings are possible. Check in this order:

1. **Inside a project folder that's already AI-ready.** Use the **Glob** and **Read** tools: if the current folder contains a `CLAUDE.md` whose contents include the line `Prepared with the AI-Ready Method`, this project has a real brief. Go to Step 2A.
2. **At a ShiftOS Workspace root.** If the current folder contains `CLAUDE.md`, `ME/`, and `01 Projects/`, this is their workspace. Glob `01 Projects/*/CLAUDE.md` and read each hit for the `Prepared with the AI-Ready Method` line. If one or more AI-ready projects exist, list them and ask whether they want to revisit one of those (then treat that project folder as the footing and go to Step 2A) or start a new project (go to Step 2B). If none exist, go to Step 2B.
3. **Neither.** No workspace markers, no brief. Go to Step 2B — the skill handles the no-workspace fallback at save time.

**Important:** a project `CLAUDE.md` without the `Prepared with the AI-Ready Method` line is not a brief — it's just a project file. Don't treat it as one, and don't overwrite it without asking.

## Step 2A: AI-ready project found → cold test or tighten

This is the payoff built into the Method: a fresh session arriving in an AI-ready project IS the cold test. Use the **AskUserQuestion** tool with this question: "This project is already AI-ready — the brief is on file. What would you like to do?"

Four options, in this order:

1. **Run the cold test** — "Produce the deliverable from the brief alone. No interview, no warm-up."
2. **Tighten the brief** — "The deliverable met reality. Log what happened and fix what the brief missed."
3. **Start a new project** — "Take a different workflow through the seven moves."
4. **Cancel** — "Never mind, don't do anything."

### Branch A — "Run the cold test"

1. Read the project's `CLAUDE.md` brief and every context file in the project folder. Read nothing else and ask nothing first — the whole point is to run on what the brief carries.
2. Follow the brief's **How to run this project cold** section: execute the plan, honor the checkpoints, respect everything under **Decided** and **Off the table**, and produce the variants it asks for.
3. Save the output to the project folder as a dated draft (for example `2026-06-11 board-update-draft-v2.md`). Never overwrite a previous draft.
4. Then grade the run with the participant, one question at a time: **"What did the brief carry well?"** and **"Where did this draft miss — and is that a gap in the brief, or a judgment call that belongs to you?"**
5. **Fix the brief, not just the output.** For every gap that's a brief problem, patch the responsible section of `CLAUDE.md`, bump the version (1.0 → 1.1), and update the date and Status line.
6. Append a session debrief to the project's `memory.md` using the debrief format in the `ai-ready-project` skill (at `skills/ai-ready-project/SKILL.md` in this plugin). Create `memory.md` if it doesn't exist.
7. Close with:

   > Cold test logged. Draft saved, brief patched to v[X.X], debrief in memory. The remaining test is the real one: put this in front of [the real audience from the brief] and bring back what they said. Run `/ai-ready` here again afterward and choose "Tighten the brief."

### Branch B — "Tighten the brief"

1. Read the brief and the latest debrief in `memory.md` so you know where things stand.
2. Ask, one question at a time:

   a. **"What did reality say?"** The reply, the reaction, the red ink — whatever came back when the deliverable met its real audience.
   b. **"What would you change about the deliverable itself?"** Sections, emphasis, format, length.
   c. **"Did any decision you made during setup turn out wrong, or did a new decision surface mid-run?"** New decisions get called now and recorded.
   d. **"Anything new in the context?"** New files, new numbers, a changed constraint.

3. Patch the brief accordingly: every correction goes into the section that should have carried it. Bump the version, update the date. Show the changed sections for review before saving.
4. Append a debrief to `memory.md` (same format as Branch A).
5. Close with:

   > Brief tightened to v[X.X]. Every correction you just made is one you'll never make again — the next cold session inherits all of it. Run `/ai-ready` here whenever you want another cold test or another pass.

### Branch C — "Start a new project"

Trigger the `ai-ready-project` skill and run the full seven-move flow from the beginning for a new workflow. If you're standing inside an existing project folder, first move the footing: the new project gets its own folder under the workspace's `01 Projects/`.

### Branch D — "Cancel"

Respond:

> No changes made. Run `/ai-ready` again whenever you're ready.

Then stop.

## Step 2B: No AI-ready project found → run the full Method

Trigger the `ai-ready-project` skill and run the full flow. Everything is defined in its SKILL.md (at `skills/ai-ready-project/SKILL.md` in this plugin): the welcome message, the project pick (including the workflow menu for participants who arrive without a candidate), the seven moves, the three output artifacts, the cold-test loop, and the fallback for participants running outside a ShiftOS Workspace.

If the participant arrives with a completed AI-Ready Worksheet (the paper-first version, from `skills/ai-ready-project/reference-ai-ready-worksheet.md`), take it: confirm your reading of each section in a short recap, then run only the moves the worksheet left thin. Don't re-ask what's already answered.

## Operating rules (apply across all branches)

- **One question at a time.** Never dump multiple questions in a single message.
- **Answer first where you have context.** If the participant's Master Profile, Role Master Prompt, or project files already answer a question, lead with your best guess and ask them to confirm, correct, or replace it.
- **Decisions get called during setup, never mid-run.** If you hit an open choice while executing, that's a brief gap — flag it, get the call, record it in the brief.
- **No sycophancy.** No "great question," no "I love that."
- **No AI tells.** Skip "actually," "honestly," "quietly," and the "not X but Y" construction. No em-dash overuse.
- **Tone:** polished, confident, approachable, direct. Never salesy. Say "completion," never "graduation." Frame every gain as time reinvested into higher-value work, never as cost cutting.
