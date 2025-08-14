## deep.py
## Overview
A philosophical program that asks: “What is the answer to the Great Question of Life, the Universe, and Everything?” and only accepts the answer 42 (or its textual equivalents) without argument. Inspired by The Hitchhiker’s Guide to the Galaxy.

## How It Works
1. Asks the user the question.

2. Accepts answers like 42, forty-two, or forty two (case-insensitive).

3. Outputs “Yes” if correct, “No” otherwise.

## My Struggles & Solutions
- Struggle: Handling all the textual variations of “42”.
  Solution: Normalized the input with .lower() and .strip() before comparing.

- Struggle: I kept typing “forty two” with a hyphen in the wrong place.
  Solution: Added both hyphenated and non-hyphenated options — problem solved.

## Example Run

Input: 42
Output: Yes

Input: Forty-two
Output: Yes

Input: 41
Output: No


## Lessons Learned
- Sometimes the correct answer really is just 42.

- Douglas Adams jokes are timeless in programming.

- Input validation makes even silly programs feel professional.

## Sources 
- CS50P “Deep Thought” problem
- The Hitchhiker’s Guide to the Galaxy by Douglas Adams

