lecturers_py = ["Rainer", "Phillip", "Devid"]
lecturers_math = ["Martina", "Florian"]

lecturers = lecturers_py + lecturers_math

l = [e for e in lecturers if e.startswith("P")]
l = [len(e) for e in lecturers if e.startswith("P")]

print(sum(l)/len(l))