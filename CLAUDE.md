# Italian Learning Project

This project is a structured Italian learning system. Claude Code acts as a tutor, generating exercises and reviewing answers.

## Project Structure

- `grammar.md` — Grammar rules to teach and test (A1 level, expandable)
- `vocabulary.md` — Vocabulary organized by category (expandable)
- `exercises/` — Exercise files, one per session, named `YYYY-MM-DD.md`
- `issues/rating.md` — Tracked weak areas, strengths, and study recommendations
- `issues/level.md` — CEFR level assessment, untested areas, and next-level requirements

## Custom Commands

### /exercise

Generate a new exercise file in `exercises/YYYY-MM-DD.md` (using today's date).

**Process:**
1. Read `grammar.md`, `vocabulary.md`, and `issues/rating.md`
2. Generate an exercise file containing:
   - **20 sentences in German to translate into Italian**
3. Sentences must:
   - Be at A1 beginner level
   - Be based on the grammar rules and vocabulary in the project files
   - Target weak areas identified in `issues/rating.md`
   - Mix new material with reinforcement of previous weak spots
   - Adapt difficulty and topics based on the current rating
   - Include 3–5 multi-clause sentences using subordinating conjunctions (quando, se, mentre, perché, etc.), relative pronouns (che, cui), or infinitive constructions (prima di, senza, per + infinitive) — gradually increase complexity based on what's been demonstrated in `issues/level.md`
4. Use this format:

```markdown
# Exercise — YYYY-MM-DD

## German → Italian
Translate the following sentences into Italian.

1. [German sentence]
   >

2. [German sentence]
   >

(... 20 sentences total)
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

4c. After reviewing, update `issues/level.md`:
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

### /drill

Generate a focused drill exercise targeting the #1 weak area from `issues/rating.md`.

**Process:**
1. Read `issues/rating.md` and identify the top weak area (highest error count or marked CRITICAL)
2. Generate 10 short, focused exercises in `exercises/drill-YYYY-MM-DD.md` (using today's date)
3. **Always use German→Italian translation format** — give each sentence in German and the user translates to Italian. Each sentence should isolate the target weak area.
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
3. For each wrong answer, create a **new sentence in German** that tests the **same grammar point** — do not repeat the original sentence verbatim. The user translates to Italian.
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

### /listen

Generate an Italian listening exercise using Google TTS (`gtts`).

**Process:**
1. Read `grammar.md`, `vocabulary.md`, and `issues/rating.md`
2. Generate 10 short Italian sentences (5–10 words each) using only known vocabulary, targeting weak areas
3. Create the exercise file in `exercises/listen-YYYY-MM-DD.md` (using today's date) **without the answer key** — the answer key must NOT be written to the file until the exercise is complete
4. Write the generated sentences to `/tmp/listen_keys.txt` (one per line, numbered) and create the helper script `/tmp/listen_play.sh`
5. Play each sentence one at a time via `bash /tmp/listen_play.sh N`
6. The user types what they heard — write each answer to the `> ` line in the file
7. Track replay counts per sentence. After all 10, append a `<!-- REPLAY COUNTS: 1:0, 2:3, ... -->` comment to the exercise file
8. **After all sentences are done**, append the `<!-- ANSWER KEY -->` block to the exercise file
9. Suggest `/review` and clean up temp files

**IMPORTANT:** Never pass sentence text directly as a CLI argument — it's visible to the user. Always use the helper script which reads from the temp file indirectly.

**IMPORTANT:** The answer key must ONLY be appended to the exercise file after all 10 sentences have been played and answered. During the exercise, answers exist only in `/tmp/listen_keys.txt`. This prevents answer spoiling through edit previews or tool output.

**Replay commands during playback:**
- `replay` — hear the sentence again at normal speed
- `slow` — hear the sentence at slow speed (gTTS slow mode)
- `next` — skip to the next sentence

**Helper script (`/tmp/listen_play.sh`):**
Use a Python-only implementation so sentence text never appears in shell variable expansion:

```bash
#!/bin/bash
python3 - "$1" "$2" <<'PYEOF'
import sys, subprocess, tempfile, os
n = int(sys.argv[1])
slow = len(sys.argv) > 2 and sys.argv[2] == "slow"
keys = open("/tmp/listen_keys.txt").readlines()
# Strip number prefix (e.g. "1. ") to get raw sentence
line = keys[n - 1].strip()
if line and line[0].isdigit():
    line = line.split(". ", 1)[-1]
with tempfile.NamedTemporaryFile(suffix=".mp3", delete=False) as f:
    tmp = f.name
try:
    from gtts import gTTS
    tts = gTTS(line, lang="it", slow=slow)
    tts.save(tmp)
    subprocess.run(["afplay", tmp])
finally:
    os.unlink(tmp)
PYEOF
```

**File format (during exercise — no answer key):**

```markdown
# Listen — YYYY-MM-DD

## Italian Listening
Listen to each sentence and write what you hear.

1. _(audio)_
   >

2. _(audio)_
   >

(... 10 sentences total)
```

**File format (after exercise — answer key appended):**

```markdown
# Listen — YYYY-MM-DD

## Italian Listening
Listen to each sentence and write what you hear.

1. _(audio)_
   > [user's answer]

(... 10 sentences total)

<!-- REPLAY COUNTS: 1:0, 2:3, ... -->

<!-- ANSWER KEY (do not read before completing the exercise)
1. [Italian sentence]
2. [Italian sentence]
...
-->
```

If a listen exercise for today already exists, append a letter suffix (e.g. `listen-2026-03-01b.md`).

**Reviewing listen exercises:** Use `/review` — it works the same way, with these adjustments:
- Extract correct answers from the `<!-- ANSWER KEY -->` HTML comment block at the bottom of the file
- Extract replay counts from the `<!-- REPLAY COUNTS: ... -->` comment. In the Summary, note which sentences needed the most replays — these indicate difficult-to-parse phrases worth revisiting
- **Lenient on:** missing/wrong accent marks (è vs e, à vs a — hard to distinguish by ear)
- **Strict on:** actual words, word forms, word order
- **Highlight:** homophones and near-homophones as learning opportunities (anno/hanno, uova/uva)
