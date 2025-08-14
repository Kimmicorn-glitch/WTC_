import emoji

def emoji_text():
    text = input("Input: ")

    print( emoji.emojize(text, language='alias'))

if __name__ == "__main__":
    emoji_text()
