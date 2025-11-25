import random


def generate_lottery_number():
    list = []
    for number in range (7):
        number = random.randint(0,9)
        list.append(number)
    return list

def show_list():
    list = generate_lottery_number()
    for i in range(len(list)):
        print(list[i], end="")

show_list()


