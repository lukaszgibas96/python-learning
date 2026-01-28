# random                            /random.choice()        /random.choices()       /random.sample()
import random

cards = ["jack", "king", "queen"]


def main():

    print(random.choices(cards, weights = [75, 20 , 5], k=2))



main()