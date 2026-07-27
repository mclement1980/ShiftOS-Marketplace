#!/usr/bin/env python3
"""Deterministic, standard-library validation for ShiftOS Marketplace v2."""

from __future__ import annotations

import hashlib
import json
import re
import stat
import sys
import zipfile
from pathlib import Path, PurePosixPath


ROOT = Path(__file__).resolve().parents[1]
VERSION = "1.0.0"
PLUGIN_ID = "shiftos-dispatch"
DISPLAY_NAME = "ShiftOS-DISPATCH"
CATALOG_NAME = "shiftos"
DIST = ROOT / "distributions" / PLUGIN_ID / VERSION

ROUTES = {
    "claude": {
        "catalog": ROOT / ".claude-plugin" / "marketplace.json",
        "plugin": ROOT / "claude-plugins" / PLUGIN_ID,
        "manifest": ROOT
        / "claude-plugins"
        / PLUGIN_ID
        / ".claude-plugin"
        / "plugin.json",
        "skill": ROOT / "claude-plugins" / PLUGIN_ID / "skills" / "dispatch",
        "zip": DIST / "dispatch-claude.zip",
        "sha256": "3fff17a74a21b6fb10a9dd08a985f7eae41d8e7f53d3255f7c5c8026d6256b22",
        "foreign": ("co" + "dex", "chat" + "gpt"),
    },
    "codex": {
        "catalog": ROOT / ".agents" / "plugins" / "marketplace.json",
        "plugin": ROOT / "plugins" / PLUGIN_ID,
        "manifest": ROOT
        / "plugins"
        / PLUGIN_ID
        / ".codex-plugin"
        / "plugin.json",
        "skill": ROOT / "plugins" / PLUGIN_ID / "skills" / "dispatch",
        "zip": DIST / "dispatch-codex.zip",
        "sha256": "a5fef514ee7df9ddc5095acdab27cba5a6ac2e9613133ead824fb6943075b9bf",
        "foreign": ("clau" + "de", "chat" + "gpt"),
    },
}

REQUIRED_PUBLIC_FILES = {
    ".gitattributes",
    "README.md",
    "LICENSE.md",
    "SECURITY.md",
    "SUPPORT.md",
    "CHANGELOG.md",
    "RELEASE-POLICY.md",
    "archive/README.md",
    ".github/CODEOWNERS",
    ".github/pull_request_template.md",
    ".github/workflows/validate-marketplace.yml",
    "scripts/validate_marketplace.py",
    ".claude-plugin/marketplace.json",
    ".agents/plugins/marketplace.json",
    "distributions/shiftos-dispatch/1.0.0/dispatch-claude.zip",
    "distributions/shiftos-dispatch/1.0.0/dispatch-codex.zip",
    "distributions/shiftos-dispatch/1.0.0/SHA256SUMS",
    "distributions/shiftos-dispatch/1.0.0/RELEASE-NOTES.md",
    "distributions/shiftos-dispatch/1.0.0/PUBLIC-PROVENANCE.md",
}

EXPECTED_PAYLOAD_FILES = {
    "README.md",
    "SKILL.md",
    "references/examples/README.md",
    "references/examples/example-dispatch-brief.md",
    "references/examples/example-dispatch-debrief.md",
    "references/examples/example-draft-artifact.md",
    "references/taxonomies.md",
}
EXPECTED_CORE_FILES = EXPECTED_PAYLOAD_FILES - {"README.md"}

ERRORS: list[str] = []


def fail(message: str) -> None:
    ERRORS.append(message)


def relative(path: Path) -> str:
    try:
        return path.relative_to(ROOT).as_posix()
    except ValueError:
        return str(path)


def load_json(path: Path) -> dict:
    try:
        with path.open("r", encoding="utf-8") as handle:
            value = json.load(handle)
    except FileNotFoundError:
        fail(f"missing JSON file: {relative(path)}")
        return {}
    except (OSError, UnicodeDecodeError, json.JSONDecodeError) as exc:
        fail(f"invalid JSON file {relative(path)}: {exc}")
        return {}
    if not isinstance(value, dict):
        fail(f"JSON root must be an object: {relative(path)}")
        return {}
    return value


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def public_files() -> list[Path]:
    paths: list[Path] = []
    for path in ROOT.rglob("*"):
        if not path.is_file():
            continue
        rel_parts = path.relative_to(ROOT).parts
        if rel_parts and rel_parts[0] in {".git", ".superpowers"}:
            continue
        if "__pycache__" in rel_parts:
            continue
        paths.append(path)
    return sorted(paths)


def text_value(path: Path) -> str | None:
    try:
        data = path.read_bytes()
    except OSError as exc:
        fail(f"cannot read {relative(path)}: {exc}")
        return None
    if b"\x00" in data:
        return None
    try:
        return data.decode("utf-8")
    except UnicodeDecodeError:
        return None


def validate_required_files() -> None:
    for rel in sorted(REQUIRED_PUBLIC_FILES):
        path = ROOT / rel
        if not path.is_file():
            fail(f"missing required file: {rel}")

    expected_runtime = {
        "claude": "runtime-claude.md",
        "codex": "runtime-codex.md",
    }
    for route, expected_runtime_file in expected_runtime.items():
        config = ROUTES[route]
        manifest = config["manifest"]
        skill = config["skill"]
        if not manifest.is_file():
            fail(f"missing {route} plugin manifest: {relative(manifest)}")
        actual = {
            path.relative_to(skill).as_posix()
            for path in skill.rglob("*")
            if path.is_file()
        } if skill.is_dir() else set()
        expected = EXPECTED_PAYLOAD_FILES | {expected_runtime_file}
        missing = expected - actual
        extra = actual - expected
        for rel in sorted(missing):
            fail(f"missing {route} payload file: {relative(skill / rel)}")
        for rel in sorted(extra):
            fail(f"unexpected {route} payload file: {relative(skill / rel)}")
        skill_text = text_value(skill / "SKILL.md") or ""
        if not re.search(r"(?m)^name:\s*dispatch\s*$", skill_text):
            fail(f"{route} skill frontmatter name must be dispatch")

    claude_dirs = {
        path.name
        for path in (ROOT / "claude-plugins").iterdir()
        if path.is_dir()
    } if (ROOT / "claude-plugins").is_dir() else set()
    codex_dirs = {
        path.name
        for path in (ROOT / "plugins").iterdir()
        if path.is_dir()
    } if (ROOT / "plugins").is_dir() else set()
    if claude_dirs != {PLUGIN_ID}:
        fail(f"Claude active plugin allowlist mismatch: {sorted(claude_dirs)}")
    if codex_dirs != {PLUGIN_ID}:
        fail(f"Codex active plugin allowlist mismatch: {sorted(codex_dirs)}")

    zip_paths = {
        path.relative_to(ROOT).as_posix()
        for path in public_files()
        if path.suffix.lower() == ".zip"
    }
    expected_zips = {
        "distributions/shiftos-dispatch/1.0.0/dispatch-claude.zip",
        "distributions/shiftos-dispatch/1.0.0/dispatch-codex.zip",
    }
    if zip_paths != expected_zips:
        fail(f"distribution ZIP allowlist mismatch: {sorted(zip_paths)}")


def validate_manifest_common(route: str, manifest: dict) -> None:
    if manifest.get("name") != PLUGIN_ID:
        fail(f"{route} plugin name mismatch")
    if manifest.get("version") != VERSION:
        fail(f"{route} plugin version mismatch")
    if route == "claude":
        if manifest.get("displayName") != DISPLAY_NAME:
            fail("Claude plugin display name mismatch")
        if "interface" in manifest:
            fail("Claude plugin manifest contains unsupported interface metadata")
        if "skills" in manifest:
            fail("Claude plugin must use its standard skills/ discovery path")
    elif route == "codex":
        interface = manifest.get("interface")
        if not isinstance(interface, dict):
            fail("Codex plugin interface must be an object")
            return
        if interface.get("displayName") != DISPLAY_NAME:
            fail("Codex display name mismatch")
        if interface.get("category") != "Productivity":
            fail("Codex plugin category mismatch")
        if manifest.get("skills") != "./skills/":
            fail("Codex plugin skill declaration mismatch")


def validate_manifests() -> None:
    claude_catalog = load_json(ROUTES["claude"]["catalog"])
    codex_catalog = load_json(ROUTES["codex"]["catalog"])
    manifests = {
        route: load_json(config["manifest"])
        for route, config in ROUTES.items()
    }

    if claude_catalog.get("name") != CATALOG_NAME:
        fail("Claude catalog name mismatch")
    claude_plugins = claude_catalog.get("plugins")
    if not isinstance(claude_plugins, list) or len(claude_plugins) != 1:
        fail("Claude catalog must contain exactly one plugin")
    else:
        entry = claude_plugins[0]
        if not isinstance(entry, dict):
            fail("Claude catalog plugin entry must be an object")
        else:
            if entry.get("name") != PLUGIN_ID:
                fail("Claude catalog plugin name mismatch")
            if entry.get("source") != "./claude-plugins/shiftos-dispatch":
                fail("Claude catalog source mismatch")
            description = entry.get("description")
            if (
                not isinstance(description, str)
                or DISPLAY_NAME not in description
            ):
                fail("Claude catalog must carry the public display identity")
            if "version" in entry:
                fail("Claude catalog entry must not duplicate plugin version")

    if codex_catalog.get("name") != CATALOG_NAME:
        fail("Codex catalog name mismatch")
    interface = codex_catalog.get("interface")
    if not isinstance(interface, dict) or interface.get("displayName") != "ShiftOS":
        fail("Codex catalog display name mismatch")
    codex_plugins = codex_catalog.get("plugins")
    if not isinstance(codex_plugins, list) or len(codex_plugins) != 1:
        fail("Codex catalog must contain exactly one plugin")
    else:
        entry = codex_plugins[0]
        if not isinstance(entry, dict):
            fail("Codex catalog plugin entry must be an object")
        else:
            if entry.get("name") != PLUGIN_ID:
                fail("Codex catalog plugin name mismatch")
            if entry.get("source") != {
                "source": "local",
                "path": "./plugins/shiftos-dispatch",
            }:
                fail("Codex catalog source mismatch")
            if entry.get("policy") != {
                "installation": "AVAILABLE",
                "authentication": "ON_INSTALL",
            }:
                fail("Codex catalog policy mismatch")
            if entry.get("category") != "Productivity":
                fail("Codex catalog category mismatch")
            if "version" in entry:
                fail("Codex catalog entry must not duplicate plugin version")

    for route, manifest in manifests.items():
        validate_manifest_common(route, manifest)

    if manifests["claude"].get("version") != manifests["codex"].get("version"):
        fail("Claude and Codex plugin versions differ")


def validate_zip_path(name: str, seen: set[str], route: str) -> None:
    if not name or "\x00" in name:
        fail(f"{route} ZIP contains an empty or null path")
        return
    if "\\" in name:
        fail(f"{route} ZIP contains a backslash path: {name!r}")
    pure = PurePosixPath(name)
    if pure.is_absolute() or any(part in {"", ".", ".."} for part in pure.parts):
        fail(f"{route} ZIP contains an unsafe path: {name!r}")
    if re.match(r"^[A-Za-z]:", name):
        fail(f"{route} ZIP contains a drive-qualified path: {name!r}")
    if name in seen:
        fail(f"{route} ZIP contains a duplicate path: {name!r}")
    seen.add(name)


def validate_zip_and_parity(route: str) -> None:
    config = ROUTES[route]
    zip_path = config["zip"]
    if not zip_path.is_file():
        fail(f"missing {route} ZIP: {relative(zip_path)}")
        return
    actual_hash = sha256(zip_path)
    if actual_hash != config["sha256"]:
        fail(
            f"{route} ZIP hash mismatch: expected {config['sha256']}, "
            f"got {actual_hash}"
        )

    try:
        with zipfile.ZipFile(zip_path) as archive:
            seen: set[str] = set()
            files: dict[str, bytes] = {}
            for info in archive.infolist():
                validate_zip_path(info.filename, seen, route)
                mode = (info.external_attr >> 16) & 0xFFFF
                if stat.S_ISLNK(mode):
                    fail(f"{route} ZIP contains a symlink: {info.filename!r}")
                if info.is_dir():
                    continue
                files[info.filename] = archive.read(info)
    except (OSError, zipfile.BadZipFile, RuntimeError) as exc:
        fail(f"invalid {route} ZIP: {exc}")
        return

    expected_zip_names = {
        *{
            f"dispatch/{rel}"
            for rel in (
                EXPECTED_PAYLOAD_FILES
                | {f"runtime-{route}.md"}
            )
        },
    }
    if set(files) != expected_zip_names:
        missing = expected_zip_names - set(files)
        extra = set(files) - expected_zip_names
        if missing:
            fail(f"{route} ZIP missing files: {sorted(missing)}")
        if extra:
            fail(f"{route} ZIP has unexpected files: {sorted(extra)}")

    forbidden_zip_terms = (
        "air" + "port",
        "my" + "os",
        *config["foreign"],
        "/" + "Users/",
        "Personal " + "GDrive",
        "/Ze" + "us/",
    )
    for archive_name, data in files.items():
        try:
            text = data.decode("utf-8")
        except UnicodeDecodeError:
            continue
        lowered = text.lower()
        for term in forbidden_zip_terms:
            if term.lower() in lowered:
                fail(
                    f"{route} ZIP file {archive_name!r} contains "
                    f"forbidden term {term!r}"
                )

    zip_readme = files.get("dispatch/README.md", b"").decode(
        "utf-8", errors="replace"
    )
    if f"# {DISPLAY_NAME}" not in zip_readme:
        fail(f"{route} ZIP README public display identity mismatch")
    if f"Version: {VERSION}" not in zip_readme:
        fail(f"{route} ZIP README version mismatch")
    zip_skill = files.get("dispatch/SKILL.md", b"").decode(
        "utf-8", errors="replace"
    )
    if not re.search(r"(?m)^name:\s*dispatch\s*$", zip_skill):
        fail(f"{route} ZIP skill frontmatter name must be dispatch")

    mappings = {
        f"dispatch/{rel}": config["skill"] / rel
        for rel in EXPECTED_CORE_FILES
    }
    for archive_name, tree_path in mappings.items():
        if archive_name not in files or not tree_path.is_file():
            continue
        if files[archive_name] != tree_path.read_bytes():
            fail(
                f"{route} plugin tree differs from ZIP payload: "
                f"{archive_name} -> {relative(tree_path)}"
            )


def validate_checksums() -> None:
    sums_path = DIST / "SHA256SUMS"
    try:
        lines = sums_path.read_text(encoding="utf-8").splitlines()
    except OSError as exc:
        fail(f"cannot read SHA256SUMS: {exc}")
        return
    expected = [
        f"{ROUTES['claude']['sha256']}  dispatch-claude.zip",
        f"{ROUTES['codex']['sha256']}  dispatch-codex.zip",
    ]
    if lines != expected:
        fail("SHA256SUMS content or ordering mismatch")


def validate_delivery_guides() -> None:
    expected_commands = {
        "claude": (
            "/plugin marketplace add mclement1980/ShiftOS-Marketplace",
            "/plugin install shiftos-dispatch@shiftos",
            "/plugin uninstall shiftos-dispatch@shiftos",
        ),
        "codex": (
            "codex plugin marketplace add mclement1980/ShiftOS-Marketplace",
            "codex plugin add shiftos-dispatch@shiftos",
            "codex plugin remove shiftos-dispatch@shiftos",
        ),
    }
    direct_skill_paths = {
        "claude": "~/.claude/skills/dispatch/",
        "codex": "~/.codex/skills/dispatch/",
    }

    for route, config in ROUTES.items():
        wrapper_readme = text_value(config["skill"] / "README.md") or ""
        wrapper_runtime = (
            text_value(config["skill"] / f"runtime-{route}.md") or ""
        )
        if "Run DISPATCH" not in wrapper_readme:
            fail(f"{route} Marketplace README lacks cross-platform invocation")
        if "`/dispatch`" in wrapper_readme or "`/dispatch`" in wrapper_runtime:
            fail(f"{route} Marketplace guide promises unnamespaced /dispatch")
        for command in expected_commands[route]:
            if command not in wrapper_runtime:
                fail(f"{route} Marketplace guide lacks command: {command}")
        if direct_skill_paths[route] in wrapper_runtime:
            fail(f"{route} Marketplace guide contains ZIP-style install path")

        try:
            with zipfile.ZipFile(config["zip"]) as archive:
                zip_runtime = archive.read(
                    f"dispatch/runtime-{route}.md"
                ).decode("utf-8")
        except (OSError, KeyError, UnicodeDecodeError, zipfile.BadZipFile) as exc:
            fail(f"cannot validate {route} ZIP delivery guide: {exc}")
            continue
        if direct_skill_paths[route] not in zip_runtime:
            fail(f"{route} ZIP guide lacks direct-skill install path")
        if "/dispatch" not in zip_runtime:
            fail(f"{route} ZIP guide lacks direct-skill invocation")


def validate_public_content() -> None:
    forbidden_public = {
        "air" + "port": "retired internal lineage term",
        "my" + "os": "retired system identity",
        "chat" + "gpt": "unapproved platform route",
    }
    retired_identifiers = (
        "ai-" + "ready-project",
        "my-" + "capture-system",
        "role-" + "os-interview",
        "shiftos-" + "setup-coach",
        "my" + "os-" + "local-search",
        "my" + "os-" + "heartbeat",
        "my" + "os-" + "handbook",
        "my" + "os-" + "orchestrator",
    )
    unresolved_terms = (
        "to" + "do",
        "fix" + "me",
        "tk" + "tk",
        "change" + "me",
        "lorem " + "ipsum",
    )
    unsupported_claims = (
        "participant " + "transfer proven",
        "authenticated " + "live behavior proven",
        "workplace " + "adoption proven",
        "organizational " + "impact proven",
    )
    internal_markers = (
        "/" + "Users/",
        "/" + "home/",
        "/" + "Volumes/",
        "C:" + "\\Users\\",
        "Personal " + "GDrive",
        "/Ze" + "us/",
    )
    client_markers = (
        "confidential " + "client",
        "client " + "data:",
        "participant " + "email:",
        "account " + "number:",
    )
    credential_assignment = re.compile(
        r"(?i)(?:api[_-]?key|access[_-]?"
        + "to"
        + r"ken|se"
        + r"cret)\s*[:=]\s*[\"']?[A-Za-z0-9_./+=-]{12,}"
    )
    angle_marker = re.compile(
        r"(?i)<\s*(?:your|insert|replace)[^>]{0,80}>"
    )

    for path in public_files():
        text = text_value(path)
        if text is None:
            continue
        lowered = text.lower()
        for term, label in forbidden_public.items():
            if term in lowered:
                fail(f"{relative(path)} contains {label}")
        for term in retired_identifiers:
            if term in lowered:
                fail(f"{relative(path)} contains retired active identifier {term!r}")
        for term in unresolved_terms:
            if term in lowered:
                fail(f"{relative(path)} contains unresolved marker {term!r}")
        for phrase in unsupported_claims:
            if phrase in lowered:
                fail(f"{relative(path)} contains unsupported claim {phrase!r}")
        for marker in internal_markers:
            if marker.lower() in lowered:
                fail(f"{relative(path)} contains internal absolute-path marker")
        for marker in client_markers:
            if marker.lower() in lowered:
                fail(f"{relative(path)} contains client-data marker")
        if credential_assignment.search(text):
            fail(f"{relative(path)} contains an apparent credential assignment")
        if angle_marker.search(text):
            fail(f"{relative(path)} contains an unresolved angle-bracket marker")

    for route, config in ROUTES.items():
        for path in sorted(config["plugin"].rglob("*")):
            if not path.is_file():
                continue
            text = text_value(path)
            if text is None:
                continue
            lowered = text.lower()
            for term in config["foreign"]:
                if term in lowered:
                    fail(
                        f"{relative(path)} contains foreign-runtime guidance "
                        f"for {term}"
                    )


def validate_workflow() -> None:
    path = ROOT / ".github" / "workflows" / "validate-marketplace.yml"
    text = text_value(path)
    if text is None:
        return
    if "validate-marketplace:" not in text:
        fail("workflow job name validate-marketplace is missing")
    if "pull_request:" not in text:
        fail("workflow pull_request trigger is missing")
    if not re.search(r"(?m)^\s*push:\s*$", text):
        fail("workflow push trigger is missing")
    if not re.search(r"(?m)^\s*-\s+main\s*$", text):
        fail("workflow main branch filter is missing")
    if "python3 scripts/validate_marketplace.py" not in text:
        fail("workflow validator command is missing")
    full_tree_whitespace = (
        'git diff --check "$(git hash-object -t tree /dev/null)" HEAD'
    )
    if full_tree_whitespace not in text:
        fail("workflow full-tree whitespace check is missing")
    for line in text.splitlines():
        stripped = line.strip()
        if not stripped.startswith("uses:"):
            continue
        action = stripped.split(":", 1)[1].strip()
        if not re.fullmatch(r"[^@\s]+@[0-9a-fA-F]{40}", action):
            fail(f"workflow action is not pinned to a full commit SHA: {action}")


def main() -> int:
    if Path.cwd().resolve() != ROOT:
        print(f"INFO: validating repository at {ROOT}")

    validate_required_files()
    validate_manifests()
    for route in ROUTES:
        validate_zip_and_parity(route)
    validate_checksums()
    validate_delivery_guides()
    validate_public_content()
    validate_workflow()

    if ERRORS:
        print("MARKETPLACE VALIDATION: FAIL")
        for error in ERRORS:
            print(f"- {error}")
        return 1

    print("MARKETPLACE VALIDATION: PASS")
    print("Active routes: Claude, Codex")
    print(f"Public display identity: {DISPLAY_NAME}")
    print(f"Version: {VERSION}")
    print("ZIP hashes and shared core skill payloads: exact")
    print("Public-content and archive-safety findings: 0")
    return 0


if __name__ == "__main__":
    sys.exit(main())
