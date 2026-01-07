# Problem Set - Einstein e= mc^2
c = int(300000000) # meter per sec 

def main():

    mass = int(input("What's mass? [kg]"))

    print(f"{energy(mass):,} [J] ")

def energy(m):

    return m * c ** 2

main()