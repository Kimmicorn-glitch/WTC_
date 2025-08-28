import sys
import os


def lines():
   check_args()
   file_name = sys.argv[1]
   print(count_lines(file_name))


def check_args():
   if len(sys.argv) != 2:
      sys.exit("Too few command-line arguments")
   if not sys.argv[1].endswith(".py"):
      sys.exit("Not a Python File")
   if not os.path.isfile(sys.argv[1]):
      sys.exit("File does not exist")

#okay this is the hard part please bear with me if its not right.
#def. to try something and if not do not count. sounds simple. mxm.

def count_lines(file_name):
   try:
      with open(file_name, "r") as file:
         count = 0
         for line in file:
            stripped = line.lstrip()
            if stripped and not stripped.startswith("#"):
               count += 1
         return count
   except FileNotFoundError:
      sys.exit("File not found")


if __name__ == "__main__":
   lines()

