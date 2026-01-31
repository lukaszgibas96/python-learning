# Problem set 4 - Frank, Ian and Glen's Letters

from pyfiglet import Figlet
import sys
import random

figlet = Figlet()
fonts = figlet.getFonts()

def main():

    if len(sys.argv) < 2:
        f = random.choice(fonts)
        convert(f)
    elif len(sys.argv) == 3:
        if sys.argv[1] == "-f" or sys.argv[1] == "--font":
            if sys.argv[2] in fonts:
                f = sys.argv[2]
                convert(f)
            else:
                sys.exit("Invalid usage")
        else:
            sys.exit("Invalid usage")
        
    else:
        sys.exit("Invalid usage")


def convert(f):
    text = input("Input: ")
    figlet.setFont(font = f)
    output = figlet.renderText(text)
    print(output)

if __name__ == "__main__":
    main()