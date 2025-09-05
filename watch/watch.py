import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
#https://regex101.com/library/qE6dO9?orderBy=RELEVANCE&search=youtube+
#stack
    match = re.search(r'<iframe[^>]*src="(https?://(?:www\.)?youtube\.com/embed/([\w-]+))"',s)
    if match:
        return f"https://youtu.be/{match.group(2)}"
    return None

if __name__ == "__main__":
    main()
