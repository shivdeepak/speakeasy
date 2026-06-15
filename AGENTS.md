# Agent instructions

## Commit conventions

This repo releases via
[release-please](https://github.com/googleapis/release-please-action),
which derives versions from commit messages. Commits on `main` MUST follow
[Conventional Commits](https://www.conventionalcommits.org/).

Format: `<type>[optional scope][!]: <description>`

Common types:

- `feat:` — new user-facing behavior (triggers a minor bump)
- `fix:` — bug fix (patch bump)
- `docs:` — documentation only
- `refactor:` — code change that neither fixes a bug nor adds a feature
- `perf:` — performance improvement
- `ci:` — CI/workflow changes (hidden from changelog)
- `chore:` — tooling/maintenance (hidden from changelog)

Breaking changes: append `!` after the type (e.g. `feat!:`) or add a
`BREAKING CHANGE:` footer. This triggers a major bump.

Rules:

- Keep the description in the imperative mood, lower-case, no trailing period.
- One logical change per commit; do not mix unrelated changes.
- Do NOT bump versions, edit `version.txt`, `.release-please-manifest.json`, or
  the
  `# x-release-please-version` line by hand — release-please owns these.

Examples:

```
feat: flag missing articles in spoken English
fix: stop double coaching when the same error repeats
docs: clarify Claude Web upload steps
feat!: change feedback format to a single inline note
```

## Portability tooling

Validation, packaging, and install are delegated to
[`skillship`](https://github.com/shivdeepak/skillship), a standalone
skill-agnostic CLI, invoked via `npx skillship <command>`. This repo holds no
local packaging scripts; CI calls `skillship` directly. Change behavior there,
not here.
