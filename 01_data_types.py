"""
TASK 1:
Create a float variable, and then convert it to an integer
Print both the original variable and the converted integer.

"""
#converted 8.25 to 8 
float = 8.25
convert=int(float)
print (float)
print (convert)


"""
TASK 2:
Write code that takes a number as input and prints whether 
it's positive, negative, or zero using if-elif-else statements.
"""
#code takes number and depicts whether its positive of negative or zero.
number = int(input("Number:"))
if number > 0:
  print ("Number is positive")
elif number < 0:
   print ("Number is negtive")
else: 
   print ("Number is zero")


"""
TASK 3:

Write code that takes two numbers as input (an integer and a float), 
performs addition, subtraction, multiplication, and division, and prints the results.
"""
integer = int(input("Integer: "))
float = float(input("Float: "))

add = integer + float
subtract= integer - float
multiply= integer * float
divide= integer / float






"""
TASK 4:

Create a dictionary with keys as fruit names and values as their respective quantities. 
Then print out the quantity of one of the fruits.
"""
#made a dictionary of fruits and printed the quantity of dragonfruits
fruitquantity = {
   "banana": 4,
   "dragonfruit": 12,
   "mango": 3

}
print(fruitquantity["dragonfruit"])

"""
TASK 5:

Create a string variable with that is a list of numbers and convert that string into a tuple.
Then print out the both the original string and tuple.
"""
string = "1,3,5,7,9"

tuple = tuple(int())
"""
TASK 6:

Create a list of your favorite subjects (as strings). 
Use the join() function to combine all subjects into a single string separated by commas.
Then create another version using " - " as the separator.
Print both the original list and both joined strings.
"""