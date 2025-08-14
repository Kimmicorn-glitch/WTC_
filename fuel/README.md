## fuel/README.md


# Fuel Gauge Module

## What it does
Reads a fraction like `1/4` or `3/4` and outputs a fuel gauge percentage (e.g., `25%`, `75%`), or `F`/`E` if near full/empty per spec.

## How it works (brief)
- Splits `x/y` and calculates percentage.
- Checks input (no zero division, numerator 0 <= numerator <= denominator).
- Rounds to nearest and outputs `F` or `E` for outlier values.


## However, I struggled with the following:
- Prevention of invalid input and `ZeroDivisionError`.
- How often to display `F` vs `100%` and `E` vs `0%` in order to meet automated testing.
- Edge cases for rounding surprised us (e.g., `2/3` -> 67%).

## How I solved it (detail)
- Put parsing in `try/except` to catch `ValueError` and `ZeroDivisionError`.
- Verified numeric ranges prior to division.
- Employed `round()` for percentages and used hardcoded thresholds for `E` and `F`.

## Example usage
```
$ python fuel.py
Fraction: 1/4
25%
```
