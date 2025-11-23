#2
# length1 = float(input("Enter the length of the rectangle 1: "))
# width1 = float(input("Enter the width of the rectangle 1: "))

# length2 = float(input("Enter the length of the rectangle 2: "))
# width2 = float(input("Enter the width of the rectangle 2: "))

# area1 = length1 * width1
# area2 = length2 * width2

# if area1 > area2:
#     print ("the rectangle 1 is greater")
# else:
#     print ("the rectangle 2 is greater")

#6
# month = int(input("Please enter the month: "))
# day = int(input("Please enter the day: "))
# year = int(input("Please enter the year (two last digits): "))

# magic_number = month * day

# if magic_number == year:
#     print("the date is magic")
# else:
#     print("the date is not magic")

#11
# number_of_books = int(input("Please enter the number of books: "))

# if number_of_books == 0:
#     print("you have 0 points")
# if number_of_books == 2:
#     print("you have 5 points")
# if number_of_books == 4:
#     print("you have 15 points")
# if number_of_books == 6:
#     print("you have 30 points")
# if number_of_books >= 8:
#     print("you have 60 points")

#12
# PRICE = 99
# number_of_packages = int(input("Please enter the number of the packages: "))
# discount = 0
# if number_of_packages > 10 and number_of_packages < 19:
#     discount = 10
# if number_of_packages > 20 and number_of_packages < 49:
#     discount = 20
# if number_of_packages > 50 and number_of_packages < 99:
#     discount = 10
# if number_of_packages >= 100:
#     discount = 40
# print("Discount is",discount,"%")
# print("The price is", number_of_packages*PRICE*discount/100)

#15
# year = int(input("Please enter the year: "))
# leap_year = False
# if year%400==0:
#     leap_year = True
# if year%4==0:
#     leap_year = True
# if leap_year==True:
#     print (f"in {year} February has 29 days. ")
# else:
#     print (f"in {year} February has 28 days. ")
