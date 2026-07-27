# DISPATCH — Claude Route

## Supported model

- Preferred: Claude Opus 4.8
- Minimum: Claude Sonnet 5
- Effort: use the runtime default; do not lower it for speed

If the current session is below Sonnet 5 or the model cannot be verified, stop before Bootstrap. Relaunch on Opus 4.8 or Sonnet 5, then ask Claude to run DISPATCH.

Heavy Alternatives, brief, deliverable, and verification subagents must use Opus 4.8 or Sonnet 5. Prefer Opus 4.8 for complex, multi-file, audience-facing, sensitive, or high-risk work.

## Install

Add the ShiftOS Marketplace and install the Claude plugin:

```text
/plugin marketplace add mclement1980/ShiftOS-Marketplace
/plugin install shiftos-dispatch@shiftos
```

## Invoke

```text
Run DISPATCH.
```

Claude exposes the namespaced shortcut `/shiftos-dispatch:dispatch`. The natural-language instruction is the supported cross-platform route.

## Verify

Confirm:

1. `shiftos-dispatch@shiftos` is installed and enabled.
2. The model gate appears before project selection.
3. The gate recommends Opus 4.8 and refuses anything below Sonnet 5.
4. The Bootstrap asks Start from scratch or Evaluate an existing project.

## Remove

```text
/plugin uninstall shiftos-dispatch@shiftos
```

Existing `dispatch-brief.md`, deliverables, and `dispatch-debrief.md` files remain untouched.
