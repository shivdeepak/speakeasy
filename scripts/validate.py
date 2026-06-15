#!/usr/bin/env python3
"""Validate a skill directory for cross-platform portability."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

DESCRIPTION_MAX_SPEC = 1024
DESCRIPTION_MAX_UPLOAD = 200
BODY_MAX_LINES = 500
NAME_PATTERN = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")


def parse_frontmatter(content: str) -> tuple[dict[str, str], str]:
    if not content.startswith("---"):
        raise ValueError("SKILL.md must start with YAML frontmatter (---)")

    end = content.find("\n---", 3)
    if end == -1:
        raise ValueError("SKILL.md frontmatter is not closed with ---")

    raw = content[3:end].strip()
    body = content[end + 4 :].lstrip("\n")

    fields: dict[str, str] = {}
    current_key: str | None = None
    current_lines: list[str] = []
    skip_children = False

    def flush() -> None:
        nonlocal current_key, current_lines
        if current_key is None:
            return
        value = "\n".join(current_lines).strip()
        if value.startswith('"') and value.endswith('"'):
            value = value[1:-1]
        elif value.startswith("'") and value.endswith("'"):
            value = value[1:-1]
        fields[current_key] = " ".join(value.split())
        current_key = None
        current_lines = []

    for line in raw.splitlines():
        if not line.strip():
            if current_key is not None and not skip_children:
                current_lines.append("")
            continue

        if line.startswith(" "):
            if skip_children:
                continue
            if current_key is not None:
                current_lines.append(line.strip())
                continue

        flush()
        skip_children = False
        if ":" not in line:
            raise ValueError(f"Invalid frontmatter line: {line!r}")
        key, value = line.split(":", 1)
        current_key = key.strip()
        stripped = value.strip()
        if stripped in {">", ">-", ">+", "|", "|-", "|+"}:
            current_lines = []
        elif not stripped:
            # Key with no inline value: treat as a nested map (e.g. metadata:)
            # and skip its indented children so they are not mis-joined.
            fields[current_key] = ""
            current_key = None
            current_lines = []
            skip_children = True
        else:
            current_lines = [stripped]

    flush()
    return fields, body


def validate_skill(skill_path: Path) -> tuple[list[str], dict[str, str]]:
    errors: list[str] = []
    fields: dict[str, str] = {}

    if not skill_path.is_dir():
        return [f"Not a directory: {skill_path}"], fields

    skill_md = skill_path / "SKILL.md"
    if not skill_md.is_file():
        return [f"Missing SKILL.md in {skill_path}"], fields

    content = skill_md.read_text(encoding="utf-8")
    try:
        fields, body = parse_frontmatter(content)
    except ValueError as exc:
        return [str(exc)], fields

    name = fields.get("name", "").strip()
    description = fields.get("description", "").strip()
    folder_name = skill_path.name

    if not name:
        errors.append("Frontmatter missing required field: name")
    elif name != folder_name:
        errors.append(
            f"name {name!r} must match parent directory {folder_name!r}"
        )
    elif not NAME_PATTERN.match(name):
        errors.append(
            f"name {name!r} must be lowercase letters, numbers, and hyphens only"
        )

    if not description:
        errors.append("Frontmatter missing required field: description")
    else:
        if "<" in description or ">" in description:
            errors.append("description must not contain XML tags (< or >)")
        if len(description) > DESCRIPTION_MAX_SPEC:
            errors.append(
                f"description is {len(description)} chars; max is {DESCRIPTION_MAX_SPEC}"
            )
        if len(description) > DESCRIPTION_MAX_UPLOAD:
            errors.append(
                f"description is {len(description)} chars; Claude Web/Cowork max is "
                f"{DESCRIPTION_MAX_UPLOAD}"
            )

    for key, value in fields.items():
        if "<" in value or ">" in value:
            errors.append(f"frontmatter field {key!r} must not contain XML tags")

    body_lines = body.splitlines()
    if len(body_lines) > BODY_MAX_LINES:
        errors.append(
            f"SKILL.md body is {len(body_lines)} lines; recommended max is {BODY_MAX_LINES}"
        )

    return errors, fields


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate an Agent Skills directory")
    parser.add_argument(
        "skill_path",
        nargs="?",
        default="speakeasy",
        help="Path to skill directory (default: speakeasy)",
    )
    args = parser.parse_args()

    skill_path = Path(args.skill_path).resolve()
    errors, fields = validate_skill(skill_path)

    if errors:
        print(f"Validation failed for {skill_path}:", file=sys.stderr)
        for error in errors:
            print(f"  - {error}", file=sys.stderr)
        return 1

    name = fields.get("name", skill_path.name)
    desc_len = len(fields.get("description", ""))
    print(f"OK: {name} ({desc_len}-char description, upload-safe)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
