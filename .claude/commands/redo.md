Generate a redo exercise from wrong answers in the most recent reviewed exercise.

1. Find the most recent reviewed exercise file in `exercises/` (not `exercises/archive/`) that has ✗ marks (or use a file specified by the user: $ARGUMENTS)
2. Read `issues/tracking.md` for context on recurring weak areas
3. Extract all sentences the user got wrong (marked with ✗)
4. For each wrong answer, create a **new sentence in German** that tests the **same grammar point** — do not repeat the original sentence verbatim. The user translates to Italian.
5. Create a redo file in `exercises/` named `redo-YYYY-MM-DD.md` (using today's date). If one already exists, append a letter suffix (e.g. `redo-2026-02-21b.md`).
6. Use this exact format:

```
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

The user fills in answers on the blank `> ` lines. Use `/review` to grade the completed redo.
