def shorten(word):

    vowels = "aeiouAEIOU"
    output = ""

    for character in word:
        if character not in vowels:
            output += character
    return output

def main():
    twttr_str = input("Input: ").strip()
    print("Output:", shorten(twttr_str))


if __name__ == "__main__":
    shorten()
