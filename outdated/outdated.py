def outdated():
    months = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December"
]

    while True:
        date = input("Date: ").strip()

        try:
            if "/" in date:
                m, d, y = date.split("/")
                m, d, y = int(m), int(d), int(y)
            else:
                if "," not in date:
                    raise ValueError("Missing comma in textual date format")

                parts = date.replace(",", "").split()
                if len(parts) != 3:

                    raise ValueError("Invalid textual date format")
                month_name = parts[0]
                day_str = parts[1]
                year_str = parts[2]

                if not day_str.endswith(","):
                    raise ValueError("Day must be followed by a comma")

                day = day_str[:-1]

                m = months.index(month_name) + 1
                d = int(day)
                y = int(year_str)

            if 1 <= m <= 12 and 1 <= d <= 31:
                print(f"{y:04d}-{m:02d}-{d:02d}")
                break
            else:
                continue
        except(ValueError,IndexError):
            pass

if __name__ == "__main__":
    outdated()
