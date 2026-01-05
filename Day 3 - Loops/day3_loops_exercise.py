
def give_number():
    
    while True:
        n = int(input("Give me a number greater than 0:"))
        if n > 0:
            return n
        
def main():

    number = give_number()
    print(f"podana liczba > 0 to {number}")
    

main()

