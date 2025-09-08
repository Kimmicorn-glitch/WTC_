from datetime import date
import sys

def main():
    birthday = get_date(input("Date of birth: "))
    mins = age_in_min(birthday)
    print(to_words(mins))

def get_date(s):
    try:
        return date.fromisoformat(s)
    except ValueError:
        sys.exit("Invalid date")

def age_in_min(birthday):
    today = date.today()
    return (today - birthday).days * 24 * 60

def to_words(n):
    return num_to_words(n).capitalize() + " minutes"

def num_to_words(n):
    ones = ["","one","two","three","four","five","six","seven","eight","nine"]
    teens = ["ten","eleven","twelve","thirteen","fourteen","fifteen",
             "sixteen","seventeen","eighteen","nineteen"]
    tens = ["","","twenty","thirty","forty","fifty",
            "sixty","seventy","eighty","ninety"]

    if n < 10:
        return ones[n]
    if n < 20:
        return teens[n-10]
    if n < 100:
        return tens[n//10] + ("" if n % 10 == 0 else "-" + ones[n % 10])
    if n < 1000:
        return ones[n//100] + " hundred" + ("" if n % 100 == 0 else " " + num_to_words(n % 100))
    if n < 1_000_000:
        remainder = n % 1000
        thousands = num_to_words(n // 1000) + " thousand"
        if remainder == 0:
            return thousands
        else:
            return thousands + ", " + num_to_words(remainder)
    if n < 1_000_000_000:
        remainder = n % 1_000_000
        millions = num_to_words(n // 1_000_000) + " million"
        if remainder == 0:
            return millions
        else:
            return millions + ", " + num_to_words(remainder)

    return str(n)

if __name__== "__main__":
    main()