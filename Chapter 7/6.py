import random

def dice():
    list = []
    number = int(input("Please enter the number of times: "))

    for i in range(number):
        number = random.randint(1,6)
        list.append(number)
    print(list)

dice()
    
    