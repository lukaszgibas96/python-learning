name = input("What's your name? ").strip()

if "," in name:
    last, first = name.split(", ")
    name = f"{name} {last}"
 
print(f"hello, {name}")


