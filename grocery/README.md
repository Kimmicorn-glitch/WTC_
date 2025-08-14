# Grocery (Counter) 

## What it does
Counts orders from input (one per line) until EOFError and prints tallies in alphabetical order.

## What I struggled with
- Handling EOFError in interactive tests and ensuring consistent casing.
- Sorting output as specified and uppercasing item names for output.

## How I solved it
- Used `try/except` catching `EOFError` and `dict.get()` for counting.


## How to run
```bash
python grocery.py
```
