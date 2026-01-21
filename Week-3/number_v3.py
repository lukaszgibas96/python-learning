# Week 3 - Exceptions - Lecture v3             /get_int()   /try:   /except ValueError:  /pass

def main():

    x = get_int("What's x? ")
    print(f"x is {x}")



def get_int(prompt):
    while True:
        try: 
            x = int(input(prompt))
            return x 
        except ValueError:
            pass
main()

         