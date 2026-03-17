# Problem set 7 - Numb3rs

#.#.#.#

import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):

    pattern = r"^(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})$"

    match = re.search(pattern,ip)

    if match:
        for i in range(1,5):
            group = match.group(i)
            
            if len(group) > 1 and group.startswith("0"):
                return False
                
            if 0<= int(group)<= 255:
                continue
            else:
                return False
        return True
    else:
        return False


if __name__ == "__main__":
    main()