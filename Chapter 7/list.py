lecturers_py = ["Rainer", "Phillip", "Devid"]
lecturers_math = ["Martina", "Florian"]

lecturers = lecturers_py + lecturers_math

print("Bob" in lecturers)

lecturers.append("Bob")

print("Bob" in lecturers)

print(lecturers.count("Bob"))

lecturers.insert(0,"Bob")
lecturers.remove("Bob")
print(lecturers)

l = lecturers.copy()
l[0] = "Gabriel"
print(l)