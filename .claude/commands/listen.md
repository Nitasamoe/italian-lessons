Generate a new Italian listening exercise.

**Files to read:**
- `issues/tracking.md` — for weak areas and study recommendations
- `grammar.md` — read only the index (lines 1–20). Read specific sections only if needed.
- `vocabulary.md` — read only the index (lines 1–18). Read specific sections only if needed.

1. Read the files listed above
2. Generate **10 short Italian sentences** (5–10 words each):
   - Use only vocabulary from `vocabulary.md`
   - Target weak areas from `issues/tracking.md`
   - A1 level, natural-sounding sentences
   - Mix grammar points — articles, verb conjugation, prepositions, etc.
3. Create the exercise file in `exercises/listen-YYYY-MM-DD.md` (using today's date) **without the answer key** — the answer key must NOT be written to the file until the exercise is complete. If one already exists for today, append a letter suffix (e.g. `listen-2026-03-01b.md`).
4. Use this format for the initial file:

```
# Listen — YYYY-MM-DD

## Italian Listening
Listen to each sentence and write what you hear.

1. _(audio)_
   >

2. _(audio)_
   >

(... 10 sentences total)
```

5. Write the generated sentences to `/tmp/listen_keys.txt` (one per line, numbered) and create the helper script `/tmp/listen_play.sh`

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

6. Run the interactive playback loop, **tracking replay counts**:
   - Initialize a replay counter for each sentence (all start at 0)
   - For each sentence (1 through 10):
     a. Announce "Sentence N" to the user
     b. Play the sentence: `bash /tmp/listen_play.sh N`
     c. Ask the user to type what they heard
     d. If the user types `replay`, play again: `bash /tmp/listen_play.sh N` — increment replay count
     e. If the user types `slow`, play at slow speed: `bash /tmp/listen_play.sh N slow` — increment replay count
     f. If the user types `next`, skip to the next sentence (leave `> ` line blank)
     g. Once the user provides an answer (anything other than `replay`/`slow`/`next`), write it to the corresponding `> ` line in the exercise file
     h. Move to the next sentence
   - After all 10 sentences:
     a. Append a `<!-- REPLAY COUNTS: 1:0, 2:3, 3:1, ... -->` comment to the exercise file
     b. **Append the `<!-- ANSWER KEY -->` block** to the exercise file (only now, not before)
     c. Tell the user: "All done! Run `/review` to check your answers."
7. Clean up: `rm /tmp/listen_keys.txt /tmp/listen_play.sh`

**IMPORTANT:** Never pass sentence text directly as a CLI argument — it's visible to the user. Always use the helper script which reads from the temp file indirectly.

**IMPORTANT:** The answer key must ONLY be appended to the exercise file after all 10 sentences have been played and answered. During the exercise, answers exist only in `/tmp/listen_keys.txt`. This prevents answer spoiling through edit previews or tool output.

**IMPORTANT:** Never display or output the contents of `/tmp/listen_keys.txt` or any sentence text during the exercise. Specifically:
- To check if temp files exist, use `test -f /tmp/listen_keys.txt` or `ls /tmp/listen_keys.txt` — NEVER use `cat`, `Read`, or any command that outputs file contents
- To count sentences, use `wc -l < /tmp/listen_keys.txt`
- When resuming across sessions, determine progress by counting filled `> ` lines in the exercise file — do not inspect the keys file

**Answer key format (appended after exercise):**

```
<!-- ANSWER KEY (do not read before completing the exercise)
1. [Italian sentence]
2. [Italian sentence]
...
-->
```
