# Too complex program, we keep asking further questions
# even if a previous condition has already been met

x = int(input("What's x?"))
y = int(input("What's y?"))

if x > y:
    print("X is greater than y")

if x < y:
    print("x is less than y")

if x == y:
    print("x is equal to y")

#Simpler code, but we still keep checking for equality even if, 
#logically, the answer couldn't be different.

x = int(input("What's x?"))
y = int(input("What's y?"))

if x > y:
    print("X is greater than y")

elif x < y:
    print("x is less than y")

elif x == y:
    print("x is equal to y")

x = int(input("What's x\n?"))
y = int(input("What's y?\n"))

if x > y:
    print("X is greater than y")

elif x < y:
    print("x is less than y")

else:
    print("x is equal to y")