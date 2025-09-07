def main():
    while True:
        try:
            fraction = input("Fraction: ")
            percentage = convert(fraction)
            print(gauge(percentage))
            break
        except (ValueError, ZeroDivisionError):
<<<<<<< HEAD
            # Reprompt on invalid input
=======
            
>>>>>>> 4e8093f5474ca1ab25b9cd33131df1c208bf3562
            pass


def convert(fraction):
    try:
        x, y = fraction.split("/")
        x = int(x)
        y = int(y)
    except ValueError:
<<<<<<< HEAD
        # not integers or wrong format
=======
>>>>>>> 4e8093f5474ca1ab25b9cd33131df1c208bf3562
        raise ValueError

    if y == 0:
        raise ZeroDivisionError

<<<<<<< HEAD
=======
    if x < 0 or y< 0:
        raise ValueError

>>>>>>> 4e8093f5474ca1ab25b9cd33131df1c208bf3562
    if x > y:
        raise ValueError

    return round((x / y) * 100)


def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage}%"


if __name__ == "__main__":
    main()
