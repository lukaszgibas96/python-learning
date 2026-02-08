# Problem set 5 - Re-requesting a vanity plates

def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if 2<= len(s) <=6 and s[0:2].isalpha() and s.isalnum():

         # Find first digit
        for i in range(len(s)):
           
            if s[i].isdigit():
                first_digit = i
                break

        if s[first_digit] != "0":
            end_numbers = s[first_digit:]
            return end_numbers.isdigit()  
        
    return False

if __name__ == "__main__":
    main()