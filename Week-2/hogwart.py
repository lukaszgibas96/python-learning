students = [
    {"name" : "Hermione", "house" : "Gryfindor", "patronus" : "Otter"},
    {"name" : "Harry", "house" : "Gryfindor", "patronus" : "Stag"},
    {"name" : "Ron", "house" : "Gryfindor", "patronus" : "Jack Russell terrier"},
    {"name" : "Draco", "house" : "Slytherin", "patronus" : None}
    ]

for student in students:
    print(student["name"], student["house"], student["patronus"], sep = ", ")