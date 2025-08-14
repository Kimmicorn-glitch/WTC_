# bank.py

## Purpose
Greets the user, then rewards or ignores them based on how politely they greet, because manners matter, even to computers.

## How It Works
1. Prompt the user for a greeting.
2. Remove any extra spaces and lowercase it for consistent checking.
3. Apply the rules:
   - Starts with "hello" ->  $0
   - Starts with "h" but not "hello" → $20
   - Anything else → $100
4. Output the amount owed.

## Struggles
- Case sensitivity — "Hello", "HELLO", and "hello" all needed to be treated the same.
- Accidentally matching "hello" in the middle of a sentence instead of just at the start.
- Forgetting that .startswith() is case-sensitive without preprocessing.

## Solutions
- Used .strip().lower() to normalize input before checks.
- Applied .startswith("hello") for the most polite scenario.
- Made the logic check "h" as the fallback polite-but-not-perfect case.

## Sources
- CS50P Problem Set — Bank
- Python Official Docs — str.startswith()(https://docs.python.org/3/library/stdtypes.html#str.startswith)
- My own belief that a "hi" deserves less free stuff than a "hello."
