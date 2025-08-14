def twitter():
    twttr_str = input("Input: ").strip()
    output = ""
    vowels = "aeiouAEIOU"

    for character in twttr_str:
        if character not in vowels:
            output += character
    print("Output:", output)
twitter()
