# Problem set 6 - Pizza Py

import sys
import csv
from tabulate import tabulate

def main():
    try:
        check_command()
        file_name = sys.argv[1]
        check_extension(file_name)
        menu = []

        with open(file_name, "r") as file:
            reader = csv.DictReader(file)
            
            for row in reader:
                menu.append(row)
            print(tabulate(menu, headers="keys",tablefmt="grid"))
    
    except FileNotFoundError:
        sys.exit("File does not exist")

   

def check_command():
    
    if len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    elif len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    else:
        return
    
def check_extension(name):
    if name.endswith(".csv"):
        return name
    else:
        sys.exit("Not a CSV file")

if __name__ == "__main__":
    main()