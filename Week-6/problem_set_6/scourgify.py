# Problem Set 6 - Scourgify
import sys
import csv


def main():
    try:
        check_command()

        file_name = sys.argv[1]
        new_file_name = sys.argv[2]

        check_extension(file_name)
        check_extension(new_file_name)

        with open(file_name, "r") as before_file, open(new_file_name, "w") as after_file:
            reader = csv.DictReader(before_file)
            writer = csv.DictWriter(after_file, fieldnames = ["first", "last" , "house"])
            writer.writeheader()
            for row in reader:
                last, first = row["name"].split(",")
                writer.writerow({"first": first.strip(), 
                                 "last": last.strip(), 
                                 "house": row["house"]
                                 })         

    except FileNotFoundError:
        sys.exit("File does not exist")



def check_command():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) == 3:
        return
    else:
        sys.exit("Too many command-line arguments")
        
def check_extension(name):
    
    if name.endswith(".csv"):
        return 
    else:
        sys.exit(f"Could not read {name}")

if __name__ == "__main__":
    main()


