"""
Task 1: Greeting
Write a function that takes a name as a 
agrument and prints a greeting message like "Hello, [name]!".
"""

"""
This functions job is to print a greeting to the person whose name is given.

"""
print()
def my_function(name):   
    print("Hello" + " " + name)
    #This combines the word hello and space and the persons name to be printed together into a sentence.
my_function("Kathy")
#This runs the function replacing name with kathy.
print()
print()

"""
Task 2: Square of a Number
Write a function that takes an integer as an argument and returns its square.
"""
"""
This function takes a number and returns the squared result.
"""
def sqr_num (a):
    return a ** 2
#This multiplies the inputted number by itself to find the square.
print(sqr_num(8))
#This prints the result of the given number squared.
print()
print()

"""
Task 3: Even or Odd
Write a function that takes a number as a argument that 
returns `True` if the number is even, and `False` otherwise.
"""
"""
This function checks if a number is even or odd and returns even if the number is even and odd if its odd.
"""
def even_or_odd(num):
    if num % 2 == 0:
        #This checks if the remainder of the number divided by 2 is 0 because if it is then its even.
        return "Even"
    else:
        #If the remainder is not 0 then it prints Odd.
        return "Odd"
print(even_or_odd(5))
#This prints whether 5 is an odd or even number.
print()
print()

"""
Task 4: Area of a Rectangle
Write a function that takes the length and width of a rectangle and returns its area.
"""
"""
This function finds the area of a rectangle by taking the length and the width and giving the product.
"""
def area(num1, num2):
    return num1 * num2
#This multiplies the length and width to get the area of the rectangle.
print(area(8, 5))
#This prints the product of 8 and 5 and gives you the area of 40.
print()
print()

"""
Task 5: Celsius to Fahrenheit
Write a function that takes a temperature in Celsius and returns 
the equivalent temperature in Fahrenheit using the correct formula
"""
"""
This function changes temperature from celsius to fahrenheit.
"""
def cel(num1):
    return num1 * 2 + 30
# This used the conversion formula to convert the Celsius to Fahrenheit.
print(cel(10))
#This does the conversion from 10 degrees to 40 degrees.
print()
print()

"""
Task 6: Average of Numbers
Write a function that takes a list of numbers as an argument
and returns the average (mean) of those numbers.
"""
"""
This function finds the average of a list of numbers.
"""
def average(num):
    return sum(num) / len(num)
#This adds all numbers and divides by how many there are.
    
print(average([1,2,3,10]))
#This prints the average of all the numbers in the list.
print()
print()

"""
Task 7: Total Calculator
Create a function that has arguments for the price and quantity of something, 
and returns the total.

Your function should also optionally accept a 3rd argument for discount as a float, 
and return the discounted if provided.
"""

"""
This function calculates the total cost based on price and quantity and if a discount is added then it would subtract from the total price.
"""

def total_cal( price, quantity, discount= 0.0):
    subtotal = price * quantity
    #This finds the total before there is any discount added.
    return subtotal - (subtotal * discount)
#This subtracts the discounted amount from the total.
print (total_cal(3,4))
    
    
    
