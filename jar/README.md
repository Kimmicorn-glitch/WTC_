# Cookie Jar – jar.py

This project implements a Cookie Jar class in Python, allowing deposits and withdrawals of cookies with a maximum capacity.

## Features
- Initialize a jar with a given capacity (default 12)
- Deposit cookies, checking for overflow
- Withdraw cookies, checking for underflow
- Display cookies as 🍪 emojis with __str__
- Properties to access capacity and current size

## What I learned
- How to define a class with __init__, __str__, and @property decorators
- Using ValueError to handle invalid input
- How instance variables like _size and _capacity work
- How to write pytest unit tests for class methods

## Challenges
- Remembering to update _size in both deposit and withdraw
- Handling edge cases like negative capacity or attempting to withdraw too many cookies
- Naming test functions correctly for pytest collection

## Files
- jar.py – defines the Jar class
- test_jar.py – tests the constructor, deposit, withdraw, and string output

## How to test

Run tests with:

bash
pytest test_jar.py

---
## Test cases include:

Initializing a jar with valid and invalid capacities

Depositing cookies within capacity

Withdrawing cookies within available size

Checking str outputs correct number of emojis