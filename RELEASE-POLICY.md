# Release Policy

## Supported release surface

The active public release contains exactly two platform routes:

- Claude
- Codex

Both routes must carry the same ShiftOS-DISPATCH version, public identity, semantic workflow, required outputs, and proof boundary. Runtime-specific installation, model, effort, and invocation guidance stays in its corresponding package.

## Versioning

ShiftOS-DISPATCH uses semantic versioning. The version is declared in each platform plugin manifest and in the versioned distribution directory. Catalog entries do not duplicate the plugin version.

## Release gate

A release candidate must pass:

1. the repository's standard-library validator;
2. the current Claude manifest validator;
3. Codex marketplace discovery and lifecycle validation when a safe isolated route is available;
4. exact ZIP checksum and shared skill-payload parity checks;
5. unsafe-archive, public-content, and internal-data scans; and
6. repository whitespace validation.

Passing these gates proves only the files and local command paths tested. It does not prove participant transfer, authenticated production behavior, workplace adoption, or organizational impact.

## Distribution integrity

Release ZIPs use a direct-skill envelope: the extracted `dispatch` folder contains `SKILL.md`, its learning support files, and one route-specific installation guide, but no plugin manifest. Shared core skill payloads must match the Marketplace plugin trees byte for byte. Marketplace wrappers and direct-skill ZIP documentation are validated independently because they use different installation and invocation routes. SHA-256 digests are published beside the ZIPs. Any ZIP byte change requires a new validated release input and an updated release record.

## Prior release access

The pre-v2 Marketplace is preserved at the immutable `legacy-marketplace-v1` tag. See [archive/README.md](archive/README.md) for inspection and rollback instructions.
