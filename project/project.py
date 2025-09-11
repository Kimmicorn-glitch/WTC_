
def get_celsius():
    while True:
        try:
            temp = float(input("Enter temperature in Celsius: "))
            return temp
        except ValueError:
            print("Invalid input. -_- please enter a number")


def to_Fahrenheit(celsius):
    return (celsius * 9/5) + 32

def to_Kelvin(celsius):
    return celsius + 273.15


def main():
    celsius = get_celsius()
    while True:
        print("\nChoose conversion type:")
        print("1 - Celsius to Fahrenheit")
        print("2 - Celsius to Kelvin")
        print("3 - both conversions\n")
        print()

        choice = input("Enter (1/2/3): ").strip()
        print()

        try:
            choice = int(choice)
        except ValueError:
            print("Invalide choice... -_- please enter 1, 2, or 3.\n")
            continue

        if choice == 1:
            print(f"{celsius}°C is equal to {to_Fahrenheit(celsius)}°F\n")
            break
        elif choice == 2:
            print(f"{celsius}°C is equal to {to_Kelvin(celsius)}K\n")
            break
        elif choice == 3:
            print(f"{celsius}°C is equal to {to_Fahrenheit(celsius)}°F")
            print(f"{celsius}°C is equal to {to_Kelvin(celsius)}K\n")
            break
        else:
            print("Invalid choice. run it again and choose 1, 2, or 3.\n")


if __name__ == "__main__":
    main()
