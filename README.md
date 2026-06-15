# Speakeasy

An [Agent Skill](https://agentskills.io/specification) (Cursor, Claude Code,
Claude Web, Cowork) that quietly coaches your spoken English. It runs on every
turn: the agent answers your actual question first, then — only when there is
something worth mentioning — appends a short, friendly note on grammar, word
choice, or phrasing.

Built for voice input. Because messages are assumed to be voice-transcribed,
Speakeasy ignores capitalization, punctuation, filler words ("um", "uh"), and
false starts, and flags only genuine spoken-English errors.

Packaged with [skillship](https://github.com/shivdeepak/skillship) for
cross-surface distribution.

## Installation

### Cursor and Claude Code

Install via [skillship](https://github.com/shivdeepak/skillship) (requires
Node.js >= 18):

```bash
npx skillship@latest install shivdeepak/speakeasy -a cursor -a claude-code
```

Or install directly with the `skills` CLI:

```bash
npx skills add shivdeepak/speakeasy
```

### Claude Web and Cowork

These surfaces upload a packaged `.skill` file. Download the latest build:

```text
https://github.com/shivdeepak/speakeasy/releases/latest/download/speakeasy.skill
```

- **Claude Web:** Settings → Capabilities → Upload skill → enable the toggle
  (requires code execution on your plan)
- **Claude Cowork:** Customize → Skills → Upload (desktop app only)

## What it does

- Answers your request normally every time — coaching never replaces or shortens
  the real answer
- Appends a brief note **only** when it spots a real error; clean messages get
  nothing
- Caps feedback at 1–3 useful items and favors recurring patterns over one-off
  slips
- Ignores transcription artifacts: capitalization, punctuation, filler, and
  false starts

## Example

> **You:** can you explain me how this works
>
> **Agent:** *(answers the question in full, then:)*
>
> 🗣️ Quick note: "explain me" → "explain to me" or "explain how this works" —
> *explain* doesn't take a direct person object.

## Optional always-on backup

Skills are description-triggered and may not fire every turn on all surfaces. If
coaching feels inconsistent, add **one** of these — not the skill and a snippet
together:

| Surface | File | Action |
|---------|------|--------|
| Cursor | [`snippets/cursor-rule.mdc`](snippets/cursor-rule.mdc) | Copy into `~/.cursor/rules/` **only if** the skill is not installed |
| Claude Code | [`snippets/claude-md.md`](snippets/claude-md.md) | Append the one-liner to `~/.claude/CLAUDE.md` or project `CLAUDE.md` |

## How it works

The skill is a single [`speakeasy/SKILL.md`](speakeasy/SKILL.md) in the
[Agent Skills](https://agentskills.io/specification) format. The frontmatter
`description` tells agents when to load it; the body holds the coaching rules.
It stays small because the metadata loads on every turn.

## Troubleshooting

| Problem | Fix |
|---------|-----|
| Skill not firing | Add an optional companion snippet (skill **or** snippet, not both) |
| Double coaching notes | Remove duplicate Cursor user rules; use either the skill or `snippets/cursor-rule.mdc` |
| Upload rejected | Re-download the latest `speakeasy.skill` release; it is built and validated in CI |
| Install path wrong | Cursor: `~/.cursor/skills/` or `.cursor/skills/`; Claude Code: `~/.claude/skills/` or `.claude/skills/` |

## Development / maintainers

Validation, packaging, and releases are handled by
[skillship](https://github.com/shivdeepak/skillship) and
[release-please](https://github.com/googleapis/release-please-action). See
[`AGENTS.md`](AGENTS.md) for commit conventions and tooling — end users don't
need any of it.

## License

MIT — see [LICENSE](LICENSE).
