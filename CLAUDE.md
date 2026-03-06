# Italian Learning Project

A structured Italian learning system. Claude Code acts as a tutor, generating exercises and reviewing answers.

## Project Structure

- `grammar.md` — Grammar rules to teach and test (A1 level, expandable)
- `vocabulary.md` — Vocabulary organized by category (expandable)
- `exercises/` — Exercise files, one per session, named `YYYY-MM-DD.md`
- `issues/rating.md` — Tracked weak areas, strengths, and study recommendations
- `issues/level.md` — CEFR level assessment, untested areas, and next-level requirements

## Commands

- `/exercise` — Generate 20 German→Italian translation sentences
- `/review` — Grade a completed exercise and update rating/level tracking
- `/drill` — Generate 10 focused exercises on the top weak area
- `/redo` — Rephrase wrong answers from the last exercise as new exercises
- `/listen` — Generate an audio listening exercise using Google TTS

## Shared Conventions

- **Date suffixes:** If a file for today already exists, append a letter suffix (e.g. `2026-02-21b.md`)
- **Answer format:** Users fill in answers on `> ` lines
- **Exercise language:** Always German→Italian (user translates into Italian)
- **Grading guidelines:**
  - Accept minor typos if meaning is clear, but note them
  - Accept valid alternative translations
  - Explain grammar mistakes clearly and concisely
  - Be encouraging but honest
