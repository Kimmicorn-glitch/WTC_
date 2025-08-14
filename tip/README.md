# Tip Calculator 

## What it does
Calculates a tip amount from a bill and desired tip percentage and prints a cheeky message for very small tips.

## What I struggled with
- Parsing currency inputs with optional `$` signs and whitespace.
- Ensuring consistent rounding/formatting for automated checks.

## How I solved it
- Figured out input with `.replace()` and `.strip()` then converted to `float` within `try/except`.



## How to run
```bash
python tip.py
```
