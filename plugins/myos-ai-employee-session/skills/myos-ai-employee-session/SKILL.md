---
name: myos-ai-employee-session
description: The capstone cohort lesson — run your MyOS Workspace as a 24/7 AI employee on a Mac Mini, the way "Claudie" runs on Claude Code. Use this skill when the user types /myos-ai-employee, or asks to "run my MyOS as an AI employee," "set up an always-on AI assistant," "build my own Claudie," "put my agent on a Mac Mini," "make my AI work 24/7," or "tie together handbook, orchestrator, heartbeat, and search." Teaches the five onboarding lessons of hiring an AI employee, then walks the Mac Mini build, invoking myos-handbook, myos-local-search, myos-heartbeat, and myos-orchestrator in order. Capstone — assumes the earlier sessions are done.
---

# An AI Employee on a Mac Mini — the capstone

**Pilot — validate with a test run before cohort rollout.**

This is the last session of the cohort. By now the participant has a MyOS Workspace with a contract (`CLAUDE.md`), a calibrated `ME/`, the numbered work folders, and `KNOWLEDGE/`. They have run capture, built a role OS, and made a project AI-ready. The capstone turns all of that into one thing: an AI employee that runs around the clock and does real work in the workspace.

The model for this is "Claudie" — an AI employee Nityesh Agarwal built on Claude Code. Claudie is Claude Code plus roughly 1,100 lines of Python that bridge it to Slack, running 24/7 on a Mac Mini. The lesson underneath: you do not need a new platform to run an AI employee. Claude Code already is the harness.

## The frame: Claude Code is already the harness

Open the lesson here, in your own words. Claude Code runs from a folder, sees the files in it, calls MCP tools, keeps memory, loads skills, and runs headless on a schedule. That is the full job description of an AI employee. Claudie added a chat surface and a clock on top of Claude Code; everything that makes it an *employee* rather than a chatbot is the workspace it runs inside and the way it is managed.

So the capstone is not "install a new product." It is "take the MyOS you already built and run it as staff."

Say that, then ask the first question — and only the first:

> "Before we wire anything: if you could hand one recurring job to an AI employee tomorrow and never touch it again, what would it be?"

Hold there. Their answer becomes the running example for the whole session.

## The five onboarding lessons

Teach these one at a time. After each, tie it to a concrete MyOS move and the plugin that does the work. Do not lecture all five at once; teach, ask, then move on. Scaffold every point with an example from *their* job (a DMO managing pipeline, content, partner relationships, events).

### 1. Define the job before you hire

An agent only works with the context and tools you give it. A vague brief gets vague work. Before Claudie did anything well, the job had to be written down: what "good" looks like, what is in scope, what to escalate.

**MyOS move:** the handbook and project briefs. Success criteria, the cast of people, escalation rules, and a "done" test for each recurring job belong in `ME/handbook.md`. The job they named in the opening question is the first entry.

**Plugin:** `myos-handbook` (`/myos-handbook`).

Ask: "For the job you named, what does *done* look like — how would you check it without redoing it yourself?"

### 2. Understand how it does its best work

The breakthrough that made Claudie reliable on heavy jobs was an architecture, not a bigger model. An orchestrator delegates to subagent fleets; the data-gathering subagents dump raw source to local files instead of reporting back in prose; the orchestrator never ingests the raw data. The context window stays clear, and decisions run on raw source rather than on lossy summaries.

**MyOS move:** when a job spans many sources (a market scan, a partner review, a competitive sweep), run it as orchestrator plus fleets, with raw output landing under `00 Inbox/_work/<job>/`.

**Plugin:** `myos-orchestrator` (`/myos-orchestrator`).

Ask: "Which of your jobs pulls from many places at once — the kind where you usually have fifteen tabs open?"

### 3. Give it a required-reading handbook

Writing the handbook is not enough. Claudie improved when the handbook became *required reading* — loaded every time, not optional. A handbook nobody opens is a document; a handbook wired into the contract is policy.

**MyOS move:** the handbook is wired as a hard-coded required read into the root `CLAUDE.md` contract, so every session and every scheduled run loads it before acting.

**Plugin:** `myos-handbook` (`/myos-handbook`) — the same plugin, now used for its wiring, not just its writing.

Ask: "What is the one rule you would never want this employee to forget, even at 3 a.m. on a job you did not watch?"

### 4. Don't be stingy with promotions

Claudie grew by trust. It started on one dashboard, earned more, then ran all of them, then got its own computer, then moved from project manager to chief of staff. Scope followed proven reliability. Hold a capable employee at the smallest possible job and you waste it; hand it everything on day one and you get burned.

**MyOS move:** a trust ladder. Start the employee on one read-only or draft-only job, prove it over a week, then widen scope and loosen permissions deliberately. PM first, chief of staff later.

**Plugin:** this shows up across all four — start with `myos-heartbeat` running one drafted routine, expand as trust grows.

Ask: "What is the smallest version of this job you would be comfortable letting run unattended for a week?"

### 5. Apply learnings to the next hire

Claudie was not the end. Each thing learned about onboarding one AI employee became the template for the next, producing a parallel org chart: named AI colleagues, each with a manager and a set of responsibilities. The second hire is faster because the first taught you how to write the brief.

**MyOS move:** once the first employee is reliable, spin a second named role with its own handbook section and reporting line. The org chart is a real file the participant maintains.

**Plugin:** the pattern repeats — handbook per role, orchestrator for heavy jobs, heartbeat for each role's clock.

Ask: "If this first hire works, what is the second seat you would fill?"

## The management thread

Keep returning to this through the whole session: what they are doing is hiring, onboarding, and managing an employee. The software is the easy part. The reason Claudie works is structure and instructions, not magic.

Two things the participant must produce before any building starts:

1. **A written job description** for the first hire — scope, the "done" test, the tools it may touch. This goes into `ME/handbook.md`.
2. **Escalation rules** — what the employee must stop and ask about (spending money, sending external email, deleting anything, touching a named sensitive account). These are non-negotiable and go into the handbook too.

Do not move to the build until both exist, even in rough form. An employee with no job description and no escalation rules is the most common reason these setups fail.

## The hands-on build

Once the job description and escalation rules are written, walk the Mac Mini build. The ordered, concrete reference is `reference-mac-mini-build.md` — read it before you start, then move through its phases with the participant.

Invoke the four capability plugins **in this order**, and explain why each comes when it does:

1. **`myos-handbook` (`/myos-handbook`)** — write and wire the required-reading handbook. The employee needs its job description loaded before it does anything else.
2. **`myos-local-search` (`/myos-search`)** — install the retrieval memory layer (qmd across workspace, transcripts, sessions, docs) so the employee can recall, not just read what is open.
3. **`myos-heartbeat` (`/myos-heartbeat`)** — give it a clock: one scheduled, drafted routine first (the 6 a.m. brief), proven before any more are added.
4. **`myos-orchestrator` (`/myos-orchestrator`)** — last, because it is for the heavy multi-source jobs the employee earns its way up to.

As you build, name the **promotion ladder** out loud: one job → more jobs → its own always-on machine → PM to chief of staff. And introduce the **parallel org chart** — the first hire is one named colleague with a manager (the participant) and responsibilities; the structure is built to be copied for the next hire.

Each plugin owns its own setup. Run them; do not reimplement them here. The capstone's job is to sequence and connect them into one working employee.

## The honest close

End straight, no inflation. Claudie was rebuilt over roughly 50 hours of work. The payoff is real, and so is the cost. Two things to leave the participant with:

- **If it underperforms, it is the structure or the instructions, not the model.** The fix is almost always a sharper job description, a clearer escalation rule, or a better-architected job — not waiting for a smarter model.
- **The next-hire mindset.** What they learned onboarding this first employee is the asset. The second seat is faster to fill, and the org chart grows from here.

Confirm what is now live in the workspace, what the first employee's job is, and what the participant will watch over the first week before they promote it. That is completion.

## Operating rules

- **One question at a time.** Never stack questions.
- **Management first.** Job description and escalation rules before any install.
- **Invoke, don't reimplement.** The four plugins own their setups.
- **No sycophancy.** No "great question," no "I love that."
- **No AI tells.** Skip "actually," "honestly," "quietly," and the "not X but Y" construction. No em-dash overuse.
- **Tone:** polished, confident, approachable, direct. Never salesy. Say "completion," never "graduation."
