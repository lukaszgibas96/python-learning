name = input("what's your name?")

match name:
    
    case "Lukasz" | "Piotr" |   "Adam":
        print("Krakow")
    case "Bartek":
        print("Konin")
    case _:
        print("Who?")



# if name == "Lukasz":
#     print("Krakow")
# elif name == "Piotr":
#     print("Krakow")
# elif name == "Adam":
#     print("Krakow")
# elif name == "Bartek":
#     print("Konin")
# else:
#     print("who?")

    