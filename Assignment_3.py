# Task 1: Calculate Factorial Using a Function
'''
n = int(input("Enter a number: ")) # take input from user
def factorial(n):
    if n < 2:
        return 1
    else:
        fac = n*(factorial(n-1))
        return fac

result = factorial(5)
print("Factorial of {} is: {}".format(n,result)) # use string formating
'''


#  Task 2: Using the Math Module for Calculations
import math
n = int(input("Enter a number: "))
square_root = math.sqrt(n)
logarithm = math.log(n)
angle_radians = math.radians(n)
sine_value = math.sin(angle_radians)
print("Square root: {}\nLogarithm: {}\nSine: {} ".format(square_root,logarithm,sine_value))
