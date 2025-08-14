# einstein.py

## Purpose
Calculates energy (E) from a given mass (m) using Einstein’s famous equation **E = m × c²**.

## How It Works
1. Prompt the user for a mass in kilograms.
2. Convert the input into an integer.
3. Use the constant `c = 300000000` (speed of light in m/s).
4. Apply the formula `E = m * c**2`.
5. Output the result as an integer (no decimals).

## Struggles
- Remembering to use `**` for exponentiation instead of `^`.
- Accidentally printing a huge floating-point number instead of an integer.
- Initially forgot to cast user input to an integer before math.

## Solutions
- Explicitly cast the input with `int()`.
- Stored `c` as a constant variable for clarity.
- Printed result as a plain integer for neatness.

##  Sources
- CS50P Problem Set — Einstein
- [Python Operators Reference](https://docs.python.org/3/reference/expressions.html#binary-arithmetic-operations)
- High school physics class flashbacks.
