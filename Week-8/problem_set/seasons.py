# problem set - Seasons of love

import sys
from datetime import date

class Date:
    ...

def main():

    try:
        birthday = input("Date of birth: ")
        birthday = date.fromisoformat(birthday)
        today = date.fromisoformat("2026-01-01")


        

    except ValueError:
        sys.exit("Invalid date")

if __name__ == "__main__":
    main()