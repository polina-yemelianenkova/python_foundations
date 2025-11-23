def main():
   val1 = int(input("Please enter the first number: "))
   val2 = int(input("Please enter the second number: "))
   print(f"The max number is: {max(val1, val2)}")

def max(val1, val2):
   """
   Method which is finding the maximum
   Arguments are integers
   """
   largest = val1
   if val2 > largest:
      largest = val2
   return largest

#Start program
main()