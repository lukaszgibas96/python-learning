# Problem set 4 - Response Validation

import re

def main():
    
    email = input("What's your email address? ").lower()

    pattern = r"^[a-zA-Z0-9.!#$%&'*+\/=?^_`{|}~-]+@[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?(?:\.[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?)*$"
    match = re.search(pattern, email,)

    if match:
        print("Valid")
    else:
        print("Invalid")

if __name__ == "__main__":
    main()