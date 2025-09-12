"""
TASK 1:
Write code that checks if a user entered the correct password.
The password should not be case sensitive

"""
#created a enter pass input and made it not case sensitive 
enter_pass= input("Enter pass: ")
my_pass= "Prity16"

if enter_pass.upper() == my_pass.upper():
    print("Correct")
elif enter_pass.lower() == my_pass.lower():
    print("Correct")
print(enter_pass)

"""
TASK 2:
Write code that checks if a user inputs an empty string
If the string is empty, print "invalid" otherwise print "valid"
"""
#created an input for text if the text is empty it prints invalid and if its not empty it prints valid.
my_input = input("Text: ")

if my_input == "":
    print("invalid")
else:
    print("valid")


"""
TASK 3:

Write a program that will replace the word "cat" with the word "dog"
It should replace all occurances regardless of captilization 
"""
#made three varibles and replaced cats with dogs in the sentence 
a= "I like"
b= "cats"
c="dogs"

txt="{0} {1}".format(a,c)
print(txt)

"""
TASK 4:

Write a program that takes a person's name and age as input and prints it
"""
#made a code that asks for users name and age and then prints the information in a sentnece
my_name = input("Whats your name: ")
my_age = input("Whats your age: ")
print("Name:", my_name)
print("Age:", my_age)

"""
TASK 5:

Write a program that takes in two floats, and prints the quotient
The result should be rounded to the nearest tenth (1 decimal place)
"""

my_num1= float(input("Number 1:"))
my_num2= float(input("Number 2:"))

txt = f"Results: {my_num1: 2f}"
txt2= f"Results: {my_num2: 2f}"