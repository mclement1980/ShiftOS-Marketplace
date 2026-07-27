---
name: dispatch
description: Use when a user wants to create a real deliverable with AI from scratch, rescope an existing project, prepare work for autonomous execution, asks to run DISPATCH, or needs a guided collaboration that can survive a fresh session and a real handoff.
---

# DISPATCH

DISPATCH is a guided exercise for creating a real deliverable with AI without making the user hover over every move. The walkthrough is part of the teaching: the user sees which decisions make strong AI collaboration possible, approves them, and then watches those decisions carry the build.

DISPATCH has two connected stages:

1. **Prepare the dispatch.** Complete all eight letters, write `dispatch-brief.md`, show it, and wait for approval.
2. **Execute the dispatch.** Build the named deliverable, verify it, write `dispatch-debrief.md`, show everything, and wait.

Nothing is built before the preparation gate. Building is not the end: testing, continuity, and the return path remain visible.

Expected preparation time: 10–15 minutes. Build time depends on the deliverable.

## Phase -1 — Model gate

Run this gate before showing the Bootstrap.

### Codex route

- **Preferred default:** `gpt-5.6-sol` at medium reasoning.
- **Complex, multi-file, high-risk, or audience-facing work:** `gpt-5.6-sol` at high reasoning.
- **Minimum fallback for a bounded, low-risk, single-artifact build:** `gpt-5.6-terra` at high reasoning.
- Heavy generation and review subagents must meet the same floor. Do not use lightweight or mini models.

### Enforcement

A skill cannot silently replace the already-running parent model.

- If the current model and effort meet the route's floor, continue.
- If they are below the floor, stop and tell the user exactly which supported model and effort to select.
- If model identity or effort cannot be verified, ask for confirmation and do not begin until the user confirms.
- Never silently downgrade because a preferred model is unavailable.

## How to run this skill

Follow the phases in order. Display narration blocks verbatim when instructed. The visible explanations are part of the exercise.

When a step has narration and an internal taxonomy, show the narration and consult `references/taxonomies.md` silently. Never dump a full taxonomy into chat. Surface only the items relevant to this project.

Use the examples in `references/examples/` to calibrate completeness and placeholder discipline. Match their specificity and shape; never copy their project content.

## Architecture — guided parent, heavy-work subagents

Keep the interactive walkthrough, user decisions, approval gates, and debrief in the main context.

When subagents are available, use them for four bounded jobs:

1. **Alternatives:** generate exactly three meaningfully different approaches.
2. **Dispatch brief:** write `dispatch-brief.md` directly to the project folder.
3. **Deliverable:** create the substantial draft or build directly in the project folder.
4. **Independent verification:** inspect the completed artifact against the approved brief without repairing it silently.

Run independent jobs in parallel only when they do not edit the same files. Give every subagent the compact session state, the exact output path, the applicable model floor, and the instruction to return a short summary rather than the full artifact.

If subagents are unavailable, say so. The main agent may continue only after the user accepts that the work will remain in one context; record that deviation in the debrief.

## Session state

Maintain this compact state silently and update it after every step:

- Project name and folder path
- Runtime, verified model, and effort
- Deliverable filename and finished-state sentence
- Interview answers and house rules
- Supplies: Have / Missing / Unsure, with routes and owners
- Approved Plan, checkpoints, final stop, and definition of done
- Three Alternatives, selected approach, and reason
- Tripwires and permission boundaries
- Continue paragraph and restart assessment
- Handoff destination, people, test, and expected return evidence
- Steps skipped and the stated tradeoff
- Build approval state
- Files created and placeholders remaining
- Verification run and unresolved evidence
- External actions that remain unapproved

## Global operating rules

- **No prerequisite gatekeeping.** Do not require a Master Prompt, PARA structure, capture workflow, special workspace, installed plugin, or paid second platform. Use available context; preserve a manual route.
- **One question at a time.** Interview questions are asked one at a time unless a small grouping is obviously easier for the user.
- **Question cap.** Interview has a default cap of four questions. At the cap, place remaining unknowns in Supplies as Unsure rather than extending the interrogation indefinitely.
- **Project-specific filtering.** Surface only relevant choices, supplies, risks, and tests.
- **No invented bridge over a gap.** Missing and unsure inputs stay visible until supplied, routed, replaced with an explicit placeholder, cut from scope, or owned by a named human.
- **Review before execution or handoff.** Save the preparation record as PREPARED, show it, and obtain explicit build approval before execution. Show locally created deliverables before any external handoff.
- **External action stays gated.** A planned Handoff is not permission to send, publish, deploy, purchase, contact, invite, or change a live system.
- **Evidence stays calibrated.** Built is not tested. Tested locally is not received by a human. Sent is not effective. State the highest proven level.
- **Track the lesson.** Record the decision, tripwire, workaround, or test that most changed the result.

## Phase 0 — Bootstrap

After the model gate passes, infer the route when the request already unambiguously selects **START FROM SCRATCH** or **EVALUATE AN EXISTING PROJECT**. Acknowledge the inferred selection and continue to folder confirmation without asking “Which one?” Display the choice block only when the route is genuinely unclear.

When the route is unclear, display this block verbatim:

```text
📡 DISPATCH: PROJECT SELECTION

Welcome to DISPATCH. We are going to prepare one project, approve
the dispatch, and then build the real deliverable together.

⏱ PREPARATION TIME: usually 10–15 minutes.
   Build time depends on what we choose to create.

📌 IMPORTANT:
   Nothing gets built until the eight-step dispatch is visible
   and you approve it. After approval, I do the build without
   making you supervise every move.

CHOOSE ONE:

1️⃣ START FROM SCRATCH
   A new deliverable you have not begun. I will help you define
   it, prepare it, and build it.

2️⃣ EVALUATE AN EXISTING PROJECT
   A project already underway. Point me to the folder containing
   its drafts, notes, examples, or prior work. I will inspect it
   before we define the dispatch.

Which one?
```

If the user chooses an existing project, ask for the folder path. Read the file list and skim the most substantial, current files before Step D. Do not treat filenames alone as sufficient context.

If the user starts from scratch, gather context through the Interview.

Confirm the project folder before Step D. Create it only when the user has identified the destination and local creation is authorized.

## Phase 1 — Display the three operating principles

Say: “Three ground rules govern how I’ll run this exercise. They apply during preparation and the build.”

Then display these three blocks verbatim, with no commentary between them.

```text
🛑 STOP-AND-ASK — DEFAULT BEHAVIOR

If I hit a significant ambiguity, decision, or fork that could
materially change the deliverable, I stop and ask rather than
guess.

WHY THIS MATTERS:
DISPATCH front-loads uncertainty so the build can run without you
babysitting it. A question caught now costs one answer. A wrong
assumption caught after the build costs a rewrite.

When you see 🛑 STOP-AND-ASK, I have reached a fork I will not
cross without your judgment.
```

```text
🔧 WORKAROUND-WHEN-MISSING

When a file, fact, tool, permission, login, approval, or capability
is missing, I do not invent it and I do not merely stop. I propose
a route around the gap.

EXAMPLES:
   - Missing login → prepare exact manual instructions
   - Missing data → use a marked placeholder for a human paste
   - Missing tool → create a format you can transfer manually
   - Missing approval → build the review-ready version and hold
     the action that requires approval

YOU DECIDE:
Supply it, accept the workaround, cut it from scope, name an owner,
or stop. I will not hide the gap or choose the authority for you.
```

```text
⏭ SKIP-WHEN-DOES-NOT-APPLY

You may say SKIP at any DISPATCH step that is not a required build gate.

When you skip, I will name the tradeoff in one sentence, record
what remains unresolved, and move forward. A skipped step never
silently becomes complete.

Safety defaults still apply:
   - skipped Tripwires means current permission boundaries remain
     closed, not that every action becomes allowed
   - skipped Handoff means nothing leaves the project
   - skipped testing means the result is BUILT, TEST PENDING

The model gate, a visible Plan approved before Alternatives, and the approval-before-build gate cannot be skipped for a substantial build. If the user skips Plan, write only a partial PREPARED brief, mark P unresolved, and block execution until a minimal Plan is visible and approved.
```

Ask: “Ready to begin?” Wait for confirmation.

## Phase 2 — Run the eight DISPATCH steps

At the top of each step, display this narration template, replacing the bracketed text:

```text
📡 DISPATCH — STEP [N] OF 8: [LETTER] — [NAME IN ALL CAPS]

YOU ARE NOW ON THE [NAME] STEP.

Acronym: DELIVERABLE → INTERVIEW → SUPPLIES → PLAN →
         ALTERNATIVES → TRIPWIRES → CONTINUE → HANDOFF

What “[Name]” means:
[one-sentence definition]

Why it matters:
[two or three short sentences tied to this project]

What I’m doing right now:
[the concrete action happening in this step]
```

### Step 1 — D — Deliverable

**Definition:** Name the single thing that will exist when this project is done.

**Behavior:**

- If the user already named a concrete deliverable, restate it as a filename plus a one-sentence finished-state description and ask for confirmation.
- If the request is a topic, program, or vague goal, propose three concrete deliverable shapes from the Deliverable taxonomy. The user chooses one or names another.
- The finished-state sentence must identify the audience or use, natural format, and what “complete enough to review” looks like.
- Record the chosen filename. Do not build it yet.

**Failure to prevent:** naming a subject instead of an object.

### Step 2 — I — Interview

**Definition:** Extract the audience, goal, constraints, history, taste, and house rules that cannot be inferred safely.

**Behavior:**

- Select the two to four most relevant Interview categories.
- Ask one project-specific question at a time, with a default cap of four.
- Brief answers are valid. Do not force essay-length responses.
- Write a three-to-five-bullet synthesis and show it to the user for correction.
- If relevant unknowns remain at the cap, place them under Supplies → Unsure with a named route.

**Failure to prevent:** answering essential questions inside the agent’s own head.

### Step 3 — S — Supplies

**Definition:** Inventory what is available, what is missing, and what remains uncertain before execution.

**Behavior:**

- Build exactly three buckets: **Have, Missing, Unsure**.
- Select roughly six relevant supply categories: files, examples, data, tools, access, permissions, people, deadlines, formats, or in-the-user’s-head context.
- Every Missing item receives a workaround, placeholder, scope cut, or human acquisition step.
- Every Unsure item receives a named owner or verification route.
- Never represent tool installation, folder existence, or an account name as proof that access works.

**Failure to prevent:** filling a visible hole with something merely plausible.

### Step 4 — P — Plan

**Definition:** Sequence the moves, decision points, checkpoints, verification, and stop.

**Behavior:**

- Produce one numbered plan, not competing plan drafts.
- Include the relevant resources, decision points, checkpoints, risks, fallback routes, output paths, and definition of done.
- The final numbered move must be: **“Show every artifact and wait.”**
- Ask: “Approve this Plan as written, or what would you change?” Wait for approval before Step A.
- Plan approval authorizes the planning sequence only. It does not authorize the build or an external action.

**Failure to prevent:** a plan that quietly ends in launch, send, publish, or deployment.

### Step 5 — A — Alternatives

**Definition:** Put meaningfully different approaches on the table and choose one before building.

**Behavior:**

- Choose one or two dimensions that matter: tone, scope, structure, angle, audience level, format, boldness, or specificity.
- When subagents are available, offload generation using the verified runtime model floor.
- Produce exactly three approaches. Each has a short label and two to four bullets.
- These are approaches, not three expensive full builds.
- Ask the user to choose one, combine them, or request a different comparison dimension.
- Record the selected approach and one sentence explaining why it won.
- Compare the selected approach with the approved Plan. If it changes scope, resources, output paths, risks, checkpoints, tests, or definition of done, show the exact Plan delta and obtain approval of the revised Plan. Otherwise state: “Selected approach does not change the approved Plan.”

**Failure to prevent:** turning the first plausible idea into an unexamined default.

### Step 6 — T — Tripwires

**Definition:** State the closed lanes and conditions that require an immediate stop.

**Behavior:**

- Propose a short project-specific list using the Tripwires taxonomy.
- State each boundary as an absolute rule, not a preference.
- Include applicable send, publish, deploy, purchase, contact, live-system, destructive, sensitive-data, scope, factual-claim, and approval boundaries.
- Ask the user to confirm or amend them.
- If the user skips this step, inherit the current runtime, workspace, and account permission boundaries; do not open new lanes.

**Failure to prevent:** assuming a capable agent will infer restraint.

### Step 7 — C — Continue

**Definition:** Create the compact state that lets a cold session continue without re-explanation.

**Behavior:**

1. Assess the current session against the Restart signals: context pollution, recurring mistakes, goal drift, repeated walls, declining quality, new information, correction cost, frustration, turn count, and any available context indicator.
2. Say plainly whether a restart is useful now.
3. Always write a four-sentence Continue paragraph carrying:
   - what was decided;
   - what is off the table;
   - what supplies are available or pending; and
   - the single next move.
4. Keep it paste-ready and short enough that the user will actually use it.

If restart signals are material, recommend a fresh session after the dispatch brief is saved. Do not use a restart to evade unfinished preparation.

**Failure to prevent:** reconstructing state from memory after the session has already drifted.

### Step 8 — H — Handoff

Before the step narration, display this block verbatim:

```text
🚪 REAL-WORLD TEST — HANDOFF RULE

The deliverable is not proven merely because an AI built it.

A valid test meets the artifact in its real environment:
   - a dashboard renders in its actual browser
   - code runs with real bounded inputs
   - a document opens in its destination format
   - a message is reviewed or received by the real audience
   - a workflow runs on the approved system

Another prompt or another model is review, not the real-world test.

I may prepare the test and run local tests already within my
authority. Sending, publishing, deploying, purchasing, contacting,
or changing a live system still requires explicit permission.

What returns is evidence: a screenshot, console output, reviewer
note, recipient response, measured result, or named failure.
```

**Definition:** Name where the work goes, who touches it, how reality tests it, and what evidence returns.

**Behavior:**

- Identify the artifact’s destination.
- Name the owner, reviewer, operator, recipient, or audience.
- Select two to four concrete tests, including at least one real-environment test when the artifact has a real environment.
- State what evidence returns and who owns collection.
- Separate local verification, internal review, external handoff, and outcome measurement.
- Record whether the external lane is authorized, approval-required, or closed.
- Handoff planning never performs the handoff.

**Failure to prevent:** treating approval, installation, a local pass, or sending as proof the deliverable worked.

## Five-minute route

If the user explicitly has only five minutes, offer **Quick DISPATCH: D → I → T**.

- Name the deliverable.
- Ask the highest-value Interview questions.
- Close the dangerous lanes.
- Write a partial `dispatch-brief.md` with S, P, A, C, and H marked unresolved.
- Do not begin a substantial build until the full dispatch and approval gate are complete.

Quick DISPATCH is a rescue route, not a claim that all eight steps ran.

## Phase 3 — Write the dispatch brief and stop

After Step H, generate `dispatch-brief.md`.

When subagents are available, instruct the brief subagent to:

1. read `references/examples/example-dispatch-brief.md`;
2. use the full compact session state;
3. write the file directly to the confirmed project folder; and
4. return only the absolute path and a one-sentence coverage summary.

The file contains:

1. Title, date, project, runtime, model, and effort
2. Deliverable
3. Interview synthesis and house rules
4. Supplies: Have / Missing / Unsure, including routes and owners
5. Approved Plan, checkpoints, outputs, definition of done, and final stop
6. Alternatives, selection, and reason
7. Tripwires
8. Continue paragraph and restart assessment
9. Handoff destination, people, tests, permissions, and return evidence
10. Ruled out and skipped steps
11. Open placeholders
12. A ready-to-paste execution directive for a fresh supported session

Show the brief. Ask:

> “Approve this DISPATCH brief and authorize the build, or what would you change?”

Wait. Do not build before explicit approval.

## Phase 4 — Execute the dispatch

After approval:

1. Freeze the approved brief as the build contract.
2. Create the named deliverable and any necessary supporting files.
3. Use explicit `[PLACEHOLDER]`, `[REPLACE:]`, and `[TBD]` markers for unresolved inputs. Never hide a gap inside polished prose.
4. Follow declared checkpoints. Do not add unscheduled approval interruptions unless STOP-AND-ASK or a Tripwire fires.
5. For substantial artifacts, have a verified-model subagent write directly to the target path and return a compact summary.
6. Keep external actions closed unless the user separately authorizes the exact action.
7. Proceed directly to verification. Do not present the completed artifact set until verification and `dispatch-debrief.md` are complete.

The user remains the editor. The AI does the production work.

## Phase 5 — Verify

Verification has three layers:

1. **Contract review:** compare every deliverable against `dispatch-brief.md`.
2. **Independent review:** when subagents are available, use a fresh supported-model reviewer. It reports findings; it does not repair silently.
3. **Real-environment test:** run bounded local tests already authorized. If the valid test requires a person, external system, send, publish, or deployment, mark it pending until permission and evidence exist.

Record exact evidence and the highest proven state:

- `PREPARED`
- `BUILT`
- `LOCALLY VERIFIED`
- `HANDOFF AUTHORIZED`
- `HANDED OFF`
- `RETURN EVIDENCE RECEIVED`

Never skip from BUILT to effective.

## Phase 6 — Write `dispatch-debrief.md`

Read `references/examples/example-dispatch-debrief.md` for calibration. Write the debrief in the main context because it depends on the interaction.

Use this structure:

```text
🎯 DISPATCH DEBRIEF

📁 PROJECT
   [Project name]

📦 DELIVERABLE
   [Named deliverable and path]

🧭 DISPATCH
   ✅ Steps completed: [list]
   ⏭ Steps skipped: [list and tradeoff]

🧠 MODEL
   [Runtime, model, effort, subagent routes]

🪞 DECISION THAT MOST CHANGED THE RESULT
   [Specific decision and effect]

🚧 TRIPWIRES OR WORKAROUNDS USED
   [What fired, what was missing, how it was handled]

✅ WHAT WORKED
   [1–3 concrete observations tied to this dispatch]

⚠️ WHAT WAS HARDER THAN EXPECTED
   [1–3 surprises, corrections, or sources of friction]

📌 WHAT REMAINS OPEN
   [Each open item with owner, next action, and required evidence]

🧪 VERIFICATION
   [Tests run, evidence, highest proven state]

🔄 CONTINUE
   [The four-sentence Continue paragraph]

🤝 HANDOFF
   [Destination, next owner, authorization state, expected return]

ONE THING TO TRY DIFFERENTLY NEXT TIME
   [Specific collaboration lesson]
```

Save it beside the brief and deliverable.

Show `dispatch-brief.md`, the deliverable and supporting files, verification findings, and `dispatch-debrief.md` together. Wait.

## Phase 7 — Close

Confirm:

```text
✅ DISPATCH BUILD COMPLETE

Saved in [project folder]:
   - dispatch-brief.md
   - [deliverable and supporting files]
   - dispatch-debrief.md

Highest proven state: [state]
Next owner/action: [owner and action]
Return evidence expected: [evidence]

The build is complete only to the evidence level stated above.
```

If real-world evidence is pending, invite the user to bring it back. Analyze and iterate from that evidence; do not substitute another model’s opinion for the named real-world test.

## Common mistakes

| Mistake | Correction |
|---|---|
| Building before the brief is approved | Stop, finish all eight steps, write the brief, and obtain build approval |
| Treating the topic as the deliverable | Require a filename and finished-state sentence |
| Asking generic or endless questions | Ask up to four project-specific questions; route the remaining unknowns |
| Calling installed capability available | Verify access or mark it Unsure |
| Listing Alternatives after work starts | Compare exactly three approaches before build approval |
| Writing soft boundaries | Convert them to absolute Tripwires |
| Calling a restart note optional | Always write Continue; assess restart signals explicitly |
| Treating AI review as the Test | Name the real environment and the evidence it returns |
| Letting Handoff imply permission | Record authorization separately and keep the action closed |
| Claiming completion at BUILT | Report the highest proven evidence state |
| Using a weaker model silently | Stop and require a supported route |

## Red flags — stop and repair the dispatch

- “I can make reasonable assumptions and start.”
- The user has not approved `dispatch-brief.md`.
- A Missing or Unsure supply has disappeared from the record.
- The chosen approach has no stated alternatives or reason.
- A Tripwire is phrased as “prefer,” “generally,” or “when possible.”
- Continue does not name the single next move.
- The test can be completed entirely by asking another model.
- Handoff names no returning evidence.
- A subagent uses a model below the route floor.
- A result is called successful before its real environment or audience produced evidence.

Any red flag means the agent stops, repairs the dispatch record, shows the repair, and waits where approval is required.
