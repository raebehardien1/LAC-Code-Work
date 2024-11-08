# Question 1: Using a for loop with a list

# TODO: Create a list of fruits
fruits = ["apple", "bannana", "kiwi", "strawberry"]

# TODO: Use a for loop to print each fruit in the list

for fruit in fruits:
    print(fruits)

#-------------------------------------------------------------------------
# Question 2: Using a while loop for countdown

# TODO: Use a while loop to create a countdown from 5 to 1
"""
count = 5
while count > 0:
   (print(count))
count -= 1
"""

#-------------------------------------------------------------------------
# Question 3: Using a for loop with range()

# TODO: Use a for loop to print the first 10 square numbers

# for number in range (1,10):
#   print (number)
#-------------------------------------------------------------------------

# Question 4: Using the random module

#TODO: Import the random module
import random

#TODO:  #Create a list of colors
random_colors = ("red" , "blue" , "orange" ,"black")

# TODO: Use a for loop to select and print 3 random colors from the list
#for x in range (3):

 #   print()
#pass
#-------------------------------------------------------------------------
# Question 5: Creating and using a custom module

# TODO: Create a new file named 'math_operations.py' with the following content:
# ""
# def add(a, b):
#     return a + b

# def subtract(a, b):
#     return a - b

# def multiply(a, b):
#     return a * b

# def divide(a, b):
#     if b != 0:
#         return a / b
#     else:
#         return "Error: Division by zero"
# ""
# TODO: Import the custom module and use its functions
import math_operation

print(math_operation.add(1, 2))



# TODO: Use a while loop to create a simple calculator
'''
def add(a, b):
    return a + b
def subtract(a, b):
    return a - b
def multiply(a, b):
    return a * b
def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: Division by zero"
'''
