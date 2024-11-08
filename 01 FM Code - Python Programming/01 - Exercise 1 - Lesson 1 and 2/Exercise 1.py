# Question 1: Variable Assignment and String Manipulation

# TODO: Ask the user for their name and store it in a variable
name = input("What is your name? ")
print= "name"
# TODO: Ask the user for their age and store it in a variable
age = input("What is your age? ")
# TODO: Print a greeting using the name and age variables
print=("Hello,"+ name+ "You are"+age+" years old.")
print=("Hello,"+ (name)+ "You are"+(age)+" years old.")

#------------------------------------------------------------------------------------

# Question 2: Integer Operations

# TODO: Ask the user for the length of a rectangle and store it as an integer
length=int (input("What is the length of a rectangle? "))
# TODO: Ask the user for the width of a rectangle and store it as an integer

width=input(("What is the width of a rectangle?: "))
# TODO: Calculate area
area=int(length*width)

# TODO: Print the result
print("The area of the rectangle is:", area)
#------------------------------------------------------------------------------------
# Question 3: Working with Floats

# TODO: Ask the user for a temperature in Celsius and store it as a float
celsius = float(input("Enter the temperature in Celsius: "))

# TODO: Convert the temperature to Fahrenheit using the formula: (C * 9/5) + 32
fahrenheit = (celsius * 9/5) + 32
# TODO: Print the result rounded to two decimal places
print("The temperature in Fahrenheit is: " + str(round(fahrenheit, 2)))