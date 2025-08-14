import sys
from pyfiglet import Figlet

def main():

    figlet = Figlet()
    font = "standard"

    if len(sys.argv) == 1:

        pass
    elif len(sys.argv) == 3 and sys.argv[1] == "-f":
        font = sys.argv[2]
        if font not in figlet.getFonts():
            print("Invalid font")
            sys.exit(1)
    else:
      print("Usage: python figlet.py [-f font]")
      sys.exit(1)




    figlet.setFont(font=font)

    text = input("Input: ")



    print("Output: ",figlet.renderText(text))

if __name__ == "__main__":
   main()
