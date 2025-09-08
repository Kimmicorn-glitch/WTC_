from datetime import date
import sys
import inflect 


def parse_birthday(birthday_str):
    try:
        return date.fromisoformat(birthday_str)
    except ValueError:
        sys.exit("Invalid date")


def age_in_min(birthday):
    today = date.today()
    diff = today - birthday
    return diff.days * 24 *60


def minutes_to_words(minutes):
    p = inflect.engine() 
    words = p.number_to_words(minutes, andword="")

    return words.capitalize() + " minutes"

def main():
    birthday_str = input("Enter your date of birth: ")
    birthday = parse_birthday(birthday_str)
    minutes = age_in_min(birthday)
    print(minutes_to_words(minutes))




if __name__ == "__main__":
    main()
