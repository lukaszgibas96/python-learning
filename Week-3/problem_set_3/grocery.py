# Problem Set 3 - Grocery list

grocery = {}

while True:

    try:
        item = input("").strip().lower()
        
        if not item in grocery:
            grocery.update({item : 1})

        else:
            grocery[item] += 1

    except EOFError:

        new_list = sorted(grocery)
        for name in new_list:
            print(f"{grocery[name]} {name.upper()}")

        break
            
        


