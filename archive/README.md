# Pre-v2 Marketplace archive

The pre-v2 ShiftOS Marketplace is preserved at the immutable `legacy-marketplace-v1` tag.

To inspect that release without changing the current branch:

```text
git show legacy-marketplace-v1:README.md
```

To create a separate local rollback branch from the preserved release:

```text
git switch -c restore-marketplace-v1 legacy-marketplace-v1
```

The active v2 branch does not carry copies of the retired plugin payloads.
