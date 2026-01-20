# Problem Set 2 - Vanity Plates


# OK - min 2 letters at beginning
# OK - min2 max 6 characters
# OK - numbbers not in middle. must be at the end 
# OK - 0 cannot be first used number
# OK - no space, periods or punctuation marks

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

        # Check if first digit is not 0
        if s[first_digit] != "0":
            end_name = s.split(s[first_digit])   
        else:
            return False 
        # Check if numbers are at the end
        return end_name[1].isdigit()
    
main()