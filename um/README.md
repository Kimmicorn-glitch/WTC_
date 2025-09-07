### README for um.py

Counts how many times the word “um” appears in a string. Ignores case and makes sure it’s a standalone word,so “dummy” or “yummy” don’t get flagged.

## How it works
- Prompts for text input.
- Uses a regular expression to search for \bum\b with re.IGNORECASE.
- Counts matches and prints the total.

## How I solved it
Used Python’s re.findall() because it handles word boundaries neatly. Keeping it case-insensitive avoids extra logic. One line, elegant, and it actually works.

## Questions I asked myself
- Should “UM”, “Um”, “uM” count? Yes, ignore case.
- What about “dummy” or “alumni”? Nope, word boundaries protect us.
- Does punctuation break it? Nope, regex handles trailing punctuation.

## Examples
Input: “Hello, um, world” -> Output: 1
Input: “UM, um, Um” -> Output: 3
Input: “Yummy” -> Output: 0

---

## for test_um.py

Pytest suite for um.py. Makes sure the count() function correctly counts standalone “um”s.

## How it works
- Imports count() from um.py.
- test_um: simple cases like “Hello, um, world” and single “um”.
- test_case: ensures case-insensitivity works for “UM, um, Um”.
- test_not_in_word: words like “Yummy”, “dummy”, “alumni” don’t trigger false positives.
- test_punctuation: handles “um!”, “um?”, or “..um?” correctly.

## How I solved it
Covered all the obvious edge cases: casing, punctuation, false positives inside other words. Used assert statements so tests fail visibly if something goes wrong.

## Questions I asked myself
– Does punctuation affect the count? No, regex handles it.
– Should embedded “um” in other words count? No, word boundaries save the day.
– Does uppercase count? Yes, re.IGNORECASE makes it easy.

## Examples
$ pytest test_um.py
All tests pass, counts are accurate, no surprises.

Signiture
// Kimberley B.