def main():

    size = get_size()
    tree_print(size)

def get_size():

    while True:
        n = int(input("What's size of the tree?"))
        if n > 0:
            return n
        print("The size value has to be possitive")
        

def tree_print(x):

    for i in range(1, x+1):
        print(int((x-i)/2) * " ", i * "#")


main()
            
            

