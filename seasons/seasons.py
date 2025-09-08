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
    
    def num_into_chunks(num):
        if num < 10:
            return ones[num]
        if num < 20:
            return teens[num-10]
        if num < 100: 
            return tens[num//10] + ("" if num%10==0 else "-" + ones[num%10])
        if num < 1000: 
            return ones[num//100] + " hundred" + ("" if num%100==0 else " " + num_into_chunks(num%100))
        if num < 1_000_000: 
            return num_into_chunks(num//1000) + " thousand" + ("," if num%1000==0 else ", " + num_into_chunks(num%1000))
        if num < 1_000_000_000:    
            return num_into_chunks(num//1_000_000) + " million" + ("," if num%1_000_000==0 else ", " + num_into_chunks(num%1_000_000))
       
        return str(num)

    return num_into_chunks(n)

if __name__ == "__main__":
    main()