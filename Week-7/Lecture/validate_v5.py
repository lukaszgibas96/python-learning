import re

email = input("What's your email?").strip()


if re.search(r"^\w+@\w+\.(edu|com|gov|net|org)$", email):
    print("Valid")
else:
    print("Invalid ")

 