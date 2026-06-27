---
description: Write your MyOS employee handbook and make every session read it first
---

# /myos-handbook

You have been invoked via the `/myos-handbook` slash command, part of the **myos-handbook** plugin. Your job is to give the participant's MyOS Workspace an *employee handbook* — a living document of how the work actually gets done (success criteria, the cast, escalation rules, what "done" means per recurring job) — and to make reading it the hard-coded first move of every session.

This implements the highest-leverage lesson from onboarding an AI colleague: the handbook only works when it is *required reading*. When the agent skips it, performance collapses. Everything about the handbook's structure and how to enforce the read lives in the **myos-handbook** skill (at `skills/myos-handbook/SKILL.md`) and its reference file. Read the skill before you act.

## Step 1: Figure out where you're standing

Use **Glob** and **Read**:

1. **Workspace?** Confirm the ShiftOS Workspace root (`CLAUDE.md`, `ME/`, numbered sections). The handbook lives at `ME/handbook.md`.
2. **Handbook already exists?** Read `ME/handbook.md` if present. Treat it as real only if it has filled sections (success criteria, escalation, recurring jobs), not an empty stub.
3. **Enforcement wired?** Read the root `CLAUDE.md`. The required-read is installed if it contains the marker `<!-- myos-handbook -->`.

## Step 2A: No handbook → build it

Trigger the **myos-handbook** skill and run its **Build flow**: interview the participant for the handbook's contents (pulling first from `ME/master-profile.md` and `ME/role-master-prompt.md` so you don't re-ask what's known), write `ME/handbook.md` from the template, and wire the enforced startup read into the root `CLAUDE.md` contract.

## Step 2B: Handbook exists → update or check enforcement

Use **AskUserQuestion**: "You've already got a handbook. What do you want to do?"

Three options, in this order:

1. **Update it** — "Reflect a changed responsibility, a new recurring job, or a new escalation rule." (Edit `ME/handbook.md`, bump its version and date.)
2. **Check enforcement** — "Make sure every session is actually reading it first." (Confirm the `<!-- myos-handbook -->` block is in the root contract; offer the optional SessionStart hook from the skill.)
3. **Cancel** — "Never mind."

## Operating rules

- **The read must be enforced, not suggested.** A handbook nobody reads is dead weight. Wire it into the contract, and offer the SessionStart hook for hard enforcement.
- **Living document.** Every update bumps the version and date. For an agent, a stale handbook is all it knows.
- **Pull from what exists.** `master-profile.md` and `role-master-prompt.md` already hold the seat and the cast; build on them, don't re-interview.
- **No sycophancy.** No "great question," no "I love that."
- **No AI tells.** Skip "actually," "honestly," "quietly," and the "not X but Y" construction. No em-dash overuse.
- **Tone:** polished, confident, approachable, direct. Never salesy. Say "completion," never "graduation."
