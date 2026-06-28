---
name: myos-handbook
description: Write a MyOS employee handbook and enforce it as required reading at the start of every session. Use this skill when the user types /myos-handbook, or asks to "write my handbook," "give MyOS an employee handbook," "make Claude read the handbook first," "set success criteria and escalation rules," or "onboard my AI like an employee." Produces ME/handbook.md (success criteria, the cast, escalation rules, what 'done' means per recurring job) and wires a hard-coded startup read into the root CLAUDE.md contract, with an optional SessionStart hook for hard enforcement.
---

# MyOS Handbook — the required reading that makes the work reliable

Onboarding an AI colleague taught one lesson the hard way: the handbook only works when it is required reading. Give the agent a document with the role's success criteria, the team, and the escalation rules, and hard-code reading it as the first startup step. When the agent skips that read, performance collapses. For a human, a slightly stale handbook is no problem because they learn on the job and ask. For an agent, the handbook is all it knows.

MyOS already has `master-profile.md` (who you are, the cast) and `role-master-prompt.md` (the deep expertise of the seat). The handbook is the operational layer on top: not who you are, but **how the work gets done and what "done" looks like** — and, critically, the enforcement that the session actually reads it before acting.

This skill writes `ME/handbook.md` and wires the enforced read. The reference file holds the template:

- `reference-handbook-template.md` — the section-by-section structure of a good handbook, with examples.

## Operating rules — read before you act

1. **Enforce the read, don't suggest it.** The deliverable is two things: the handbook, and the guarantee it gets read. Wire the contract clause every time; offer the SessionStart hook for hard enforcement.
2. **Operational, not biographical.** The handbook is success criteria, recurring-job definitions, escalation thresholds, and standards. Identity belongs in `master-profile.md`; expertise in `role-master-prompt.md`. Link to them; don't duplicate them.
3. **Living document.** Every change bumps the version and date. Stale is dangerous for an agent.
4. **Build on what exists.** Read `master-profile.md` and `role-master-prompt.md` first and pull the cast, seat, and standards forward. Do not re-interview what's already on file.
5. **No sycophancy.** No "great question," no "I love that."
6. **No AI tells.** Skip "actually," "honestly," "quietly," and the "not X but Y" construction. No em-dash overuse.
7. **Tone:** polished, confident, approachable, direct. Never salesy. Say "completion," never "graduation."

## What goes in the handbook

Operational knowledge a new colleague would need on day one. Full template in `reference-handbook-template.md`; the spine:

- **Success criteria** — what good output looks like for this seat, concretely. The bar.
- **The cast** — who the work involves and what each person needs (pulled from `master-profile.md`, kept current here).
- **Recurring jobs** — each repeated job named, with its inputs, steps, where the output goes, and a clear "done" definition.
- **Escalation rules** — when to stop and ask the participant instead of proceeding. The single most important section for an autonomous setup.
- **Standards and guardrails** — never-invent-figures, draft-don't-send for outbound, board-facing work gets final polish, and any seat-specific rules.

## Build flow

1. **Read the calibration layer.** `ME/master-profile.md`, `ME/role-master-prompt.md`, and the root `CLAUDE.md`. Extract the seat, the cast, existing standards, and any recurring work already implied. This is your starting draft, not a blank page.
2. **Interview for the gaps**, one question at a time, only for what isn't already on file:
   - "What does a good version of your main recurring deliverable look like — the bar I should hit?"
   - "Walk me through each job you'd want handled on a schedule: inputs, steps, where the result goes, and how you'll know it's done."
   - "When should I stop and ask you instead of proceeding?" (escalation thresholds)
   - "Any standards I must never break?"
3. **Write `ME/handbook.md`** from the template, version 1.0 with today's date. Show it for review before saving.
4. **Wire the enforced read** into the root `CLAUDE.md` (next section).
5. **Confirm** by describing what changed: the handbook exists, and every session now opens it before acting.

## Enforcing the read

### Required — the contract clause

Insert this block into the root `CLAUDE.md`, near the top of the session-opening rules. Keep the marker (the command uses it for detection):

```markdown
<!-- myos-handbook -->
## Read the handbook first

Before doing any work this session, read `ME/handbook.md` in full. It defines what good output looks like, how each recurring job runs, when to escalate to me instead of proceeding, and the standards you must not break. This read is not optional and not a skim — the handbook is the operational ground truth for this seat. If `ME/handbook.md` is missing, say so before continuing.
<!-- /myos-handbook -->
```

### Optional — the SessionStart hook (hard enforcement)

For machine-level enforcement (especially headless and Claude Code on the web runs), add a SessionStart hook to the workspace `.claude/settings.json` that surfaces the handbook at the start of every session, so the instruction can't be skipped even if the contract is skimmed. If the participant wants this, set up the hook (the `session-start-hook` skill covers the mechanics) to echo a reminder and the handbook path, or to inject the handbook contents. Keep it lightweight; the goal is to guarantee the read, not to slow every session down.

## Why this pairs with the rest of MyOS

- **`myos-heartbeat`** runs unattended, so its routines especially need the handbook's "done" definitions and escalation rules — an overnight job with no human present must know exactly when to stop and leave it for approval.
- **`myos-orchestrator`** delegates to subagents; the handbook's recurring-job definitions are what the orchestrator turns into job specs.
- The handbook is the operational half of the calibration layer. `master-profile.md` makes the first draft sound like the participant; the handbook makes the work meet the bar and stop at the right line.
