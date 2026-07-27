# ShiftOS-DISPATCH

Version: 1.0.0

DISPATCH guides a user through preparing, approving, building, verifying, and handing off one real deliverable.

## Invocation

- “Run DISPATCH”
- “Help me create this from scratch”
- “Prepare this project so AI can carry it”
- “Rescope this existing project for autonomous AI work”

“Run DISPATCH” is the supported cross-platform instruction.

## Outputs

Every complete run produces:

1. `dispatch-brief.md`
2. The named deliverable and any necessary supporting files
3. `dispatch-debrief.md`

## Runtime model floor

- Preferred: `gpt-5.6-sol` at medium reasoning
- Complex or high-risk: `gpt-5.6-sol` at high reasoning
- Minimum bounded fallback: `gpt-5.6-terra` at high reasoning
- Do not use light or mini models.

The skill stops if the model is below the applicable floor or cannot be verified.

## Marketplace lifecycle

Install and update this skill through the ShiftOS Codex Marketplace. See `runtime-codex.md` for the exact commands and verification steps.

Removing the Marketplace plugin does not delete any project artifacts created by prior runs.
