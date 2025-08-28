### **test_bank/README.md**
markdown
# test_bank.py

## Overview
Tests bank.py, which determines a bank greeting’s value:
- Greeting starts with “hello” -> $0
- Greeting starts with “h” -> $20
- Everything else -> $100

## What I Learned
- Input normalization (.strip() + .lower()) is everything.
- Edge cases like “ Hello” or “HELLO” matter more than you think.
- Tests force me to consider *all* weird human inputs.

## Common Errors I Faced
- **Didn’t ignore case at first:** Fixed by .lower().
- **Missed leading/trailing spaces:** .strip() to the rescue.
- **Misread “starts with h” as “contains h”:** Thank you, failing test.

## How to Run
bash
pytest test_bank.py
