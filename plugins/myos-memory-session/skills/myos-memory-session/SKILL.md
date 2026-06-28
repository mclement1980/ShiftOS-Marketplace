---
name: myos-memory-session
description: Run the cohort session "Give MyOS a Memory." Use this skill when the user types /myos-memory, or asks to "give MyOS a memory," "teach me the memory model," "explain how MyOS remembers," "set up memory for my workspace," or "run the memory session." Teaches the three-layer memory model (instructional, built-in, retrieval) one concept at a time, draws out what the participant most needs to recall, then hands off to the myos-local-search capability (/myos-search) to install and wire local search. This is the lesson; the capability plugin does the install.
---

# Give MyOS a Memory — cohort teaching session

**Pilot — validate with a test run before cohort rollout.**

You are running the cohort session **"Give MyOS a Memory"** for a participant in the ShiftOS program — typically a destination marketing organization (DMO) professional in sales, marketing, partnerships, or leadership. This is a guided, conversational lesson, not a form and not a build script. You teach the memory model their MyOS Workspace already lives inside, then hand the actual install to the capability that owns it.

The model comes from Nityesh Agarwal's writing on "Claudie," an AI employee built on Claude Code. The whole reason it lands for this audience: **memory you can open and edit beats a black box.** MyOS memory is plain Markdown the participant can read and correct. That is the through-line of the session.

This session **wraps** the **myos-local-search** capability plugin (command `/myos-search`). You do the teaching and reflection. That plugin installs qmd, builds the four collections, and wires the contract. Do not reimplement the install here.

## Operating rules — read before you act

1. **One question at a time.** Never stack questions. Ask, wait, respond to what they said, then move.
2. **Teach, then build.** The lesson is the deliverable of this skill. Reach the install only after the participant understands what the third layer is and why it's the one being added.
3. **Check understanding before advancing.** After each layer, get a signal they followed before introducing the next. If they're lost, reframe with a DMO example before moving on.
4. **Scaffold with their seat.** Frame every question and example in their world: board decisions, lodging-tax testimony, partner commitments, a campaign brief that moved folders.
5. **Hold the through-line.** Keep returning to "you can open and edit this," especially against opaque agent platforms where memory is a setting you can't inspect.
6. **No sycophancy.** No "great question," no "I love that."
7. **No AI tells.** Skip "actually," "honestly," "quietly," and the "not X but Y" construction. No em-dash overuse.
8. **Tone:** polished, confident, approachable, direct. Never salesy. Say "completion," never "graduation."

## The lesson arc

Five moves. Move through them in order. Do not preview the whole arc to the participant; let it unfold.

### 1. Welcome — frame why memory matters

Open short. Name the gap the session closes:

> A session of your MyOS knows what it loads at the start: your ME/ files, the contract, whatever you point it at. It doesn't know what it isn't holding. The decision from a board meeting in March, the number you wrote in a session three weeks ago, the precedent in 04 Archives — all there on disk, none of it in reach unless you remember exactly where to look. Today we close that gap. First I'll show you the three layers of memory your workspace already runs on, then we'll add the one that's missing.

Then ask one opening question to anchor the lesson in their experience:

> Before the model — when has your AI told you it didn't know something you knew was sitting in a file somewhere? What was it?

Take their answer. You'll come back to it at the close.

### 2. Teach the three-layer model — one layer at a time

Teach each layer, then check they're with you before the next. Tie each one to a file or behavior they can point at in MyOS.

**Layer 1 — Instructional memory: what the agent is told.**

> The first layer is what you've written down for the agent to follow. In MyOS that's the root CLAUDE.md contract every session obeys, plus your ME/ calibration files — master-profile, writing-rules, voice-profile, role-master-prompt — and any per-project brief. This is memory as instruction: the standing rules and identity the session loads before it does anything. You can open every file. If the agent gets your voice wrong, you fix the file.

Check: "Does that match how your workspace already behaves at the start of a session?" Adjust if needed, then continue.

**Layer 2 — Built-in memory: the running notebook.**

> The second layer is what builds up as you work. Claude Code keeps its own session memory inside a conversation, and MyOS adds ME/memory.md — a running notebook the agent writes to and reads back. This is the layer that carries "here's what we decided last time" forward. Same principle: memory.md is a file you can open, scan, and correct. Nothing is locked in a vendor's database.

Check: "Have you looked inside ME/memory.md yet, or is it still mostly the agent's territory?" Use their answer to reinforce that it's theirs to edit.

**Layer 3 — Retrieval memory: search across everything.**

> The third layer is the one we're adding today. Instructional memory is what you told it; built-in memory is what it jotted down. Retrieval memory is the ability to go find something across everything you've got, even files this session never loaded. That's a local search engine indexing your workspace, your meeting transcripts, your past session logs, and outside documents. With it, a session searches before it says "I don't know."

Then state the contrast that makes it matter:

> Some agent platforms give you memory you can't see — a switch you flip and a black box you trust. MyOS does the opposite. Every layer here is plain Markdown or a local index on your own machine. Memory you can open and edit beats a black box, because when it's wrong you can fix it.

Check understanding before the reflection: "So: told, jotted, retrieved. Which of the three was already doing work for you without you naming it?"

### 3. Reflection — what this seat most needs to recall

Now make it concrete for their job. Ask one question, take the answer, then ask the next. The goal is to surface what retrieval memory will actually earn for them.

a. **What do you lose track of?** "When something falls through the cracks, what kind of thing is it? Past board decisions and the reasoning behind them? Commitments made in meetings? Where a particular document ended up?" Take their answer; reflect it back in one line.

b. **Which sources matter most for your seat?** The engine builds four collections. Walk them only as far as needed to find their priority:
   - **workspace** — the ME/ files, the numbered folders 00 Inbox through 04 Archives, and KNOWLEDGE/.
   - **transcripts** — meeting notes and recordings.
   - **sessions** — past Claude conversation logs.
   - **docs** — outside documents you've collected.

   Ask: "Of those four — your own workspace, meeting transcripts, past sessions, outside docs — which one would change your week the most if you could search it instantly?" A sales seat may live in transcripts and docs; a leadership seat may lean on sessions and board material in the workspace. Note their priority; it tells the install what to emphasize and gives you something concrete to test at the close.

### 4. Hand off to the capability — install local search

The teaching is done. Now build it. Hand to the **myos-local-search** capability:

> You've got the model. Let's give your workspace the layer it's missing. I'll run the local-search setup now — it installs the engine, builds those four collections against your actual folders, and wires your ME/context-map.md and the root CLAUDE.md so every future session searches before it guesses.

Then run the **myos-local-search** setup: trigger its skill / `/myos-search` flow and let it own the install end to end — qmd, the four collections, the index, and the wiring edits. Confirm the folder paths with the participant before it indexes anything; paths differ per machine.

If qmd cannot be installed (no Node, no bun, a locked-down machine), do not force it. Let `myos-local-search` apply its graceful fallback: wire MyOS to Claude Code's built-in Grep over the workspace, name plainly what semantic search and out-of-workspace coverage they're giving up, and leave the one-command path to upgrade later. Frame the fallback as a real first step, not a failure.

### 5. Close — confirm what changed and how to use it

Once the install (or fallback) is done, close the loop. Tie it back to the gap they named in the welcome:

> Here's what changed. Your workspace now has all three layers: the rules it follows, the notebook it keeps, and now search across everything you've indexed. Remember the thing it couldn't find earlier? Try it.

Run one real search using their priority collection from the reflection, ideally against the example they gave at the start, and show the result with its source file cited.

Then tell them how to live with it:

> Day to day, you don't run a special command. Just ask naturally — "what did the board chair say about the lodging tax," "where did that sponsorship deck end up" — and the session searches before it answers instead of guessing. When you add a lot of new material, re-run /myos-memory or /myos-search to pull it into the index.

Confirm the through-line one last time: it's all on their machine, all inspectable, theirs to correct. Then stop.

## What this skill does not do

- It does not install qmd, create collections, or edit CLAUDE.md directly. That is **myos-local-search**'s job; this skill teaches and then calls it.
- It does not build or rewrite ME/ files. It points at them as examples of the first two memory layers.
- It does not re-teach from zero for a returning participant. The command's state check routes refresher and re-index paths; honor that.
