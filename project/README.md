### Celsius Converter

**Video Demo**: https://youtu.be/KdqRbdLHKvM

## Description:

This Project is a Python program that converts temperatures from Celsius into Fahrenheit and Kelvin. It was developed as part of the CS50 Final Projet and demonstrates structured programming, error handling, and automated testing with pytest.

The motivation behind the project was to build a simple but robust tool that emphasizes:
- Input validation
- user friendly prompts
Additionally, I wanted to practice writing professional documentation and tests.

---

## Project Files

- project.py
  Contains the proagam and required functions. Handles userinteraction, input validation and tempretur conversions.

- test_project.py
  Contains unit test written with pytest to verify the program's core funtions, including edge cases and invalid inputs.

- requirements.txt
  Lists dependencies for the project

- README.md/
  The documentation you're currently reading.

---

## Functions
 - get_celsius()
    Prompts the user for a Celsius valu, ensures valid input, and returns the number as a float. Handles invalid input with friendly error message.
 - to_Fahrenheit(celsius)
    Converts Celsius to Fahrenheit using a formuala:
<     F = (C * 9/5) + 32
 - to_Kelvin(celsius)
    Converts Celsius to Kelvin using a formula:
<     K = C + 273.15
 -  main():
    COordinates the program flow :
     1. gets inputs,
     2. prompts user for conversion type,
     3. perfoms conversions
     4. display results

---
## Requirements
  Dependencies are listed in reqirements.txt:

  ```
  pytest
  ```
  install with:

  ```
  pip install -r requirements.txt
  ```
---

## Testing
- This project uses *pytest* for testing
    Run tests with:
    ```
    bash
    pytest
    ```
Tests cover:

- Valid conversions (Celsius -> Fahrenheit, Celsius -> Kelvin)

- Edge cases (e.g. absolute zero)

- Invalid inputs (non-numeric values)


## Example Run

Enter temperature in Celsius: 25

 Choose conversion type:
 1 - Celsius to Fahrenheit
 2 - Celsius to Kelvin
 3 - both conversions

Enter (1/2/3): 3

25.0°C is equal to 77.0°F
25.0°C is equal to 298.15K
----



## Reflection
 This project reflects my learning journey
 - Paying attention to detail : I implemented input validations and friendly error handling
 - Structure: Functions are clean, separate and reusable
 - Commitment to growth: I included automated tests beyond the minimum requirements.

Through this project,I strengthened my confidence in writing testable code.
