def main():
<<<<<<< HEAD
    greeting = input("Greet Customer:").strip().lower()
=======
    greeting = input("Greet Customer:")
>>>>>>> 4e8093f5474ca1ab25b9cd33131df1c208bf3562
    print(f"${value(greeting)}")


def value(greeting):
<<<<<<< HEAD

=======
    
    greeting = greeting.strip().lower()
    
>>>>>>> 4e8093f5474ca1ab25b9cd33131df1c208bf3562
    if greeting.startswith("hello"):
        return 0
    elif greeting.startswith("h"):
        return 20
    else:
        return 100


if __name__ == "__main__":

    main()
