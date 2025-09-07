# Playback (slow text playback)

## What it does
Slows down a sentence by inserting ellipses (or any other separator) between words to mimic slow, dramatic playback.

## What I struggled with 
- Maintaining punctuation while inserting separators.
- Not duplicating separators for multiple spaces.

 
## How I solved it
- Used .split() to remove multiple spaces and `separator.join(words)` to build output.

## Fun fact 
Perfect for dramatic presentations or passive-aggressive Slack messages. Use responsibly. ????

## How to run
```bash
python playback.py
```
