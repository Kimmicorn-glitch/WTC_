def convert(text):

    return text.replace(":)","🙂").replace(":(","🙁")

def main():

    user_input = input("Enter your text with emoticons:")
    print(convert(user_input))

main()
