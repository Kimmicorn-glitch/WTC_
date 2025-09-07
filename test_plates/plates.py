def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_letter(character):
    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if character in letters:
        return True
    else:
        return False

def is_valid(s):
    if len(s) < 2 or len(s) > 6:
        return False

    if not is_letter(s[0]) or not is_letter(s[1]):
        return False

    digits = "0123456789"
    for character in s :
        if character not in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" and character not in digits:
            return False

    first_digit_index = len(s)
    for i in range(len(s)):
        if s[i] in digits:
            first_digit_index = i
            break
    for j in range(first_digit_index, len(s)):
        if s[j] not in digits:
            return False

    if first_digit_index < len(s) and s[first_digit_index] == '0':
        return False

    return True

if __name__ == "__main__":

    main()
