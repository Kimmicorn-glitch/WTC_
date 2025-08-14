def grocery_list():
    counts= {}

    while True:
        try:
            item = input().strip().lower()
            if item == "":
                continue
            counts[item] = counts.get(item, 0) + 1
        except EOFError:
            break

    for item in sorted(counts):
        print(f"{counts[item]} {item.upper()}")



grocery_list()

