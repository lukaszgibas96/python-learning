# shorts - classes

class Package:

    def __init__(self, number, sender, recipient, weight):
        self.number = number
        self.sender = sender
        self.recipient = recipient
        self.weight = weight
         


def main():
    #insted of this: packages = ["Package 1: Alice to Bob, 10kg", "Package 2: Bob to Charlie, 5kg"]
    #do that:

    packages = [

        Package(number = 1, sender = "Alice", recipient = "Bob", weight = 10),
        Package(number = 2, sender = "Bob", recipient = "Charlie", weight = 5)
    ]
    for package in packages:
        print(f"Package {package.number}: {package.sender} to {package.recipient}, {package.weight}kg")

main() 