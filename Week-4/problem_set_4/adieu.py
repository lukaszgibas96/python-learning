# Problem set 4 - Adieu, adieu

import inflect
p = inflect.engine()

names_list = []

while True:
    
    try:
        name = input("Name: ")
        names_list.append(name)


    except EOFError:
        print()
        names = p.join(names_list, conj = "and")
        print(f"Adieu, adieu {names}")
        break

    
