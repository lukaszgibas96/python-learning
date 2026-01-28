# random                            /random.choice()        /random.choices()       /random.sample()    /random.seed()
import random

cards = ["jack", "king", "queen"]


def main():
    #random.seed(0)
    print(random.choices(cards, weights = [75, 20 , 5], k=2))



main()