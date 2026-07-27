# ShiftOS Marketplace

This repository distributes **ShiftOS-DISPATCH**, the ShiftOS companion that helps a participant prepare, approve, build, verify, and hand off one real deliverable.

Every cohort receives both the Claude and Codex versions. Choose the version for the platform you already use and run that one version; you do not need to install both. Codex is the ShiftOS reference and default implementation. Claude is fully supported under the same DISPATCH workflow and proof contract.

After installation, invoke the companion in either platform by saying:

> Run DISPATCH.

## Claude Marketplace route

In Claude Code, add this repository as a marketplace and install the Claude plugin:

```text
/plugin marketplace add mclement1980/ShiftOS-Marketplace
/plugin install shiftos-dispatch@shiftos
```

Claude exposes the Marketplace skill through the namespaced shortcut `/shiftos-dispatch:dispatch`. Use “Run DISPATCH” as the supported cross-platform invocation.

## Codex repository-marketplace route

In a terminal with Codex installed, add this repository and install the Codex plugin:

```text
codex plugin marketplace add mclement1980/ShiftOS-Marketplace
codex plugin add shiftos-dispatch@shiftos
```

## ZIP fallback routes

Use a ZIP only when the repository marketplace route is unavailable:

- [Download the Claude ZIP](distributions/shiftos-dispatch/1.0.0/dispatch-claude.zip), extract it, and follow `dispatch/runtime-claude.md`.
- [Download the Codex ZIP](distributions/shiftos-dispatch/1.0.0/dispatch-codex.zip), extract it, and follow `dispatch/runtime-codex.md`.

The release checksums are in [SHA256SUMS](distributions/shiftos-dispatch/1.0.0/SHA256SUMS).

## What completion means

Installation makes the guided companion available; it does not complete the learning work or prove transfer. A complete DISPATCH run still requires an approved brief, the actual requested deliverable, verification evidence, and a debrief.

The manual equivalent remains valid. A participant can use the course materials to prepare the same brief, build the deliverable, verify it against the agreed standard, and record the debrief without installing a plugin.

## Support and policy

- [Support](SUPPORT.md)
- [Security](SECURITY.md)
- [Release policy](RELEASE-POLICY.md)
- [License](LICENSE.md)

© 2026 KHM Shift. ShiftOS is a program of KHM Shift.
