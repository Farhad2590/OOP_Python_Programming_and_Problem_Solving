"""
Write a python that takes a floating number from users using input() 
and outputs both Floor and Ceil of that number. 
"""
x=float(input("Enter a float value: "))

import math
y=math.ceil(x)
y1=math.floor(x)

print("The ceiling value of ",x," is", y)
print("The floor value of ",x," is", y1)

