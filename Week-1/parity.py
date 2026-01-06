
def main():
    x = int(input("What's x?\n"))

    if is_even(x):
        print("EVEN")
    else:
        print("ODD")

#Parity function version 1 

# def is_even(n):
#     if n % 2 ==0:
#         return True
#     else:
#         return False


# Parity function version 2

# def is_even(n):
#     return True if n % 2 == 0 else False

# Parity function version 3

def is_even(n):
    return n % 2 ==0
    

main()

