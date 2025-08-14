def deep_thought():
    answer = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ").strip().lower()

    normalised = " ".join(answer.split())

    if normalised == "42" or normalised == "forty two" or normalised == "forty-two":
        print("Yes")
    else:
        print("No")

if __name__ == "__main__":
    deep_thought()
