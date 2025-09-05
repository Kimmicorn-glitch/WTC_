import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):


    pattern = r"^([1-9]|1[0-2])(?::([0-5][0-9]))? (AM|PM) to ([1-9]|1[0-2])(?::([0-5][0-9]))? (AM|PM)$"

    match = re.search(pattern, s)
    if not match:
        raise ValueError

    h1, m1, p1,h2,m2,p2 = match.groups()
    m1 = int(m1) if m1 else 0
    m2 = int(m2) if m2 else 0
    h1, h2 = int(h1), int(h2)

    if not (1 <= h1 <= 12 and 0 <= m1 <= 59):
        raise ValueError
    if not (1 <= h2 <= 12 and 0 <= m2 <= 59):
        raise ValueError

    return f"{to_24(h1,m1,p1)} to {to_24(h2,m2,p2)}"

def to_24(h,m,p):

    if p == "AM":
        if h == 12:
            h = 0
    else:

        if h != 12:
            h += 12
    return f"{h:02d}:{m:02}"

if __name__== "__main__":
    main()
