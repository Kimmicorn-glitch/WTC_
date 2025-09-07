# plates.py

## Purpose
Validates vanity license plates according to specific rules, because random "X7R3" nonsense just isn’t allowed.

## How It Works
1. Ask the user for a plate string.
2. Validate with these rules:
   - Starts with at least two letters.
   - Length between 2 and 6 characters.
   - Numbers, if present, must be at the end.
   - No leading zero in the number section.
   - Only alphanumeric characters allowed.
3. Print "Valid" or "Invalid" accordingly.

## Struggles
- Checking that once a number starts, it stays to the end — my first attempt let sneaky letters slip in.
- Accidentally allowing a number to start with zero.
- Forgetting that Python’s isalpha() and isalnum() behave differently.

## Solutions
- Broke validation into separate helper checks for clarity.
- Used string slicing to check starting letters and trailing numbers.
- Added explicit check for leading zero in the numeric portion.

## Sources
- CS50P Problem Set specification for Vanity Plates
- [Python Official Docs — String Methods](https://docs.python.org/3/library/stdtypes.html#string-methods)
- Multiple failed validation tests that made me suspicious of my own logic.
- Shout out to [GeeksforGeeks](http://www.GeeksforGeeks.com)
