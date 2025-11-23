file_path = "./data/numbers.txt"

total = 0
number = 0

with open(file_path,'r') as file:
    for line in file:
        number = int(line)
        total += number
        print(line.rstrip())
    print(total)
