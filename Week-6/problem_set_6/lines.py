# Problem set 6 - Lines of code 

import sys


def main():

    try:
        check_command()
        file_name = sys.argv[1]
        check_name(file_name)

        with open(file_name, "r") as f:
            code_line = count_line(f.readlines())
            print(code_line)

    except FileNotFoundError:
        sys.exit("File does not exist")
    

def check_command():

    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) == 2:
        return
    else:
        sys.exit("Too many command-line arguments")

def check_name(name):

    if name.endswith(".py"):
        return name
    else:
        sys.exit("Not a Python file")

def count_line(file):

    count = 0
    for line in file:
        if line.strip().startswith("#") or line.strip() == "":
            pass
        else:
            count += 1
            
    return count
        
if __name__ == "__main__":
    main()

