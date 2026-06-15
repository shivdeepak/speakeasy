# Speakeasy

A lightweight agent skill that quietly coaches your spoken English. It runs on
every turn: the agent answers your actual question first, then — only when there
is something worth mentioning — appends a short, friendly note on grammar, word
choice, or phrasing.

Built for voice input. Because messages are assumed to be voice-transcribed,
Speakeasy ignores capitalization, punctuation, filler words ("um", "uh"), and
false starts, and flags only genuine spoken-English errors.

## What it does

- Answers your request normally every time — coaching never replaces or shortens
  the real answer
- Appends a brief note **only** when it spots a real error; clean messages get
  nothing
- Caps feedback at 1–3 useful items and favors recurring patterns over one-off
  slips

## Example

> **You:** can you explain me how this works
>
> **Agent:** *(answers the question in full, then:)*
>
> 🗣️ Quick note: "explain me" → "explain to me" or "explain how this works" —
> *explain* doesn't take a direct person object.

## Installation

The skill lives in [`speakeasy/SKILL.md`](speakeasy/SKILL.md). How you install
it
depends on the surface.

### Download (Claude Web and Cowork)

These surfaces upload a packaged `.skill` file. Download the latest build:

```text
https://github.com/shivdeepak/speakeasy/releases/latest/download/speakeasy.skill
```

- **Claude Web:** Settings → Capabilities → Upload skill → enable the toggle
  (requires code execution on your plan)
- **Claude Cowork:** Customize → Skills → Upload (desktop app only)

The released file is built and validated by CI on every merge to `main`.

### Install via command (no download)

These surfaces read the skill from the filesystem or your repo.

| Surface | Command |
|---------|---------|
| **Cursor** | `npx skills add shivdeepak/speakeasy -g -a cursor -y` or `cp -r speakeasy ~/.cursor/skills/speakeasy` |
| **Claude Code** | `npx skills add shivdeepak/speakeasy -g -a claude-code -y` or `cp -r speakeasy ~/.claude/skills/speakeasy` |
| **Cursor Cloud Agents / team** | Commit `.cursor/skills/speakeasy/` (copy of `speakeasy/`) into the target repo |

### Optional always-on backup

Skills are description-triggered and may not fire every turn on all surfaces. If
coaching feels inconsistent, add **one** of these — not the skill and a snippet
together:

| Surface | File | Action |
|---------|------|--------|
| Cursor | [`snippets/cursor-rule.mdc`](snippets/cursor-rule.mdc) | Copy into `~/.cursor/rules/` **only if** the skill is not installed |
| Claude Code | [`snippets/claude-md.md`](snippets/claude-md.md) | Append the one-liner to `~/.claude/CLAUDE.md` or project `CLAUDE.md` |

## Development / maintainers

The scripts under `scripts/` are dev and CI helpers — end users do not need
them.

```bash
# Validate structure and description length (≤200 chars for upload surfaces)
python3 scripts/validate.py speakeasy

# Build dist/speakeasy.skill locally (CI does this on merge to main)
./scripts/package.sh

# Install into local Cursor / Claude Code dirs while developing
./scripts/install.sh --all-personal
```

Make scripts executable once: `chmod +x scripts/*.sh`

## Troubleshooting

| Problem | Fix |
|---------|-----|
| Skill not firing | Strengthen the `description` in frontmatter; try an optional companion snippet (skill **or** snippet, not both) |
| Double coaching notes | Remove duplicate Cursor user rules; use either the skill or `snippets/cursor-rule.mdc` |
| Upload rejected | The released `speakeasy.skill` already passed `validate.py` in CI; re-download the latest release. If building locally, run `python3 scripts/validate.py speakeasy` and confirm the zip contains `speakeasy/SKILL.md` at its root |
| Install path wrong | Cursor: `~/.cursor/skills/` or `.cursor/skills/`; Claude Code: `~/.claude/skills/` or `.claude/skills/` |

## How it works

The skill is a single `SKILL.md` in the [Agent
Skills](https://agentskills.io/specification) format. Frontmatter `description`
tells agents when to load it; the body holds coaching rules. It stays small
because metadata loads on every turn.

## License

MIT — see [LICENSE](LICENSE).
