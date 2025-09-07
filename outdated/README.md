# outdated.py

## Purpose
Converts dates from either:
- MM/DD/YYYY
- Month Day, Year
into the universal ISO format YYYY-MM-DD.

##  How It Works
1. Prompt for a date in either format.
2. If it contains /:
   - Split into month, day, year.
   - Ensure month < 12 and day < 31.
3. If it contains month name:
   - Convert month name to number.
   - Extract day and year.
4. Print in YYYY-MM-DD format with zero-padding.

## Struggles
- Parsing text months took longer than I’d like to admit.
- Had to keep re-running tests because “October 9, 170” wasn’t padded correctly.
- Accidentally accepted invalid dates at first (hello, 32nd of July).

## Lesson Learned
- Data sanitisation is everything.
- Month name lookups are easier when stored in a list.

## Example
10/9/1701 -> 1701-10-09
October 9, 1701 -> 1701-10-09