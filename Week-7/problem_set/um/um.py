# Problem set 7 - Regular, um, Expressions

import re
import sys


def main():
    print(count(input("Text: ")))


def count(s):
    pattern = r"(^| )um(?=(\W+|$))"
    match = re.findall(pattern,s,re.IGNORECASE)
    quantity = len(match)
    return quantity

if __name__ == "__main__":
    main()

