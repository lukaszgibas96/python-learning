score = int(input("What's a score?\n"))

if 90 <= score:
    print("Grade A")
elif 80 <= score:
    print("Grade B")
elif 70 <= score:
    print("Grade C")
elif 60 <= score:
    print("Grade D")
else:
    print("Grade F")