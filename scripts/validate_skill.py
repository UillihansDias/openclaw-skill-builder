#!/usr/bin/env python3
"""Validate an OpenClaw AgentSkill directory."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

JUNK_NAMES = {
    ".DS_Store", "Thumbs.db", "desktop.ini",
}
JUNK_DIRS = {
    ".git", "__MACOSX", "__pycache__", ".pytest_cache", ".mypy_cache",
}
DECORATIVE = {
    "README.md", "CHANGELOG.md", "NOTES.md", "IDEAS.md",
}
PLACEHOLDER_PATTERNS = (
    r"\bTODO\b",
    r"\[PLACEHOLDER\]",
    r"your" + r"-skill-name",
)


def parse_frontmatter(text: str) -> tuple[dict[str, str], list[str]]:
    errors: list[str] = []
    if not text.startswith("---\n"):
        return {}, ["SKILL.md must start with YAML frontmatter"]
    end = text.find("\n---", 4)
    if end < 0:
        return {}, ["SKILL.md frontmatter is not closed"]
    block = text[4:end]
    data: dict[str, str] = {}
    for line in block.splitlines():
        if not line.strip() or line.startswith((" ", "\t")):
            continue
        if ":" not in line:
            errors.append(f"invalid frontmatter line: {line}")
            continue
        key, value = line.split(":", 1)
        data[key.strip()] = value.strip()
    return data, errors


def validate(root: Path) -> list[str]:
    errors: list[str] = []
    if not root.is_dir():
        return [f"not a directory: {root}"]

    skill_file = root / "SKILL.md"
    if not skill_file.is_file():
        return ["SKILL.md is missing at the skill root"]

    text = skill_file.read_text(encoding="utf-8")
    frontmatter, fm_errors = parse_frontmatter(text)
    errors.extend(fm_errors)

    name = frontmatter.get("name", "")
    description = frontmatter.get("description", "")
    if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", name):
        errors.append("frontmatter name must be a lowercase hyphenated slug")
    if name and root.name != name:
        errors.append(f"folder name '{root.name}' does not match frontmatter name '{name}'")
    if not (len(description) >= 2 and description[0] == description[-1] and description[0] in "\"'"):
        errors.append("frontmatter description must be quoted")
    if "metadata" in frontmatter and not frontmatter["metadata"]:
        errors.append("empty metadata key is not allowed")

    files = [p for p in root.rglob("*") if p.is_file()]
    dirs = [p for p in root.rglob("*") if p.is_dir()]

    for path in files:
        rel = path.relative_to(root).as_posix()
        if path.name in JUNK_NAMES or any(part in JUNK_DIRS for part in path.parts):
            errors.append(f"junk file or path: {rel}")
        if path.name in DECORATIVE:
            errors.append(f"decorative file requires explicit justification: {rel}")
        if path != skill_file and rel not in text:
            errors.append(f"support file is not referenced from SKILL.md: {rel}")
        try:
            content = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            content = ""
        for pattern in PLACEHOLDER_PATTERNS:
            if re.search(pattern, content, re.IGNORECASE):
                errors.append(f"unresolved placeholder in {rel}: {pattern}")

    for directory in dirs:
        if not any(directory.iterdir()):
            errors.append(f"empty directory: {directory.relative_to(root).as_posix()}")

    return errors


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("skill_directory", type=Path)
    args = parser.parse_args()
    errors = validate(args.skill_directory.resolve())
    if errors:
        for error in errors:
            print(f"FAIL: {error}")
        return 1
    print("PASS: skill package structure is valid")
    return 0


if __name__ == "__main__":
    sys.exit(main())
