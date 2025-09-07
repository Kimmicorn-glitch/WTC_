# fuel.py

## Purpose
Takes a fraction like `3/4` and converts it into a percentage or a special message.

## How It Works
1. Prompt for fraction input (`x/y` format).
2. Validate that:
   - `y` > 0  
   - `x` ≥ 0  
   - `x` ≤ `y`
3. Convert to a percentage:
   - If ≤ 1%, print `E`
   - If ≥ 99%, print `F`
   - Else, print as a percentage.

## Struggles
- Division by zero errors popped up like uninvited guests.
- Invalid formats required constant re-prompts.
- The “E” and “F” conditions were initially reversed in my head.

## Lesson Learned
- Always validate inputs before doing maths.
- Edge cases make the difference between a crash and a pass.

## Example
3/4 → 75%
1/100 → E
99/100 → F