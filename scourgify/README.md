# Scourgify – scourgify.py

This program cleans a CSV file of student data, splitting full names into first and last names, and outputs a new CSV with a standardized format.

## Features
- Reads a CSV file where each row contains a student’s full name and house
- Splits the full name into first and last fields
- Preserves the house field
- Writes the cleaned data into a new CSV file with headers: first, last, house
- Validates command-line arguments and input file type

## What I learned
- How to handle command-line arguments with sys.argv
- How to read CSV files using csv.DictReader
- How to write CSV files using csv.DictWriter
- How to manipulate strings in Python (splitting names)
- Error handling with try/except and sys.exit
- Structuring a Python program with small, clear functions

## Challenges
- Ensuring correct number of command-line arguments
- Handling invalid file names and file types
- Correctly splitting names with a comma and space
- Keeping the output CSV in the correct order of fields

## Files
- scourgify.py – main program
- Example CSV input: students.csv
- Example CSV output: cleaned_students.csv

## How to run
Run the program from the command line with two arguments: input CSV file and output CSV file.

Example:

bash
python scourgify.py students.csv cleaned_students.csv