students = [
    {"name": "Hermione", "house": "Gryffindor", "patronus": "Ptter"},
    {"name": "Harry", "house": "Gryffindor", "patronus": "stag"},
    {"name": "Draco", "house": "Slytherin", "patronus": None}
]

for student in students:
    print(student["name"], student["house"], student["patronus"], sep=", ")

