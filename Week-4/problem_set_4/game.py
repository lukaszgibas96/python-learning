# Problem set 4 - Guessing game

import random

while True:
    try:
        n = int(input("Level: "))

        if n > 0:

            x = random.randint(1,n)
        
            while True:
                guess = int(input("Guess: "))
                if guess > 0:
                    if guess < x:
                        print("To small!")
                    elif guess > x:
                        print("Too large!")
                    else:
                        print("Just right!")
                        raise SystemExit   
    except ValueError:
        pass