# Speakeasy

A lightweight Claude skill that quietly coaches your spoken English. It runs on
every turn: Claude answers your actual question first, then — only when there's
something worth mentioning — appends a short, friendly note on grammar, word
choice, or phrasing so your conversation skills improve over time.

It's built for voice input. Because your messages are assumed to be
voice-transcribed, Speakeasy ignores capitalization, punctuation, filler words
("um", "uh"), and false starts, and flags only genuine spoken-English errors.

## What it does

- Answers your request normally, every time — the coaching never replaces or
  shortens the real answer.
- Appends a brief note **only** when it spots a real error; clean messages get
  nothing back.
- Caps feedback at the 1–3 most useful items and favors recurring patterns over
  one-off slips, so it stays encouraging rather than pedantic.

## What it flags

Subject–verb agreement, verb tense/form, wrong-word or vocabulary mistakes,
prepositions, clearly wrong articles, and awkward or non-idiomatic phrasing
(with a more natural alternative).

## What it ignores

Capitalization, punctuation, run-ons, contractions, slang, regional variants,
filler words, self-corrections, and obvious transcription typos — none of these
are spoken-language errors.

## Example

> **You:** can you explain me how this works
>
> **Claude:** *(answers the question in full, then:)*
>
> 🗣️ Quick note: "explain me" → "explain to me" or "explain how this works" —
> *explain* doesn't take a direct person object.

## Installation

Download `speakeasy.skill` and upload it wherever your Claude environment loads
skills, or drop the `speakeasy/` folder (containing `SKILL.md`) into your skills
directory. Once installed, it activates automatically — no command needed.

## How it works

The skill is a single `SKILL.md` file. Its frontmatter description is what tells
Claude when to use it; the body holds the coaching rules. It's intentionally
tiny, since the skill loads on every turn and token efficiency matters.

## License

MIT — feel free to use, modify, and share.
