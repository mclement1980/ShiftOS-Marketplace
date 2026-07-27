## Summary

Describe the public Marketplace change and the participant-facing reason for it.

## Release scope

- [ ] Claude and Codex remain the only active platform routes.
- [ ] Plugin names, public display identity, and versions remain synchronized.
- [ ] Distribution ZIPs remain direct-skill packages with no embedded plugin manifest.
- [ ] ZIP hashes and shared core skill-payload parity have been revalidated.
- [ ] Manual-equivalent guidance and the installation-is-not-completion boundary remain intact.

## Validation

- [ ] `python3 scripts/validate_marketplace.py`
- [ ] `claude plugin validate . --strict`
- [ ] Codex isolated marketplace lifecycle test, or an explicit held-proof record
- [ ] Full-tree committed whitespace check
- [ ] Public-content scans

## Evidence boundary

State exactly what was tested and what remains unobserved. Do not infer participant transfer, authenticated production behavior, workplace adoption, or organizational impact.
