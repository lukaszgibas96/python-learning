# Problem set 5 - Back to the bank

def main():

    greeting = input("Greeting: ").lstrip().lower()
    result = value(greeting)
    print(f"${result}")
    

def value(greeting):
    
    word = greeting.find("hello")
    char = greeting.find("h")

    if word == 0:
        return 0
    elif word != 0 and char == 0:
        return 20
    else:
        return 100


if __name__ == "__main__":
    main()



