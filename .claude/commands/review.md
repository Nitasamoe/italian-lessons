Review a completed Italian exercise.

1. Find the most recent exercise file in `exercises/` (or use a file specified by the user: $ARGUMENTS)
2. Read the exercise file — the user will have filled in answers on the `> ` lines
3. For each sentence, evaluate the translation and append a `## Review` section to the exercise file:

```
## Review

### Italian → German
1. ✓ Correct
2. ✗ "Ich gehe an die Schule" → "Ich gehe zur Schule" — wrong preposition
...

### Summary
X/20 correct. [Brief summary of patterns observed.]
```

4. After reviewing, update `issues/rating.md`:
   - List current weak areas with examples
   - List strengths
   - Provide study recommendations
   - Track progress over time (compare with previous ratings if they exist)

**Grading guidelines:**
- Accept minor typos if the meaning is clear, but note them
- Accept valid alternative translations
- Explain grammar mistakes clearly and concisely
- Be encouraging but honest

**Listen exercises (title starts with "# Listen"):**
- Extract correct answers from the `<!-- ANSWER KEY -->` HTML comment at the bottom of the file
- Compare the user's transcription against the answer key
- Extract replay counts from `<!-- REPLAY COUNTS: ... -->` if present. In the Summary, note which sentences needed the most replays — these indicate difficult-to-parse phrases worth revisiting
- **Lenient on:** missing/wrong accent marks (è vs e, à vs a — hard to distinguish by ear)
- **Strict on:** actual words, word forms, word order
- **Highlight:** homophones and near-homophones as learning opportunities (anno/hanno, uova/uva)
