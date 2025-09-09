# CS50 Python Projects – Kimberley Bezuidenhout

Welcome to my collection of CS50 Python projects. This repo documents my journey through Harvard’s Introduction to Programming with Python. Here, I learned to bend strings, wrangle numbers, tame loops, and occasionally argue with my code until it agreed with me.

These projects range from quirky exercises like faces.py and playback.py to more practical programs like bitcoin.py, meal.py, and PDF generation with shirtificate.py. Each one represents a step in my growth as a Python programmer.

---

## Projects Overview

### Cookie Jar (jar.py)
- Implements a class-based cookie jar with deposit and withdraw methods.
- Displays cookies as emojis and enforces capacity limits.
- Includes test_jar.py for unit testing with pytest.
- Learned: classes, properties, exception handling, testing instance methods.

### CS50 Shirtificate (shirtificate.py)
- Generates a PDF certificate with a shirt image and user’s name.
- Uses fpdf2, handles text alignment, font/color control, and image placement.
- Learned: PDF generation, text centering, font management, coordinate placement.

### Age in Minutes (seasons.py)
- Calculates a person’s age in minutes from their birthdate.
- Converts minutes into words.
- Includes test_seasons.py for pytest tests.
- Learned: datetime calculations, number-to-words conversion, input validation.

### Scourgify (scourgify.py)
- Cleans a CSV of student names, splitting full names into first and last names.
- Writes a new CSV in a standardized format with first, last, house.
- Learned: CSV reading/writing, command-line arguments with sys.argv, error handling.

### Playback (playback.py)
- Converts text input to add ellipses between words.
- Learned: string manipulation, loops, text formatting.

### Indoor (indoor.py)
- Converts input text to lowercase.
- Learned: string methods and input handling.

### Faces (faces.py)
- Replaces emoticons with corresponding emojis.
- Learned: order of transformations matters in string replacement.

### Twttr (twttr.py)
- Removes vowels from input text.
- Learned: string filtering and comprehension logic.

### Coke Machine (coke.py)
- Simulates a vending machine that accepts coins and dispenses products.
- Learned: loops, input validation, handling numeric values.

### Fuel (fuel.py)
- Converts user-input fractions into fuel gauge display.
- Learned: fraction parsing, exception handling, input validation.

### Meal (meal.py)
- Suggests meals based on time of day input.
- Learned: time comparison, conditionals, float conversion.

### Pizza (pizza.py)
- Calculates pizza slices needed per person.
- Learned: arithmetic operations, input sanitization.

### Nutrition (nutrition.py)
- Returns calories for given fruit input.
- Learned: dictionaries for mapping, input handling.

### Plates (plates.py)
- Validates vanity license plates based on given rules.
- Learned: string checks, conditionals, multiple constraints.

### Professor (professor.py)
- Randomly generates a professor’s level and prints results.
- Learned: loops, functions, input validation, random module.

### Tip (tip.py)
- Calculates tips with a cheeky message for small amounts.
- Learned: string parsing, float calculations, input sanitization.

### Um (um.py)
- Text analysis/counting program (CS50 short problem).
- Learned: input validation, counting occurrences.

### Numb3rs / Working / Test Scripts
- Scripts for testing numeric input, validating functions, and practicing Python basics.
- Learned: testing, debugging, automation with pytest.

---

## My Journey & Struggles

- **Getting back into Python:** strings are immutable, indentation matters, lots of trial-and-error.
- **Input validation nightmares:** empty strings, invalid numbers, unexpected formats.
- **Transformation logic:** order of operations matters (faces.py, twttr.py).
- **Time comparisons:** converting everything to consistent formats saved headaches.
- **APIs and real-world data:** bitcoin.py tested patience with requests, JSON, and exceptions.
- **Avoiding overcomplication:** simple loops and built-ins beat nested overengineering.

---

## How I Solve Problems

- Break it down: tackle one requirement at a time.
- Test small: REPL and print statements validate each function.
- Use Python built-ins: .replace(), .lower(), .split(), dictionaries.
- Read the docs: Python docs, CS50 lectures, Stack Overflow.
- Iterate: fail, improve, repeat.

---

## Resources That Helped

- CS50P Lectures & Notes
- Python 3 Official Documentation
- Stack Overflow
- CoinCap API Documentation (bitcoin.py)
- Online tutorials and forums

---

## Author

Kimberley Bezuidenhout

Note: Some programs are simple, some weirdly fun, some just me arguing with Python until it agreed. No semicolons were harmed in the making of these projects.
