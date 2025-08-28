### PIZZA.PY

Overview This program prompts the user for a pizza size and the number of toppings then calculates the price. The implementation is intentionally simple and uses small functions so it is easy to read and test.
---

## Goal of the program

- Tabulate CSV files
--- 
## How to run Run the program in a terminal and follow the prompts

python pizza.py sicilian
--- 

## How it works
1. Reads in a CSV file (the pizza menu).

2. Displays the menu as a table in the terminal using the tabulate library.

3. Handles errors for command-line arguments and file types.

- Development log Prompts I used I asked for a minimal pizza program with functions get_size and calc_price and with input sanitisation.

## Struggles and fixes

At first, I didn’t know how to use tabulate and tried to format the table manually with loops and spacing. That got messy quickly.

I forgot that tabulate needs the header row separated from the data. Initially, my table just looked like a bunch of raw rows until I fixed how I passed headers="firstrow".

I had an issue where I opened the CSV without newline="", which caused blank lines to appear in the output on Windows-style CSVs. Solved by adjusting how I opened the file.

Error messages again tripped me up — I was printing my own custom text instead of the exact wording check50 expected.

## What worked
- Learned how to use the tabulate library to make clean tables without manually formatting them.

- Got more comfortable with reading CSV files using csv.reader.

- Structured the code with clear error checks before processing, which made debugging easier

## Resources that helped

- Python csv module documentation

- tabulate library documentation and examples

- CS50 Pizza Problem Spec

- StackOverflow discussions on tabulate with headers

Author Kimberley