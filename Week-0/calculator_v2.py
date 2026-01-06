def main():

    x = int(input("What's x? "))
    print(f"{x} squared is {square(x)}")

# def function to square number x
def square(n):

#__ Method 1 

    #return n * n

#__ Method 2 

    #return n ** n 

#__ Method 3 

    return pow(n,2) 

main()
