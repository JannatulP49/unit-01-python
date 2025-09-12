"""
TASK 1:
Create a float variable, and then convert it to an integer
Print both the original variable and the converted integer.

"""
#converted 8.25 to 8 
my_float= 8.25
my_convert=int(my_float)
print (my_float)
print (my_convert)


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
my_integer = int(input("Integer: "))
my_float = float(input("Float: "))

add = my_integer + my_float
subtract= my_integer - my_float
multiply= my_integer * my_float
divide= my_integer / my_float

print(add)
print(subtract)
print(multiply)
print(multiply)





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
my_string = "1,3,5,7,9"

my_list = my_string.split(",")
my_tuple = tuple(my_list)
print(my_string)
print(my_list)
print(my_tuple)

"""
TASK 6:

Create a list of your favorite subjects (as strings). 
Use the join() function to combine all subjects into a single string separated by commas.
Then create another version using " - " as the separator.
Print both the original list and both joined strings.
"""

fav_subj=["ELA, Math, Science, History"]
my_comma= ", " .join(fav_subj)
my_dash= "- " .join(fav_subj)

print(fav_subj)
print(my_comma)
print(my_dash)
