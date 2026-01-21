# Week 3 - Exceptions - Lecture v2             /try:   /except ValueError:  /else:

while True:
    try: 
        x = int(input("What's x?" ))
    except ValueError:
        print("x is not an integer") 
    else:
        break
print(f"x is {x}") 