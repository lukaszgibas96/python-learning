# Problem set 7 - watch on YouTube

import re

def main():
    print(parse(input("HTML: ")))


def parse(s):

    pattern = r".*https?://(?:www\.)?youtube\.com/embed/(.+?)\""
    match = re.search(pattern,s)

    if match:
        address = match.group(1)
        return "https://youtu.be/" + address
    else:
        return None

if __name__ == "__main__":
    main()