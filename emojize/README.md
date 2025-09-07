## emojize.py
## Overview
This program takes user input with emoji aliases (like :smile:) and converts them into actual Unicode emojis 😄. Because sometimes plain text just can’t express the depth of human (or programmer) emotion.

## How It Works
Prompts the user to type something with emoji shortcodes.

Uses the emoji module to translate the codes into real emojis.

Outputs the result with the extra joy factor.

## My Struggles & Solutions
- Struggle: I kept forgetting to actually install the emoji module.
  Solution: pip install emoji — turns out Python can’t just “feel” emojis without a library.

- Struggle: Not all aliases worked.
  Solution: Checked the official emoji alias list instead of guessing like a psychic on bad coffee.

## Example Run
mathematica
Copy code
Input: I am happy :smile:
Output: I am happy 😄

## Lessons Learned
- Unicode is magical.
- Humans respond better to emojis than error messages.
- There is no such thing as “too many” emojis in a CS50 problem set.

## Sources & Inspiration
- CS50P “Emojize” problem

- Emoji Python Library

- Me, trying to make my code as expressive as my face when debugging

