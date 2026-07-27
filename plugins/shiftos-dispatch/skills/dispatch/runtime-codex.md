# DISPATCH — Codex Route

## Supported model

- Preferred default: `gpt-5.6-sol` at medium reasoning
- Complex, multi-file, audience-facing, sensitive, or high-risk work: `gpt-5.6-sol` at high reasoning
- Minimum fallback for bounded, low-risk, single-artifact work: `gpt-5.6-terra` at high reasoning

If the current session is below the floor or the model cannot be verified, stop before Bootstrap. Relaunch with a supported model and reasoning level, then ask Codex to run DISPATCH.

Heavy Alternatives, brief, deliverable, and verification subagents must meet the same floor. Do not use lightweight or mini models.

## Install

Add the ShiftOS Marketplace and install the Codex plugin:

```text
codex plugin marketplace add mclement1980/ShiftOS-Marketplace
codex plugin add shiftos-dispatch@shiftos
```

## Invoke

```text
Run DISPATCH.
```

## Verify

Confirm:

1. `shiftos-dispatch@shiftos` is installed and enabled.
2. The model gate appears before project selection.
3. The gate recommends `gpt-5.6-sol` at medium reasoning.
4. The Bootstrap asks Start from scratch or Evaluate an existing project.

## Remove

```text
codex plugin remove shiftos-dispatch@shiftos
```

Existing `dispatch-brief.md`, deliverables, and `dispatch-debrief.md` files remain untouched.
