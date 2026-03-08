# Problem Set 6 - CS50 P-shirt

import sys
from PIL import Image, ImageOps
import os

extension = [".jpg", ".jpeg", ".png"]

def main():
    try:
        
        check_command()
        input_file = sys.argv[1]
        output_file = sys.argv[2]

# Input and Output file extensions check
        input_ext = extract_extension(input_file)
        if input_ext not in extension:
            sys.exit("Invalid input")

        output_ext = extract_extension(output_file)
        if output_ext not in extension:
            sys.exit("Invalid output")

# Check whether input and output file extensions are the same
        if input_ext != output_ext:
            sys.exit("Input and output have different extensions")

        with Image.open(input_file) as image, Image.open("shirt.png") as shirt:

            image = ImageOps.fit(image, shirt.size)
            image.paste(shirt,(0,0), shirt)
            image.save(output_file)        

    except FileNotFoundError:
        sys.exit("Specified input does not exist")


def check_command():

    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
        
def extract_extension(file_name):
    root, ext = os.path.splitext(file_name)
    return ext.lower()


if __name__ == "__main__":
    main()

