def find_max(val1, val2, val3)->int:
   """
   Method which is finding the maximum
   Arguments are integers
   """
   largest = val1
   if val2 > largest:
      largest = val2
   if val3 > largest:
      largest = val3
   return largest


#Start program
print(find_max(4,3,9))