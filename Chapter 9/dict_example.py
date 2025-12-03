c = {
    "CH": "Bern",
    "FR": "Paris",
    "DE": "Berlin",
    "IT": "Rome"
}

c["CH"] = "Zurich"
c["UK"] = "London"

del c["FR"]

print(c["CH"])
print("UK" in c)
print(len(c))

for key in c:
    print(key)

print(c.get("UA")) #get value

for k,v in c.items():
    print(f"{k} = {v}")

print(c.values())
print(c.keys())
