# Creating new file. First move in new environment.

name = input("What's your name? ").strip().title()

first, last = name.split(" ")

print(f"Hello, {first}")
