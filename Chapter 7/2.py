list = []
for i in range(0,20):
    number = int(input("Please enter the number: "))
    list.append(number)

print(list)
print(min(list))
print(max(list))
print(sum(list))
print(sum(list)/len(list))