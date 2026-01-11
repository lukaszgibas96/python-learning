# Problem Set 1 - Home Federal Saving Bank          /.find()
greeting = input("Greeting: ").lstrip().lower()

word = greeting.find("hello")

char = greeting.find("h")

if word == 0:
    print("0$")

elif word != 0 and char == 0:
    print("20$")

else:
    print("100$")


