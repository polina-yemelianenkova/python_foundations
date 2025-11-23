#2
# calories_per_minute = 4.2
# for num in [10,15,20,25,30]:
#     print(num*calories_per_minute)

#3
budget = int(input("Please put the budget: "))
total_expence = 0
n=1
while n<6:
    expence = int(input(f"expense {n}:"))
    n += 1
    total_expence += expence
result = budget - total_expence
if result >= 0:
    print(f"Your expenses are under budget: {result}")
if result < 0:
    print(f"Your expenses are over budget: {result}")

#4
# speed = int(input("Please put the speed: "))
# time = int(input("Please put the hours traveled: "))
# distance = 0
# num = 1
# while num<=time:
#     print(num,"    ", num*speed)
#     num += 1

#4
# num = 10
# print("km       miles")
# while num <=80:
#     print (num, "     ", num * 0.62)
#     num += 10

#8
# num = 1
# summ = 0
# while num > 0:
#     num = int(input("enter the number: "))
#     if num < 0:
#         break
#     summ += num
# print(summ)



