Review a completed Italian exercise.

**Files to read:** `issues/tracking.md`
**Do NOT read:** `grammar.md`, `vocabulary.md` (not needed for grading)

**Grading Protocol (MANDATORY):**
Before writing ANY grade line:
1. Parse the German source → what is being asked
2. Parse the Italian answer → what the student wrote
3. Check grammar, meaning, spelling
4. DECIDE ✓ or ✗ (before writing anything)
5. Write ONE clean grade line — no deliberation, no "actually", no mid-sentence reversals

---

1. Find the most recent exercise file in `exercises/` (not `exercises/archive/`) (or use a file specified by the user: $ARGUMENTS)
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

4. After reviewing, update `issues/tracking.md`:
   - Update the **Active Errors** table:
     - For each error, find or create a row
     - Increment the error count
     - Update "Last Seen" to the exercise date
     - Update "Status" (ACTIVE, IMPROVING, PERSISTENT, etc.)
     - Update "Key Rule" with the most recent example
   - Move items to IMPROVING/RESOLVED status when demonstrated correct 2+ exercises in a row
   - Move RESOLVED items to `issues/archive.md` (append to the table)
   - Update the **Current Assessment** paragraph and A2 progress percentage
   - Add a new row to the **Progress** table
   - Update **Study Recommendations** (3–5 bullet points for next exercise)

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
