# Problem set 5 - refueling

def main():
    fraction = input("Fraction: ")
    percentage = convert(fraction)
    level = gauge(percentage)
    print(level)

        
       
def convert(fraction):
    while True:
        try:

            x, y = map(int,fraction.split("/"))
            if x<=y and x >= 0 and y > 0:
                percentage = round(x/y*100)
                return percentage

        except (ValueError, ZeroDivisionError):
            pass

    

def gauge(percentage):
    
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage}%"

if __name__ == "__main__":
    main()

