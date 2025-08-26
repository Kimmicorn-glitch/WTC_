def is_valid(plate):
    
    #try if not statements 
    if not (2 <= len(plate) <= 6):
        return False

    
    if not plate.isalnum():
        return False

    # I changed this to check the last digit is a number.
    if plate[-1].isdigit() is False:
        return False

    #note. this is where I thought of simplifying the code 
    for char in plate:
        if char.isdigit():
            if char == "0":
                return False
            break
    #the return here is going to do what you had wrote initially -
    # in your code but only after checking the requiremnts are met
    return True 

def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

main()