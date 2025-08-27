# interpreter.py

## Purpose
A tiny calculator that can add, subtract, or multiply two numbers no frills, no divisions, just quick maths.

## How It Works
1. Prompt the user for an expression like 5 + 3 or 10 * 4.
2. Split the input into three parts: first number, operator, second number.
3. Convert numbers to `float` to allow decimals.
4. Match the operator:
   - "+" -> addition
   - "-" -> subtraction
   - "*" -> multiplication
5. Print the result to one decimal place.

## Struggles
- Accidentally forgot to strip spaces, so "5  +   3" broke at first.
- Then broke a second time when I did not add spaces when to the prompt.
- Accidentally allowed division in early versions, but removed because CS50 spec didn’t ask for it.
- Keeping output formatting to exactly one decimal place took a minute to get right.

## Solutions
- Used input().strip() and split() to reliably get clean parts.
- Added explicit condition checks for each operator.
- Used Python f-strings to control decimal formatting.

## Sources
- CS50P Problem Set — Interpreter Specification
- [Python f-strings Guide](https://realpython.com/python-f-strings/)
- A brief argument with my REPL that I eventually won.
- An honourable mention for Geeksforgeeks.
