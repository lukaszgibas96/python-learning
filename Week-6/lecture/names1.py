# Lecture exercise          /open() /.write()   /close()    /with ... as ...
name = input("What's your name? ")

with open("names.txt", "a") as file:
    file.write(f"{name}\n")
