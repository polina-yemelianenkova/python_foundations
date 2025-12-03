def main():
    number_string = input("PLease enter a sequence of digits: ")
    total = string_total(number_string)
    print("Sum of the digits: ", string_total)
    

def string_total(string):
    total = 0
    number = 0
    for i in range(len(string)):
        number = int(string[i])
        total += number
    return total