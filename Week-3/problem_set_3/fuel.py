# Problem set 3 - Fuel Gauge


def main():
    while True:

        try:
            x, y = map(int,input("Fraction: ").split("/"))
            if x<=y and x >= 0 and y > 0:
                get_level(x,y)
                break

        except (ValueError, ZeroDivisionError):
            pass
       

        

def get_level(x,y):
    percentage = round(x/y*100)
    if percentage <= 1:
        print("E")
    elif percentage >= 99:
        print("F")
    else:
        print(f"{percentage}%")

main()

