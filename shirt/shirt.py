import sys
import os
from PIL import Image, ImageOps

def photoshop():
    input_file, output_file = check_args()
    process_image(input_file, output_file)

def check_args():

  #  def validate_args(args):
    if len(sys.argv) !=3:
        sys.exit("Too few command-line arguments")

    if len(sys.argv) >3:
        sys.exit("Too many command-line arguments")

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    valid_extensions = [".jpg",".jpeg",".png"]
    in_ext = os.path.splitext(input_file)[1].lower()
    out_ext = os.path.splitext(output_file)[1].lower()

    if in_ext not in valid_extensions or out_ext not in valid_extensions:
        sys.exit("Invalid output")

    if in_ext != out_ext:
        sys.exit("Input and output have different extensions")

    if not os.path.isfile(input_file):
        sys.exit("Input does not exist")

    return input_file, output_file

#processing the images now ref - geeks4geeks & cs50 videos

def process_image(input_file, output_file):

    try:
        shirt = Image.open("shirt.png")
    except FileNotFoundError:
        sys.exit("shirt.png not found")

    try:
        photo = Image.open(input_file)
    except FileNotFoundError:
        sys.exit("Input does not exist")


    photo = ImageOps.fit(photo, shirt.size)
    photo.paste(shirt, (0,0),shirt)
    photo.save(output_file)


if __name__ == "__main__":
    photoshop()
