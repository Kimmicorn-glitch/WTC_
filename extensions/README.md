## extensions.py
## Overview
This program detects a file’s extension and outputs the correct MIME type. It’s the detective of the programming world — quietly judging files based on their endings.

# How It Works
1. Prompts user for a filename.

2. Strips whitespace and lowers the case to avoid case-sensitive drama.

3. Checks the extension against a dictionary of MIME types.

4. Outputs the correct MIME type, or application/octet-stream if it doesn’t know what it is.

## My Struggles & Solutions
- Struggle: File extensions with uppercase letters threw off my matches.
  Solution: .lower() — turning uppercase arrogance into lowercase compliance.

- Struggle: Some files had hidden spaces.
  Solution: .strip() to politely remove the unwanted hangers-on.

## Example Run

Input: cat.JPG
Output: image/jpeg


## Lessons Learned
Computers are extremely literal — .JPG and .jpg are worlds apart unless you teach them otherwise.

MIME types sound fancy but are really just polite file descriptions.

## Sources & Inspiration
- CS50P “Extensions” problem
  Python string methods documentation

