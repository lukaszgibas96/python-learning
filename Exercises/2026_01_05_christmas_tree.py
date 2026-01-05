def main():

    size = get_size()
    tree_print(size)

def get_size():
    n=int(input("What's size of the tree?"))

    while True:

        if n >0:
            return n
        else:
            print("The size value has to be possitive")
            n = abs(n)
            print(f"The correct value of the tree' size is {n}")

def tree_print(x):

    for i in range(x):
        print(int((x-i)/2) * " ", i * "#")


main()
            
            

