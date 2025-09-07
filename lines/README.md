## lines.py — README

Counts how many actual lines of Python code are in a file. No cheats: blank lines and comments don’t count.

## How it works
- Takes one argument: the filename of a .py file.
 Checks: exactly one argument, file ends with “.py”, file exists. If not, it dies dramatically with an  error message.
- Opens the file and walks line by line.
- If the line is blank or just a comment, ignore it.
- Otherwise, count it.
- Prints the final number.

## How I solved it
Set up guardrails first (arguments and file check). Then a simple open/read loop with .lstrip() so leading spaces don’t confuse me. Count only when the line isn’t empty and doesn’t start with #. Done.

## Questions I asked myself
– Do docstrings count as comments? I let them count as code, because technically they’re strings.
– What about lines with code after a comment? They count, because something executes.
– Should I be clever and regex this? No, simple loop works fine.

## Examples
$ python3 lines.py hello.py
4


### Signature
// Kimberley B.0