# problem set 5 - Testing my twttr

def main():
    
    inpt = input("Input: ")
    inpt_convert = input_unify(inpt)

    otpt = shorten(inpt_convert)
    print(f"Output: {otpt}")

def input_unify(s):
    return s.strip().lower()
    
  

def shorten(word):
    vowels = ["A","a","E","e","I","i","O","o","U","u"]
    otpt = []

    for char in word:
        if char not in vowels:
            otpt.append(char)

    otpt = "".join(otpt)
    return otpt

if __name__ == "__main__":
    main()


