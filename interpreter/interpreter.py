def interpreter():
    equation = input(" Enter your math equation (use spaces, e.g., 5 + 2): ").strip()
#reminder. add a computed comment to tell user to add spaces between numbers cause its cause errors.
    


    x, operator, y = equation.split(" ")


    x = float(x)
    y = float(y)

    if operator  == "+":
        return x + y
    elif operator == "-":
        return x - y
    elif operator == "/":
        return x/y
    elif operator == "*":
        return x * y

print(interpreter())

