# Problem Set 2 - camelCase

def main():

    camelcase = input("camelCase: ")
    snakecase = convert(camelcase)
    print(f"snake_case: {snakecase}")


def convert(word):

    result = ""
    for char in word:
    
        if char.islower():
            result += char
        else:
            result += "_" + char.lower()
    return result
                       
        

main()