def my_min(numbers):
    min = numbers[0]
    for i in numbers[1:]:
        if min > i:
            min = i
    return min


numbers = [-13, 3, 6, 2, 3]

print(my_min(numbers))
