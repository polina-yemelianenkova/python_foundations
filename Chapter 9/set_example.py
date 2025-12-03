l = ["Phillip", "Phillip", "Devid", "Devid", "Rainer"]

s = set(l)

s.update(["Marta", "George"])
print(s)
print(len(s))

s1 = {"Phillip", "Devid", "Rainer"}
s2 = {"Claus", "Marta", "Rainer"}

result = s1.union(s2)
print(result)

result = s1.intersection(s2)
print(result)