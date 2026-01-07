def main():

    difficulty = input("Difficult or Casual? ")
    players = input("Multiplayer or Single-player? ")

    if difficulty == "Difficult":

        if players == "Multiplayer":
            recommend("Poker")
        elif players == "Single-player":
            recommend("Klondkie")
        else:
            print("Input valid number of players")

    elif difficulty == "Casual":

        if players == "Multiplayer":
            recommend("Hearts")
        elif players == "Single-player":
            recommend("Clock")
        else:
            print("Input valid number of players")

    else:
        print(" Input valid difficulty")

def recommend(game):
    print(f"You might like {game}")

main()
