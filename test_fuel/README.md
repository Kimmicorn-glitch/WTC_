### README for test_fuel.py

Pytest suite for fuel.py. Makes sure the program’s fraction-to-percentage converter and fuel gauge behave instead of lying to me.( that the fuel.py program works)

## How it works
- Imports pytest, the convert() and gauge() functions from fuel.py.
- test_convert_valid: checks proper fractions like 1/2 → 50, 3/4 → 75, etc.
- test_convert_invalid: pushes garbage (“cat/dog”), improper fractions (3/2), and division by zero to confirm the right errors get thrown.
- test_gauge: checks that tiny values (0,1) show “E”, big ones (99,100) show “F”, and normal ones give percentages.
- test_convert_negative: tries sneaky negatives like -1/2, 1/-2, and expects ValueError.

## How I solved it
Kept tests short and blunt. Covered happy paths, bad input, edge cases, and negative numbers. Used pytest.raises to confirm errors instead of letting them crash.

## Questions I asked myself
– Do I really need to test “cat/dog”? Yes, because someone will type it.
– Should 99% be “F”? Decided yes, close enough to full.
– What about weird negatives? Code should shut those down too.

## Examples
$ pytest test_fuel.py
All tests pass, no explosions.

Signature
// Kimberley B.