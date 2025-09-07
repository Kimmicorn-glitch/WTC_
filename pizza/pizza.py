from tabulate import tabulate
import sys
import csv

#needs. a pizza. an argument. a table.

def main():
    check_args()
    file_name= sys.argv[1]
    table = read_csv(file_name)
    print(tabulate(table, headers= "keys", tablefmt ="grid"))

def check_args():
    if len(sys.argv) <2:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    if not sys.argv[1].endswith(".csv"):
        sys.exit("Not CSV file")

def read_csv(file_name):
    try:
        with open(file_name , "r") as file:
            reader = csv.DictReader(file)
            return list(reader)
    except FileNotFoundError:
        sys.exit("File does not exist")


if __name__ == "__main__":
    main()
