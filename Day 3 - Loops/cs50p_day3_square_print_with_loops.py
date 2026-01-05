def main():

    square_size = int(input("What's a size? \n"))
    print_square(square_size)

def print_square(size):
    for i in range(size):
        for k in range(size):
            print("X ", end = "")
        print()


# 1st option

# def print_square(size):
#     for _ in range(size):
#         print("# " * size)



main()
