#this is going to be a long one...

import sys
import csv

def scourgify():
    check_args()
    input_file = sys.argv[1]
    output_file = sys.argv[2]

    rows = read_csv(input_file)
    clean = clean_data(rows)
    write_csv(output_file, clean)

def check_args():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    if not sys.argv[1].endswith(".csv"):
        sys.exit("Invalid file type")

def read_csv(input_file):
    try:
        with open(input_file, newline="") as file:
           return list(csv.DictReader(file))

    except FileNotFoundError:
        sys.exit("Could not read invalid_file.csv")

def clean_data(rows):
        cleaned = []
        for row in rows:
            last, first = row["name"].split(", ")
            cleaned.append({"first": first, "last": last, "house": row["house"] })
        return cleaned


def write_csv(output_file, rows):
    with open(output_file, "w", newline ="") as f:
        fieldnames = ["first", "last","house"]
        writer = csv.DictWriter(f, fieldnames = fieldnames)
        writer.writeheader()
        writer.writerows(rows)


if __name__ == "__main__":
    scourgify()
