## Figlet (Text Art Generator) 

## What it does
Accepts a user-provided string and outputs it large ASCII-art text (FIGlet-style). Perfect for dramatic terminal demo title headers, README banners, or just plain showing off.

## How it works
- Option A: Imports the `pyfiglet` library for loads of font options: `pyfiglet.figlet_format(text, font="slant")`.
- Option B: Without an external lib, uses a small built-in map for small characters and builds output line by line.

## What I grappled with 
- Dealing with external dependencies (Windows pip permissions, virtualenv confusion).
- Maintaining multi-line output neatly aligned for variable fonts/special characters.
- Dealing with extremely long inputs that exceed terminal lines.

## How I fixed it 

- Opt-in auto-detection: detect `pyfiglet` internally and use internal mapper as a replacement. Example:
  ```py
  try:
      import pyfiglet
      use_pyfiglet = True
  except ImportError:
      use_pyfiglet = False
```

##How to run

```bash
Copy code
# if you want the full font set:
pip install pyfiglet
```
# run

```python figlet.py "Hello World" --font slant
Example

bash
Copy code
$ python figlet.py "Hi Kim"
# prints big ASCII HI
```
## Resources

pyfiglet docs.

