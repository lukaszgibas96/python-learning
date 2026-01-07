# Problem set 0 - making faces

def main():

    text = input()
    
    print(convert(text))

def convert(x):
       return x.replace(":)" , "🙂").replace(":(" , "🙁" )


main()