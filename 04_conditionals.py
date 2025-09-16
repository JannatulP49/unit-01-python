'''
Exercise 1:
Check if an integer is greater than or equal to 10.
Return True, False otherwise.
'''

num: int(input('Number:'))
if num >= 10:
    print(True)
else:
    print(False)

print()



'''
Exercise 2:
Determine the ticket price based on age and student status.
Price is $10 if under 18 or a student, $20 otherwise.
'''
Student= (input("Are you a student?(ans: yes or no)"))
Age= int(input("Enter your age:"))

if Age < 18 or Student == "yes": 
    print("Tickets price is 10 dollars")
else:
    print("Tickets price is 20 dollars")


'''
Exercise 3:
Prompt the user to enter a fruit name. Check if the fruit is in the list. 
If it is, print "Yes, that fruit is in the list." 
If it's not, print "No, that fruit is not in the list."
'''

fruits=["peach", 'grapes', 'cherry', 'pineapple']
fruit1= input('Choose a fruit:')
if fruit1 in fruits:
    print("Yes that fruit is in the list.")
else:
    print("No that fruit is not on the list.")


'''
Exercise 5:
Calculate the cost of shipping for an online order based on the order weight and destination zone. 
The shipping cost is $5 per kilogram for Zone A and $7 per kilogram for Zone B. 
If the order weight is less than 0 kg, return an error message.
'''

weight = int(input("What is the order weight: "))
Zone= input("Is your destination zone A or B: ")

if weight < 0:
    print('Error!')
elif Zone == "A":
    price = weight*5
    print("the shipping cost ")


'''
Exercise 6:
Determine the type of a triangle based on side lengths.
Equilateral, Isosceles, Scalene, or Not a triangle.
'''