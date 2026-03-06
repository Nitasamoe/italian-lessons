Review a completed Italian exercise.

**Files to read:** `issues/rating.md`, `issues/level.md`
**Do NOT read:** `grammar.md`, `vocabulary.md` (not needed for grading)

1. Find the most recent exercise file in `exercises/` (or use a file specified by the user: $ARGUMENTS)
2. Read the exercise file — the user will have filled in answers on the `> ` lines
3. For each sentence, evaluate the translation **inline, directly under the user's answer** in the exercise file. Do NOT use a separate Review section. Place the correction on a line starting with `>` right below the user's answer:

```
1. [Original sentence]
   > [user's answer]
   > ✓ Correct.

2. [Original sentence]
   > [user's answer]
   > ✗ "Io vado a la scuola" → "Io vado a scuola" — no article after "a" with "scuola"
```

Then append a `## Summary` section at the end:

```
## Summary
X/20 correct. [Brief summary of patterns observed.]
```

4. After reviewing, update `issues/rating.md`:
   - List current weak areas with examples
   - List strengths
   - Provide study recommendations
   - Track progress over time (compare with previous ratings if they exist)

5. After reviewing, update the **Error Tracker** table in `issues/rating.md`:
   - For each error, find or create a row in the Error Tracker table
   - Increment the "Total Errors" count
   - Update "Last Seen" to the exercise date
   - Update "Examples" with the most recent example

6. After reviewing, update `issues/level.md`:
   - Reassess the current CEFR level based on cumulative performance
   - Move topics between "Not Yet Tested" and "Demonstrated" as they get exercised
   - Update accuracy trends and progress percentages
   - Check off completed requirements for the next level
   - Adjust the overall "Progress Toward A2" percentage
   - For listen exercises: update the "Listening comprehension" row in the progress table with the latest score and trend

**Grading guidelines:**
- Accept minor typos if the meaning is clear, but note them
- Accept valid alternative translations
- Explain grammar mistakes clearly and concisely
- Be encouraging but honest

**Grading listen exercises (title starts with "# Listen"):**
- Extract correct answers from the `<!-- ANSWER KEY -->` HTML comment at the bottom of the file
- Compare the user's transcription against the answer key
- Extract replay counts from `<!-- REPLAY COUNTS: ... -->` if present. In the Summary, note which sentences needed the most replays — these indicate difficult-to-parse phrases worth revisiting
- **Lenient on:** missing/wrong accent marks (è vs e, à vs a — hard to distinguish by ear)
- **Strict on:** actual words, word forms, word order
- **Highlight:** homophones and near-homophones as learning opportunities (anno/hanno, uova/uva)
