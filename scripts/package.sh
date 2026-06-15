#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
SKILL_DIR="${SKILL_DIR:-$ROOT/speakeasy}"
OUTPUT_DIR="${OUTPUT_DIR:-$ROOT/dist}"

python3 "$ROOT/scripts/validate.py" "$SKILL_DIR"

mkdir -p "$OUTPUT_DIR"
SKILL_NAME="$(basename "$SKILL_DIR")"
OUTPUT_FILE="$OUTPUT_DIR/$SKILL_NAME.skill"

rm -f "$OUTPUT_FILE"
(
  cd "$(dirname "$SKILL_DIR")"
  zip -r -q "$OUTPUT_FILE" "$SKILL_NAME"
)

echo "Packaged: $OUTPUT_FILE"
