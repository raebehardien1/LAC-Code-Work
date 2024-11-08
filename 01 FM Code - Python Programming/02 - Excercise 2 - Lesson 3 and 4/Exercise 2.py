# TODO: Ask the user to input a test score (0-100) and store it in a variable called 'score'
# Question 1: Arithmetic and Assignment Operators
x=2 
y=10
# TODO: Add 3 to x using the += operator
x += 3

# TODO: Multiply y by 2 using the *= operator
y*=2
# TODO: Divide x by y and store the result in a variable called 'result'
result=x / y 
# TODO: Print the value of 'result'
print("result :",result)

#------------------------------------------------------------------------------------
# Question 2: Comparison and Logical Operators

# TODO: Create a condition that checks if a is greater than b
a = 200
b = 100
c = 50
 
if a > b:
  print("a is greater than b")
elif a ==b:
    print('a is equal to b')
else:
    print('a is less than b')
# TODO: Create a condition that checks if b is even (hint: use the modulus operator)
b = 10

if b % 100 == 0 : 
  print('b is even')
else:
  print('b is odd')

# TODO:  Create a condition that checks if c is less than or equal to a
a = 100
c = 150

if c < a  :
   print("c is less than a")

elif c == a : 
   print ("c is equal than a ")

else:
   print ("c is equal to a")

# TODO: Combine the above conditions using logical operators to create a 'final_condition'
#       The 'final_condition' should be True if either:
#       - a is greater than b, or
#       - b is even and c is less than or equal to a
 
a=10
b=8
c=7

final_condition = (a > b) or (b % 2 == 0 and c <= a)

# Print the result of final_condition
print(f"Final condition is: {final_condition}")
   

#------------------------------------------------------------------------------------
# Question 3: Conditional Statements

# TODO: Ask the user to input a test score (0-100) and stor it in a variable called 'score'
score= int(input("Enter you test score between 0-100: "))
# TODO: Implement a grading system using if-elif-else statements:
#       90-100: A
#       80-89: B
#       70-79: C
#       60-69: D
#       Below 60: F
score
if 90 <= score <= 100:
 grade = 'A'
elif 80 <= score < 90:
  grade = 'B'
elif 70 <= score < 80:
    grade = 'C'
elif 60 <= score < 70:
    grade = 'D'
elif 0 <= score < 60: 
    grade = 'F'
else:
    grade = 'Invalid score' 
# TODO: Print the grade for the given score
print=("The grade for the score" + grade )
#------------------------------------------------------------------------------------
# Question 4: Combining Operators and Conditionals

# TODO: Ask the user to input two numbers and store them in variables 'num1' and 'num2'
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# TODO: Ask the user to input an operation (+, -, *, /) and store it in a variable called 'operation'
operation = input ("Enter an operation (- , + , * , / ) : ")
# TODO: Use conditional statements to perform the chosen operation on num1 and num2
if operation == "-" :
    result == num1 - num2
if operation == "+" :
    result == num1 + num2
if operation == "*" :
    result == num1*num2
if operation == "/" :
   result = num1/num2
# TODO: Handle the case of division by zero

# TODO: Print the result of the operation
print(f"The result of {num1} {operation} {num2} is: {result}")
