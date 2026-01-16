# Problem Set 2 - Just setting up my twttr

vowels = ["A","a","E","e","I","i","O","o","U","u"]

def main ():

    inpt = input("Input:")
    otpt = []

    for char in inpt:
        if char not in vowels:
            otpt.append(char)

    otpt = "".join(otpt)
    print(f"Output: {otpt}")
    



main ()