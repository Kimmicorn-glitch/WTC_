# Nutrition Module

## What it does
Asks the user for the name of a fruit (case-insensitive) and prints out the calories for that fruit. Returns an error/exit code if the fruit is unknown.

## How it works (brief)
- Normalises input with `.strip()` and `.lower()`.
- References a dictionary of fruit names to calorie values.
- Searches for the normalised key and prints out the value or raises an error.

## What I struggled with (detailed)
- Not ignoring to sanitize input — users entered `Apple`, ` apple `, or `APPLE` and I was seeing mismatches to begin with.
- Choosing a behaviour for unknown fruits (print 0 or error). I chose to adhere to the spec and reject unknown fruits.
- Tests and formatting: I required deterministic output for check50.

## How I did it (step-by-step)
- Used `.strip()` and `.lower()` directly following reading in input.
- Fruit calorie table kept in a dictionary for O(1) lookups.
- Developed small tests and example cases to ensure consistent formatting of the output.

## Example usage
```
$ python nutrition.py
Fruit: Apple
52
```
