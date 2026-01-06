distances = {

    "Voyager 1" : 163,
    "Voyager 2" : 136,
    "Pioneer 10" : 80,
    "New Horizons" : 58,
    "Pioneer 11" : 44
}

def main():

    for name in distances.keys():
        print(f"{name} is {distances[name]} AU from the Earth")

    print()

    for distance in distances.values():
        print(f"{distance} AU is {convert(distance)} m")

def convert(au):
    return au * 149597870700

# 1st method - long 

    # print("Voyager 1" , distances["Voyager 1"] + " AU", sep = " - ")
    # print("Voyager 2" , distances["Voyager 2"] + " AU", sep = " - ")
    # print("Pioneer 10" , distances["Pioneer 10"] + " AU", sep = " - ")
    # print("New Horizons" , distances["New Horizons"] + " AU", sep = " - ")
    # print("Pioneer 11" , distances["Pioneer 11"] + " AU", sep = " - ")

main()