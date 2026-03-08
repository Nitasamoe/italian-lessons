# Italian Lessons

A structured Italian learning system powered by Claude Code. It generates translation exercises, reviews your answers, tracks your weak areas, and adapts to help you improve.

## Setup

1. Install [Claude Code](https://claude.com/claude-code)
2. Clone this repo and `cd` into it
3. Start a session with `claude`

## How It Works

You learn by doing translation exercises (German <-> Italian). Claude generates sentences based on your current level, reviews your answers, and tracks what you need to practice.

### Commands

| Command     | What it does |
|-------------|-------------|
| `/exercise` | Generate a new 20-sentence translation exercise (10 DE→IT, 10 IT→DE) |
| `/review`   | Grade your completed exercise, update your error tracker |
| `/drill`    | Generate 10 focused mini-exercises on your #1 weak area |
| `/redo`     | Rephrase your wrong answers from the last exercise into new sentences |

### Typical Workflow

1. **`/exercise`** — generates `exercises/2026-02-21.md`
2. Open the file and fill in your translations on the `> ` lines
3. **`/review`** — grades inline, updates `issues/tracking.md`
4. **`/drill`** — if you want focused practice on a specific weak point
5. **`/redo`** — if you want to retry your mistakes with fresh sentences

## Project Structure

```
grammar.md          — Grammar rules and verb conjugation tables
vocabulary.md       — Vocabulary by category (verbs, food, colors, etc.)
issues/tracking.md  — Error tracker, progress history, study recommendations
issues/archive.md   — Resolved/mastered errors (reference only)
exercises/          — Active exercise files (current session)
exercises/archive/  — Completed exercises (reference only)
CLAUDE.md           — Instructions for Claude Code (command definitions)
```

## Customizing

- Add vocabulary to `vocabulary.md` — Claude will use it in exercises
- Add grammar rules to `grammar.md` — Claude will test them
- Edit `issues/tracking.md` to manually adjust priorities
