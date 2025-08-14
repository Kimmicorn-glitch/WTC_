# adieu.py

## Purpose
Collects names until EOF, then says goodbye to everyone in one grammatically correct sentence. Think "Goodbye, Alice, Bob, and Charlie" — the polite way to end a party.

## How It Works
1. Keep prompting the user for names until they press `Ctrl+D` (EOF).
2. Store names in a list.
3. Join names into a sentence:
   - One name → "Adieu, adieu, to X"
   - Two names → "Adieu, adieu, to X and Y"
   - Three or more → "Adieu, adieu, to X, Y, and Z"
4. Print the result with correct commas and "and" placement.

## Struggles
- Grammar rules for commas in a list (the Oxford comma is a hill I’ll die on.)
- EOF handling (program kept throwing errors when input stopped abruptly.)
- Joining lists into a string without an extra comma before "and."

## Solutions
- Used `try/except EOFError` to break cleanly when the user stops entering names.
- Leveraged Python’s `join()` for comma separation, then manually handled the last "and" case.
- Tested with different numbers of names to catch edge cases.

##  Sources
- CS50P Problem Set specification for Adi
