## README for working.py

Converts a 12-hour time range into 24-hour format. Input like "9AM to 5PM" becomes "09:00 to 17:00". Handles optional minutes and strict AM/PM formatting.

## How it works
1. Prompts for a single string in the format h[:mm] AM/PM to h[:mm] AM/PM.
2. Uses a regex to validate the format and extract hours, optional minutes, and AM/PM for both start and end times.
3. Converts times to 24-hour format:
 12 AM → 00:00
 12 PM → 12:00
4. other hours adjusted by adding 12 for PM if needed
5. Returns a string like "09:30 to 17:45".
6. Raises ValueError for malformed input: wrong hours, minutes out of range, missing AM/PM, or missing to.

## How I solved it
Used regex with optional minutes for flexible parsing. Extracted groups, converted them to integers, and applied simple rules to convert to 24-hour time. Used helper function to_24() to keep code clean. Added input validation everywhere.

## Questions I asked myself
– What if minutes are missing? Default to :00.
– How to handle midnight and noon? Special-case 12 AM → 0 and 12 PM → 12.
– Invalid inputs like "13 AM to 5 PM"? Raise ValueError, don’t guess.

## Examples
Input: "9 AM to 5 PM" → Output: "09:00 to 17:00"
Input: "12 AM to 12 PM" → Output: "00:00 to 12:00"
Input: "9:30 AM to 5:45 PM" → Output: "09:30 to 17:45"

--- 

## README for test_working.py

Pytest suite for working.py. Checks that convert() handles 12-hour to 24-hour ranges correctly, including minutes, noon/midnight, and edge cases.

## How it works
- Imports convert() from working.py.
- test_negative: basic range "9 AM to 5 PM".
- test_with_minutes: ranges with minutes like "9:30 AM to 5:45 PM".
- test_midnight_and_noon: "12 AM to 12 PM" and "12 PM to 12 AM".
- test_edge_cases: single-hour ranges and overnight ranges.
- test_invalid_format: hours outside 1–12.
- test_bad_minutes: minutes outside 0–59.
- test_missing_meridiem or missing to: ensures ValueError is raised.

## How I solved it
Covered normal, boundary, and error conditions. Used pytest.raises to confirm errors for invalid input. Made sure 12 AM/PM and edge times were tested so no surprises.

## Examples
$ pytest test_working.py
All tests pass, times are converted correctly, errors caught.


Signature
