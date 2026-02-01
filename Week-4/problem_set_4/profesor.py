# Problem set 4 - Little professor
    
import random


def main():

    n = get_level()
    wrong = 0
    score = 0


    for i in range(10):

        x,y = generate_integer(n)
        result = x + y
        while wrong != 3:
            
            try:

                answer = int(input(f"{x} + {y}= "))

                if answer == result:
                    score += 1
                    break
                else:
                    wrong += 1
            except ValueError:
                print("EEE")
                wrong += 1

        print(f"{x} + {y} = {result}")
        wrong = 0

    print(f"Score: {score}")
  



def get_level():

    while True:

        try:
            n = int(input("Level: "))
            if n in (1,2,3):
                return n
        except ValueError:
            print("EEE")

    
def generate_integer(level):

    ranges = {1:(0,9), 2:(10,99), 3:(100,999)}
    try:

        current_range = ranges[level]

        x = random.randint(*current_range)
        y = random.randint(*current_range)  

        return x, y
    except ValueError:
        print("EEE")


if __name__ == "__main__":
    main()