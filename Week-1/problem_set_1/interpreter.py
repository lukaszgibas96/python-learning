# Problem Set 1 - Math Interpreter

elements = (input("Expression: ")).split(" ")

print(elements)

x = float(elements[0])
z = float(elements[2])

if  elements[1] == "-" :
    result = x - z 

elif elements[1] == "+" :
    result = x + z 

elif elements[1] == "*" :
    result = x * z 

elif elements [1] == "/" :
    result = x / z
else:
    print("Wrong mathematical operator")
    exit()


print(f"{result:.1f}")

