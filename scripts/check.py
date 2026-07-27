#!/usr/bin/env python3
"""check.py — repository consistency gate.

Run before every commit and before publishing. It catches the failures that are
invisible in review and obvious to a user thirty seconds after they install the
plugin: a command registered in the manifest that points at a missing file, a
skill that was added but never registered, a malformed manifest, or a stray
non-English character in a product that promises English-only.

No third-party dependencies. Exit code 0 means publishable.

    python3 scripts/check.py
"""

import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# CJK ideographs, plus kana and hangul. This repository ships in English only,
# so any hit is a defect regardless of how it got there. The ranges are built
# from code points so that this file contains no non-English characters itself
# and therefore does not trip its own check.
_BLOCKED_RANGES = (
    (0x3040, 0x30FF),   # hiragana, katakana
    (0x3400, 0x4DBF),   # CJK extension A
    (0x4E00, 0x9FFF),   # CJK unified ideographs
    (0xAC00, 0xD7AF),   # hangul syllables
)
NON_ENGLISH = re.compile(
    "[" + "".join(f"{chr(lo)}-{chr(hi)}" for lo, hi in _BLOCKED_RANGES) + "]"
)

TEXT_SUFFIXES = (".md", ".py", ".json", ".txt", ".yml", ".yaml", ".sh", ".toml")
SKIP_DIRS = {".git", "__pycache__", ".venv", "venv", "node_modules", "research"}

failures = []
warnings = []
checks = 0


def fail(msg):
    failures.append(msg)


def warn(msg):
    warnings.append(msg)


def rel(path):
    return os.path.relpath(path, ROOT)


def load_json(path, required=True):
    global checks
    checks += 1
    if not os.path.exists(path):
        (fail if required else warn)(f"missing file: {rel(path)}")
        return None
    try:
        with open(path, encoding="utf-8") as fh:
            return json.load(fh)
    except json.JSONDecodeError as exc:
        fail(f"invalid JSON in {rel(path)}: {exc}")
        return None


def check_plugin_manifest():
    """The manifest and the skills directory must describe the same plugin."""
    global checks
    manifest = load_json(os.path.join(ROOT, ".claude-plugin", "plugin.json"))
    if manifest is None:
        return

    checks += 1
    if not manifest.get("name"):
        fail("plugin.json: 'name' is required")

    for field in ("description", "license", "repository"):
        checks += 1
        if not manifest.get(field):
            warn(f"plugin.json: '{field}' is empty — it shows in the plugin picker")

    registered = manifest.get("commands", []) or []
    if isinstance(registered, str):
        registered = [registered]

    normalized = set()
    for entry in registered:
        checks += 1
        target = os.path.join(ROOT, entry.lstrip("./"))
        if not os.path.exists(target):
            fail(f"plugin.json commands: registered file does not exist: {entry}")
        else:
            normalized.add(os.path.normpath(entry.lstrip("./")))

    # Drift in the other direction: a skill on disk that nobody registered ships
    # as dead weight and never appears as a command.
    skills_dir = os.path.join(ROOT, "skills")
    if os.path.isdir(skills_dir):
        for name in sorted(os.listdir(skills_dir)):
            if not name.endswith(".md"):
                continue
            checks += 1
            if os.path.normpath(os.path.join("skills", name)) not in normalized:
                fail(f"drift: skills/{name} exists but is not registered in plugin.json")

    if not manifest.get("version"):
        warn("plugin.json: no 'version' — installs track the git commit SHA, so every "
             "push reaches users. Set a semantic version at release.")


def check_marketplace():
    global checks
    market = load_json(os.path.join(ROOT, ".claude-plugin", "marketplace.json"))
    if market is None:
        return

    for field in ("name", "owner", "plugins"):
        checks += 1
        if field not in market:
            fail(f"marketplace.json: missing '{field}'")

    for entry in market.get("plugins", []):
        checks += 1
        name = entry.get("name", "<unnamed>")
        source = entry.get("source")
        if not source:
            fail(f"marketplace.json: plugin '{name}' has no 'source'")
            continue
        directory = ROOT if source in ("./", ".") else os.path.join(ROOT, source.lstrip("./"))
        if not os.path.isdir(directory):
            fail(f"marketplace.json: source directory not found for '{name}': {source}")
        elif not os.path.exists(os.path.join(directory, ".claude-plugin", "plugin.json")):
            fail(f"marketplace.json: no .claude-plugin/plugin.json under source of '{name}'")


def check_skill_frontmatter():
    """Every skill needs a description — it is what the picker and the model read."""
    global checks
    skills_dir = os.path.join(ROOT, "skills")
    if not os.path.isdir(skills_dir):
        fail("missing directory: skills/")
        return

    for name in sorted(os.listdir(skills_dir)):
        if not name.endswith(".md"):
            continue
        checks += 1
        with open(os.path.join(skills_dir, name), encoding="utf-8") as fh:
            head = fh.read(600)
        if not head.startswith("---"):
            fail(f"skills/{name}: no YAML frontmatter block")
        elif "description:" not in head:
            fail(f"skills/{name}: frontmatter has no 'description'")


def check_wiring():
    """The pieces that make this a system rather than ten unrelated prompts."""
    global checks

    checks += 1
    if not os.path.exists(os.path.join(ROOT, "memory", "decisions", "README.md")):
        fail("missing memory/decisions/README.md — the decision memory contract")

    # Skills that must read and write decision memory for the learning loop to close.
    for name in ("council.md", "thesis.md", "checklist.md"):
        checks += 1
        path = os.path.join(ROOT, "skills", name)
        if not os.path.exists(path):
            fail(f"missing skills/{name}")
            continue
        with open(path, encoding="utf-8") as fh:
            body = fh.read()
        if "memory/decisions" not in body:
            fail(f"skills/{name}: not wired to memory/decisions — the loop is broken")

    # Analytical skills must defer to one sourcing standard rather than inventing their own.
    for name in ("council.md", "deep-dive.md", "earnings.md", "screen.md"):
        checks += 1
        path = os.path.join(ROOT, "skills", name)
        if os.path.exists(path):
            with open(path, encoding="utf-8") as fh:
                if "data-standards" not in fh.read():
                    warn(f"skills/{name}: does not reference skills/data-standards.md")


def check_mcp():
    global checks
    config = load_json(os.path.join(ROOT, ".mcp.json"), required=False)
    if config is None:
        return
    servers = config.get("mcpServers", {})
    checks += 1
    if not servers:
        fail(".mcp.json: 'mcpServers' is empty")
    for name, spec in servers.items():
        checks += 1
        if not spec.get("command") and not spec.get("url"):
            fail(f".mcp.json: server '{name}' has neither 'command' nor 'url'")


def check_english_only():
    """This repository ships in English. Enforce it mechanically."""
    global checks
    for current, dirs, files in os.walk(ROOT):
        dirs[:] = [d for d in dirs if d not in SKIP_DIRS]
        for name in files:
            if not name.endswith(TEXT_SUFFIXES):
                continue
            path = os.path.join(current, name)
            checks += 1
            try:
                with open(path, encoding="utf-8") as fh:
                    content = fh.read()
            except (UnicodeDecodeError, OSError):
                continue
            for number, line in enumerate(content.splitlines(), 1):
                hit = NON_ENGLISH.search(line)
                if hit:
                    fail(f"non-English character {hit.group()!r} at {rel(path)}:{number}")
                    break


def main():
    print("=" * 66)
    print("value-council — repository check")
    print("=" * 66)

    check_plugin_manifest()
    check_marketplace()
    check_skill_frontmatter()
    check_wiring()
    check_mcp()
    check_english_only()

    print(f"  checks run: {checks}")
    for message in warnings:
        print(f"  warn  {message}")

    if failures:
        print(f"\n  {len(failures)} failure(s):")
        for message in failures:
            print(f"    - {message}")
        print("\nBLOCKED — fix the above before committing.")
        return 1

    print("\n  All checks passed. Ready to publish.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
