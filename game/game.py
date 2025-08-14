import random

def game():
    level = get_level()
    secret = random.randint(1, level)
    guess_number(secret)

def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level > 0:
                return level
        except ValueError:
            pass

def guess_number(secret):
    while True:
        try:
            guess = int(input("Guess: "))
            if guess <= 0:
                continue
        except ValueError:
            continue

        if guess < secret:
            print("Too small!")
        elif guess > secret:
            print("Too large!")
        else:
            print("Just right!")
            break

if __name__ == "__main__":
    game()
