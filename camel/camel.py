def camelcase():
    camel= input("CamelCase: ").strip()
    snake= ""

    for characters in camel:
        if characters == characters.upper():
            if snake != "":
                snake += "_"
            snake += characters.lower()
        else:
            snake += characters

    print("snake_case: ", snake)

camelcase()


