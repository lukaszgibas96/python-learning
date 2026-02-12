# Reading and Writing Files from shorts /.read  /.readlines /.write /.writelines

def main():
    with open("alice.txt", "r") as f:
        contents = f.readlines()

        chapter1 = contents[52:272]
        print(chapter1)
    with open("chapter1.txt", "w") as f:
        f.writelines(chapter1)
 




main()