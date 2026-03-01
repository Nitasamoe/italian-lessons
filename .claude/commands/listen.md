Generate a new Italian listening exercise.

1. Read `grammar.md`, `vocabulary.md`, and `issues/rating.md`
2. Create a new exercise file in `exercises/` named `listen-YYYY-MM-DD.md` (using today's date). If one already exists for today, append a letter suffix (e.g. `listen-2026-03-01b.md`).
3. Generate **10 short Italian sentences** (5–10 words each):
   - Use only vocabulary from `vocabulary.md`
   - Target weak areas from `issues/rating.md`
   - A1 level, natural-sounding sentences
   - Mix grammar points — articles, verb conjugation, prepositions, etc.
4. Create the exercise file with this exact format:

```
# Listen — YYYY-MM-DD

## Italian Listening
Listen to each sentence and write what you hear.

1. _(audio)_
   >

2. _(audio)_
   >

(... 10 sentences total)











<!-- ANSWER KEY (do not read before completing the exercise)
1. [Italian sentence]
2. [Italian sentence]
...
-->
```

5. After creating the file, **set up playback** so the text stays hidden from the CLI:
   a. Extract sentences to a temp file:
      ```
      sed -n '/<!-- ANSWER KEY/,/-->/p' exercises/listen-YYYY-MM-DD.md | grep '^[0-9]' | sed 's/^[0-9]*\. //' > /tmp/listen_keys.txt
      ```
   b. Create a playback helper script:
      ```bash
      cat > /tmp/listen_play.sh << 'SCRIPT'
      #!/bin/bash
      line=$1
      speed=${2:-normal}
      sentence=$(sed -n "${line}p" /tmp/listen_keys.txt)
      if [ "$speed" = "slow" ]; then slow_flag="True"; else slow_flag="False"; fi
      python3 << PYEOF
      from gtts import gTTS
      import tempfile, os, warnings
      warnings.filterwarnings("ignore")
      tts = gTTS("""$sentence""", lang='it', slow=$slow_flag)
      f = tempfile.NamedTemporaryFile(suffix='.mp3', delete=False)
      tts.save(f.name)
      os.system('afplay ' + f.name)
      os.unlink(f.name)
      PYEOF
      SCRIPT
      chmod +x /tmp/listen_play.sh
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
     a. Append a `<!-- REPLAY COUNTS: 1:0, 2:3, 3:1, ... -->` comment to the exercise file (one entry per sentence showing how many replays were needed)
     b. Tell the user: "All done! Run `/review` to check your answers."
7. Clean up: `rm /tmp/listen_keys.txt /tmp/listen_play.sh`

**IMPORTANT:** Never pass sentence text directly as a CLI argument — it's visible to the user. Always use the `/tmp/listen_play.sh` helper script which reads from the temp file.
