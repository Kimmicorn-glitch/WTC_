# Coke Machine Simulation

## What it does
Simulates a vending machine that takes coins until soda is bought, gives change, and keeps going until the user has their drink.

## What I struggled with 
- Dealing with invalid coin input and getting loops right.
- Maintaining precision when doing money calculations (floats vs. integer cents).

## How I solved it
- Used integer cents to store amounts to prevent floating point roundoff errors.
- Employed a simple while loop and conditions to prevent confusing nested loops.


## How to run
```bash
python coke.py
```