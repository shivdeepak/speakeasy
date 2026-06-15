#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
SKILL_DIR="${SKILL_DIR:-$ROOT/speakeasy}"
SKILL_NAME="$(basename "$SKILL_DIR")"
USE_SYMLINK=0

usage() {
  cat <<EOF
Usage: $(basename "$0") [OPTIONS]

Install the skill to Cursor and/or Claude Code skill directories.

Options:
  --cursor-personal    Install to ~/.cursor/skills/$SKILL_NAME
  --cursor-project     Install to .cursor/skills/$SKILL_NAME (current directory)
  --claude-personal    Install to ~/.claude/skills/$SKILL_NAME
  --claude-project     Install to .claude/skills/$SKILL_NAME (current directory)
  --all-personal       Install to both personal directories
  --symlink            Symlink instead of copy
  -h, --help           Show this help

Examples:
  $(basename "$0") --all-personal
  $(basename "$0") --cursor-project --claude-project
EOF
}

install_one() {
  local target_parent="$1"
  local target="$target_parent/$SKILL_NAME"

  mkdir -p "$target_parent"
  rm -rf "$target"

  if [[ "$USE_SYMLINK" -eq 1 ]]; then
    ln -s "$SKILL_DIR" "$target"
    echo "Linked $SKILL_DIR -> $target"
  else
    cp -R "$SKILL_DIR" "$target"
    echo "Copied $SKILL_DIR -> $target"
  fi
}

TARGETS=()

while [[ $# -gt 0 ]]; do
  case "$1" in
    --cursor-personal) TARGETS+=("$HOME/.cursor/skills") ;;
    --cursor-project) TARGETS+=("$PWD/.cursor/skills") ;;
    --claude-personal) TARGETS+=("$HOME/.claude/skills") ;;
    --claude-project) TARGETS+=("$PWD/.claude/skills") ;;
    --all-personal)
      TARGETS+=("$HOME/.cursor/skills" "$HOME/.claude/skills")
      ;;
    --symlink) USE_SYMLINK=1 ;;
    -h | --help)
      usage
      exit 0
      ;;
    *)
      echo "Unknown option: $1" >&2
      usage >&2
      exit 1
      ;;
  esac
  shift
done

if [[ ${#TARGETS[@]} -eq 0 ]]; then
  echo "No install target selected." >&2
  usage >&2
  exit 1
fi

python3 "$ROOT/scripts/validate.py" "$SKILL_DIR"

SEEN=()
for target_parent in "${TARGETS[@]}"; do
  skip=0
  for done_target in "${SEEN[@]:-}"; do
    if [[ "$done_target" == "$target_parent" ]]; then
      skip=1
      break
    fi
  done
  [[ "$skip" -eq 1 ]] && continue
  SEEN+=("$target_parent")
  install_one "$target_parent"
done
