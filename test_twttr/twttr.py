''''
def twitter():
    twttr_str = input("Input: ").strip()
    output = ""
    vowels = "aeiouAEIOU"

    for character in twttr_str:
        if character not in vowels:
            output += character
    print("Output:", output)
twitter()
'''
def main():
    user_input = input("Input: ").strip()
    result = shorten(user_input)
    print("Output:",result)


def shorten(text):
    vowels = "aeiouAEIOU"
    output = ""
    for character in text:
          if character not in vowels:
               output += character
    return output

if __name__ == "__main__":
    main()