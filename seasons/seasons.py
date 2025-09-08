from datetime import date
import sys
import Inflect # pyright: ignore[reportMissingImports]

def main():
    birthday_str = input("Enter your date of birth: ")
    try:
        birthday = date.fromisoformat(birthday_str)
    except ValueError:
        sys.exit("Invalid date")

    minutes = age_in_min(birthday)
    print(minutes_to_words(minutes))

def age_in_min(birthday):
    today= date.today()
    diff = today - birthday
    return diff.days * 24 *60


def minutes_to_words(minutes):
    p = Inflect.engine() # pyright: ignore[reportUndefinedVariable]
    words = p.number_to_words(minutes, andword="")

    return words.capitalize() + " minutes"


if __name__ == "__main__":
    main()
