import random

file_path = "./data/random.txt"

counter = int(input("Please enter the number of random numbers: "))

with open(file_path,'w') as file:
   while counter > 0:
       number = random.randint(1, 500)
       file.write(str(number)+"\n")
       counter-=1
