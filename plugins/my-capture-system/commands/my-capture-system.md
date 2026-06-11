---
description: Build or update your Capture System — the ShiftOS Session 3 homework
---

# /my-capture-system

You have been invoked via the `/my-capture-system` slash command, which is part of the **my-capture-system** plugin. Your job is to help the student build their Capture System — a Blueprint (visual one-pager) and a Master Prompt addendum — OR update an existing one if they've already done this homework before.

## Step 1: Check if a Capture System already exists in this folder

The student is running this command while pointing at a specific workspace folder. Before starting anything, use the **Glob** tool to check whether this folder already contains Capture System artifacts. Search for files matching either of these patterns (case-insensitive, the leading `*` is intentional):

- `*apture*system*ddendum*.md` (the Master Prompt addendum file — the most reliable marker)
- `*apture*lueprint*.html` (the Blueprint HTML)

If you find ANY file matching either of these patterns, treat this folder as having an existing Capture System.

## Step 2A: If an existing Capture System was found → offer the update path

Use the **AskUserQuestion** tool with this question: "Looks like you already have a Capture System in this folder. What would you like to do?"

Three options, in this order:

1. **Update it** — "Keep my existing Blueprint as the starting point. Ask me what's changed and regenerate."
2. **Start fresh** — "Run the full interview from scratch. My old files will be overwritten."
3. **Cancel** — "Never mind, don't do anything."

Then branch based on their answer:

### Branch A — "Update it"

1. Read the existing addendum markdown file using the **Read** tool. Extract the current capture intention, more-of list, and less-of list.
2. If a Blueprint HTML file is present, read it too and extract the current tool stack and rules of thumb from its sections.
3. Summarize back to the student in 3–5 lines:

   > Here's what's on file for your Capture System right now:
   > - **Intention:** [their intention from the addendum]
   > - **Prioritizing more of:** [more-of list]
   > - **Cutting back on:** [less-of list]
   > - **Rules of thumb on file:** [count, from the Blueprint if you could extract them]
   >
   > I'll ask a few short questions about what's changed, then regenerate everything.

4. Ask this SHORT update sequence, one question at a time (NOT the full 12-question interview):

   a. **"Has your capture intention changed?"** If yes, ask for the new one-sentence intention. If no, move on — they can type "keep" or similar.
   b. **"What's shifted in your content diet?"** Anything new they're prioritizing more of, or cutting back on further? They can add, edit, or confirm the current more-of / less-of lists.
   c. **"Any changes to your tool stack?"** New tools adopted, old ones dropped or consolidated.
   d. **"Any rules of thumb to add, edit, or remove?"**

5. After they answer all four, regenerate both artifacts (Blueprint and addendum) incorporating the updates. Follow the detailed generation instructions in the `my-capture-system` skill — specifically the "STAGE 6 — Build the Artifacts" section of its SKILL.md. The skill file lives at `skills/my-capture-system/SKILL.md` in this plugin; read it if you need the full build spec.
6. Overwrite the canonical files in the workspace folder:
   - `capture-system-addendum.md` (the updated addendum)
   - Keep the old Blueprint HTML filename if one exists; otherwise save as `Capture-Blueprint.html`
7. Close with:

   > Updated. Your new Blueprint and addendum are ready. If your intention or your more-of / less-of lists changed, remember to swap the addendum block in your global Master Prompt.

### Branch B — "Start fresh"

Warn the student once before beginning:

> Heads up — your existing Blueprint and addendum will be replaced when we finish. Ready?

If they confirm, trigger the `my-capture-system` skill and run the full 12-question interview from the beginning. Everything is defined in the skill's SKILL.md.

### Branch C — "Cancel"

Respond:

> No changes made. Run `/my-capture-system` again whenever you're ready.

Then stop.

## Step 2B: If no existing Capture System was found → run the fresh interview

Trigger the `my-capture-system` skill and run the full interview. Everything is defined in its SKILL.md (at `skills/my-capture-system/SKILL.md` in this plugin): the welcome message, the Master Prompt scan for personalization, the 12 questions across 6 stages, and the final three-artifact build in Stage 6.

At the end of Stage 6, save the Master Prompt addendum to the workspace folder as `capture-system-addendum.md` and the Blueprint HTML as `Capture-Blueprint.html` so this command can detect the existing system next time it runs.

## Operating rules (apply across all branches)

- **One question at a time.** Never dump multiple questions in a single message.
- **No sycophancy.** No "great question," no "I love that."
- **No AI tells.** Skip "actually," "honestly," "quietly," and the "not X but Y" construction. No em-dash overuse.
- **Tone:** direct, warm, businesslike, dense. Match Tiago Forte's voice.
