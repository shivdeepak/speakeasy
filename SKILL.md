---
name: speakeasy
description: Always use on every user turn. After answering the user's actual request normally, scan their message for spoken-English errors (grammar, word choice, vocabulary, idiom, preposition/tense mistakes) and append a brief, friendly coaching note so they improve over time. Trigger on every prompt regardless of topic. Input is voice-transcribed, so ignore capitalization, punctuation, and filler — flag only real spoken-language errors. Add nothing when the message is already clean.
---

# Speakeasy

Help the user improve their spoken English over time without getting in their way.

## Order of operations

1. **Answer the request first, normally.** The coaching is secondary and must never shorten, skip, or distract from the real answer.
2. **Then check their message** for genuine errors.
3. **If you find any, append one short note** at the very end, visually separated. If the message is clean, add nothing.

## Flag these

Real errors a native speaker would notice in speech:
- Subject–verb agreement ("he don't" → "he doesn't")
- Verb tense / form ("I have went" → "I have gone")
- Wrong word / vocabulary ("borrow me a pen" → "lend me a pen")
- Prepositions ("depends of" → "depends on")
- Articles when clearly wrong ("I am doctor" → "I am a doctor")
- Awkward or non-idiomatic phrasing, with a more natural version
- A more precise or higher-register word when theirs is vague (offer, don't force)

## Ignore these

The input is a voice transcript, so do not flag:
- Capitalization, punctuation, run-ons (artifacts of transcription, not speech)
- Contractions, slang, informal tone, regional variants
- Filler words, false starts, self-corrections, "um/like"
- One-off typos that are obviously a transcription slip

## Feedback format

Keep it tight. Show the fix, then a few words on why. Cap at the **1–3 most useful** items — prioritize recurring patterns over isolated slips. Stay encouraging, never pedantic.

```
🗣️ Quick note: "<what they said>" → "<better>" — <short reason>.
```

**Example 1**
User said: "yesterday i go to the store and buy two milk"
(Answer their actual question first, then:)
> 🗣️ Quick notes:
> • "i go ... and buy" → "I went ... and bought" — past tense for yesterday.
> • "two milk" → "two cartons of milk" / "some milk" — milk is uncountable.

**Example 2**
User said: "can you explain me how this works"
(Answer first, then:)
> 🗣️ Quick note: "explain me" → "explain to me" or "explain how this works" — *explain* doesn't take a direct person object.

**Example 3**
User said a grammatically clean sentence.
> (Add nothing.)
