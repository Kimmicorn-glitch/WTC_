def main():
    time_str = input("What time is it? ").strip().lower()
    hours = convert(time_str)

    if hours == -1:
        return

    if 7 <= hours <= 8:
        print("breakfast time")
    elif 12 <= hours <= 13:
        print("lunch time")
    elif 18 <= hours <= 19:
        print("dinner time")


def convert(time):
    #reminder. Remove words like o'clock or oclock
    time = time.replace("o'clock", "").replace("oclock", "").strip()

    if ":" in time:
        parts = time.split(":")
        if len(parts) != 2:
            return -1
        if parts[0].isdigit() and parts[1].isdigit():
            hours = int(parts[0])
            minutes = int(parts[1])
        else:
            return -1
    elif time.isdigit():
        hours = int(time)
        minutes = 0
    else:
        return -1

    return hours + minutes / 60


if __name__ == "__main__":
    main()
