### README for test_plates.py

Pytest suite for plates.py. Checks if license plates follow the rules instead of letting any random string sneak past.

## How it works
- Imports is_valid() from plates.py.
- test_length: ensures plates are the right length (not too short or too long).
- test_starts_with_letter: confirms that plates start with letters, not numbers.
- test_numbers_rules: validates number placement rules—no leading zeros, no extra letters at the end.
- test_alphanumeric_only: rejects symbols, spaces, and keeps only letters and numbers.
- test_must_start_with_two_letters: double-checks the first two characters are letters.

## How I solved it
Covered every edge case I could think of: lengths, starting characters, digits, symbols, and tricky combinations. Used assert statements for each rule so tests fail loudly if something breaks.

## Questions I asked myself
- Should “CS50” pass? Yes, perfect plate.
- What about “CS05”? No, leading zero kills it.
- Can special characters sneak through? Not on my watch.

## Examples
$ pytest test_plates.py
All tests pass, plates behave, no funny business.

Signature
// Kimberley B.