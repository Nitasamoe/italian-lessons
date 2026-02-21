# Italian Learning Project

This project is a structured Italian learning system. Claude Code acts as a tutor, generating exercises and reviewing answers.

## Project Structure

- `grammar.md` — Grammar rules to teach and test (A1 level, expandable)
- `vocabulary.md` — Vocabulary organized by category (expandable)
- `exercises/` — Exercise files, one per session, named `YYYY-MM-DD.md`
- `issues/rating.md` — Tracked weak areas, strengths, and study recommendations

## Custom Commands

### /exercise

Generate a new exercise file in `exercises/YYYY-MM-DD.md` (using today's date).

**Process:**
1. Read `grammar.md`, `vocabulary.md`, and `issues/rating.md`
2. Generate an exercise file containing:
   - **Part 1: German → Italian** — 10 sentences in German to translate into Italian
   - **Part 2: Italian → German** — 10 sentences in Italian to translate into German
3. Sentences must:
   - Be at A1 beginner level
   - Be based on the grammar rules and vocabulary in the project files
   - Target weak areas identified in `issues/rating.md`
   - Mix new material with reinforcement of previous weak spots
   - Adapt difficulty and topics based on the current rating
4. Use this format:

```markdown
# Exercise — YYYY-MM-DD

## Part 1: German → Italian
Translate the following sentences into Italian.

1. [German sentence]
   >

2. [German sentence]
   >

(... 10 sentences total)

## Part 2: Italian → German
Translate the following sentences into German.

1. [Italian sentence]
   >

2. [Italian sentence]
   >

(... 10 sentences total)
```

The user fills in answers on the `> ` lines.

If an exercise for today already exists, append a letter suffix (e.g. `2026-02-21b.md`).

### /review

Review a completed exercise file.

**Process:**
1. Find the most recent exercise file in `exercises/` (or use a specified file if the user provides one)
2. Read the exercise file — the user will have filled in answers on the `> ` lines
3. For each sentence, evaluate the translation **inline, directly under the user's answer** in the exercise file. Do NOT use a separate Review section. Place the correction on a line starting with `>` right below the user's answer:

```markdown
1. [Original sentence]
   > [user's answer]
   > ✓ Correct.

2. [Original sentence]
   > [user's answer]
   > ✗ "Io vado a la scuola" → "Io vado a scuola" — no article after "a" with "scuola"
```

Then append a `## Summary` section at the end:

```markdown
## Summary
X/20 correct. [Brief summary of patterns observed.]
```

4. After reviewing, update `issues/rating.md`:
   - List current weak areas with examples
   - List strengths
   - Provide study recommendations
   - Track progress over time (compare with previous ratings if they exist)

4b. After reviewing, update the **Error Tracker** table in `issues/rating.md`:
   - For each error, find or create a row in the Error Tracker table
   - Increment the "Total Errors" count
   - Update "Last Seen" to the exercise date
   - Update "Examples" with the most recent example

**Grading guidelines:**
- Accept minor typos if the meaning is clear, but note them
- Accept valid alternative translations
- Explain grammar mistakes clearly and concisely
- Be encouraging but honest

### /drill

Generate a focused drill exercise targeting the #1 weak area from `issues/rating.md`.

**Process:**
1. Read `issues/rating.md` and identify the top weak area (highest error count or marked CRITICAL)
2. Generate 10 short, focused exercises in `exercises/drill-YYYY-MM-DD.md` (using today's date)
3. Exercise types (pick the most appropriate for the weak area):
   - **Fill-in-the-blank:** "Il caffè ___ buono." (è / e)
   - **Conjugation completion:** "dormire → loro ___"
   - **Article selection:** "___ studenti vanno a scuola." (i / gli / lo)
   - **Correction:** "Io dormanno bene." → Fix the error.
   - **Choose the correct form:** "Lei (parla / parlano) italiano."
4. Use this format:

```markdown
# Drill — YYYY-MM-DD — [Topic Name]

Focus: [description of the weak area being drilled]

1. [exercise prompt]
   >

2. [exercise prompt]
   >

(... 10 exercises total)
```

The user fills in answers on the `> ` lines.

If a drill for today already exists, append a letter suffix (e.g. `drill-2026-02-21b.md`).

**Reviewing drills:** Use `/review` — it works the same way for drill files.

### /redo

Generate a redo exercise from wrong answers in the most recent reviewed exercise.

**Process:**
1. Find the most recent reviewed exercise file in `exercises/` (one that has ✗ marks)
2. Extract all sentences the user got wrong (marked with ✗)
3. For each wrong answer, create a **new sentence** that tests the **same grammar point** — do not repeat the original sentence verbatim
4. Generate the redo file in `exercises/redo-YYYY-MM-DD.md` (using today's date)
5. Use this format:

```markdown
# Redo — YYYY-MM-DD — Based on [original exercise filename]

Rephrased exercises targeting your mistakes from the last session.

1. [New sentence testing the same grammar point as original mistake]
   > Original error: [brief description of what went wrong]
   >

2. [New sentence testing the same grammar point as original mistake]
   > Original error: [brief description of what went wrong]
   >

(... one exercise per original mistake)
```

The user fills in answers on the blank `> ` lines.

If a redo for today already exists, append a letter suffix (e.g. `redo-2026-02-21b.md`).

**Reviewing redos:** Use `/review` — it works the same way for redo files.
