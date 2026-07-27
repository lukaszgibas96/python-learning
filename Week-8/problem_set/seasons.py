# problem set - Seasons of love

import sys
from datetime import date
import inflect
p = inflect.engine()

def main():

    try:
        birthday = input("Date of birth: ")
        today = date.today()
        transcription = convert(birthday, today)
        print(f"{transcription} minutes")

    except ValueError:
        sys.exit("Invalid date")


def convert(input_date, reference_date):
    input_date = date.fromisoformat(input_date)
    difference = reference_date - input_date
    minutes = difference.days * 24 * 60

    return p.number_to_words(minutes).replace(" and ", " ")


if __name__ == "__main__":
    main()