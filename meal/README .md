# meal.py

## Purpose
Determines whether it’s breakfast, lunch, or dinner time — based on the time you input.

## How It Works
1. Prompt the user for a time in `HH:MM` format (24-hour clock).
2. Convert hours and minutes into a single floating-point number for easy comparisons (e.g., `7:30` → `7.5`).
3. Check against time ranges:
   - *07:00–08:00* → Breakfast Time
   - *12:00–13:00* → Lunch Time
   - *18:00–19:00* → Dinner Time
4. Output the correct message, or nothing if it’s snack time.

## Struggles
- Initially compared strings directly instead of converting to numbers — which is a bad idea (`"10:00"` < `"2:00"` evaluates incorrectly).
- Needed to decide whether to use `>=` and `<` boundaries so times like exactly `08:00` would still register as breakfast.
- Debugging edge cases lik

## Solutions
- Created a helper function to convert `HH:MM` to a float.
- Used consistent decimal comparisons across all ranges.
- Tested times across day to confirm boundaries worked.

## Sources
- CS50P Lecture on Conditionals & Comparisons
- [Python Official Docs — String `split()` Method](https://docs.python.org/3/library/stdtypes.html#str.split)
- My own stubbornness and coffee.