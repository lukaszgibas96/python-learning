# Week 3 - Exceptions - Lecture             /try:   /except ValueError:

try: 
    x = int(input("What's x?" ))
except ValueError:
    print("x is not an integer") 
else:
    print(f"x is {x}") 