# taqueria.py

##  Purpose
Takes taco orders from a fixed menu, adds up the total, and shows the running cost until the user is done.

## How It Works
1. Display a pre-defined menu with prices (dictionary).
2. Continuously prompt for an item until EOF.
3. If the item exists on the menu, add its price to a running total.
4. Print the updated total in '$x.xx' format each time.
5. Ignore items not on the menu.

## Struggles
- Handling case insensitivity,"Burrito" and "burrito" should be the same.
- Program kept breaking when I typed an invalid item and with valid items.
- Forgetting to format prices with two decimal places.

## Solutions
- Used .strip().title() or .lower() to normalize input.
- Added a check to skip invalid menu items instead of erroring out.
- Used f"{total:$ .2f}" for perfect money formatting.

## Sources
- CS50P Problem Set — Taqueria
- [Python f-string formatting](https://realpython.com/python-f-strings/)
- My eternal craving for tacos while coding this.
