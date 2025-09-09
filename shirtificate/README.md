### CS50 Shirtificate – shirtificate.py

This project generates a personalized CS50 shirt certificate as a PDF using fpdf2.

## Features
- Prompts user for their name
- Creates a PDF in portrait A4 format
- Adds a centered title at the top
- Places a shirt image centered horizontally
- Overlays the user’s name on top of the shirt in white text
- Saves the PDF as shirtificate.pdf

## What I learned
- How to use the FPDF class from fpdf2
- Page orientation, size, and automatic page break control
- Adding titles and images to a PDF
- Font, size, and color handling
- Centering text using get_string_width
- Adjusting coordinates for precise layout

## Challenges
- Forgetting parentheses on pdf.add_page()
- Arial font fallback warning, fixed by switching to Helvetica
- Deprecation warning for ln=True, fixed using XPos and YPos
- Aligning name text correctly over the shirt image

## How to run
Make sure `shirtificate.png` is in the same folder. Then run:

## bash
python shirtificate.py
Enter your name when prompted and the PDF will be generated.