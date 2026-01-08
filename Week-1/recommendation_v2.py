# Implement boolean expressions             / if not / or / and

def main():

    difficulty = input("Difficult or Casual? ")

    if not (difficulty == "Difficult" or difficulty == "Casual"):
        print(" Input valid difficulty")
        return
        
    players = input("Multiplayer or Single-player? ")

    if not (players == "Multiplayer" or players == "Single-player"):
        print("Input valid number of players")
        return

    if difficulty == "Difficult" and players == "Multiplayer":
            recommend("Poker")
    elif difficulty == "Difficult" and players == "Single-player":
            recommend("Klondkie")
    elif difficulty == "Casual" and players == "Multiplayer":
            recommend("Hearts")
    else:
            recommend("Clock")
        

def recommend(game):
    print(f"You might like {game}")

main()
