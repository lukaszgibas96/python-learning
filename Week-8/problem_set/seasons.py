# problem set - Seasons of love

import sys
from datetime import date
import inflect
p = inflect.engine()

def main():

    try:
        birthday = input("Date of birth: ")
        birthday = date.fromisoformat(birthday)
        today = date.today()
        difference = today - birthday
        minutes = difference.days * 24 * 60

        transcription = p.number_to_words(minutes).replace(" and ", " ")
        print(transcription)

    except ValueError:
        sys.exit("Invalid date")

if __name__ == "__main__":
    main()