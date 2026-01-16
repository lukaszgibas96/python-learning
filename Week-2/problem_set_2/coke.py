# Problem Set 2 - Coke Machine 

def main():

    denomination = [5, 10, 25]

    due = 50
    print(f"Amount Due: {due} cents")

    while due > 0:

        coin = int(input("Insert Coin: "))
        if coin in denomination:
            due = due - coin

        print(f"Amount Due: {due}")
    
    print(f"Change Owed: {abs(due)}")
    
main()