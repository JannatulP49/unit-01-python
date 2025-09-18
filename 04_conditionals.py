'''
Exercise 1:
Check if an integer is greater than or equal to 10.
Return True, False otherwise.
'''
#I created a true or false to check if the number is greater or equal to 10
num1 = int(input('Number: '))
if num1 >= 10:
    print("True")
else:
    print("False")

print()
print()


'''
Exercise 2:
Determine the ticket price based on age and student status.
Price is $10 if under 18 or a student, $20 otherwise.
'''
#I created a code that gives students and ages under 18 10 dollar tickets and the rest 20 dollar tickets
Student= (input("Are you a student?(ans: yes or no)"))
Age= int(input("Enter your age:"))

if Age < 18 or Student == "yes": 
    print("Tickets price is 10 dollars")
else:
    print("Tickets price is 20 dollars")

print()
print()
'''
Exercise 3:
Prompt the user to enter a fruit name. Check if the fruit is in the list. 
If it is, print "Yes, that fruit is in the list." 
If it's not, print "No, that fruit is not in the list."
'''
#Created a list of fruits and had the user check if their selected fruit is in the list.
fruits=["peach", 'grapes', 'cherry', 'pineapple']
fruit1= input('Choose a fruit:')
if fruit1 in fruits:
    print("Yes that fruit is in the list.")
else:
    print("No that fruit is not on the list.")
print()
print()

'''
Exercise 5:
Calculate the cost of shipping for an online order based on the order weight and destination zone. 
The shipping cost is $5 per kilogram for Zone A and $7 per kilogram for Zone B. 
If the order weight is less than 0 kg, return an error message.
'''
#Checked if the persons weight is in zone a or b and then added 5 or 7 dollars depending on the zone.
weight = int(input("What is the order weight: "))
Zone= input("Is your destination zone A or B: ")
if weight < 0:
    print('Error!')

elif Zone == "A" or Zone == "Zone A":
    price1 = weight * 5
    print("The shipping cost:", price1 )
elif Zone == "B" or Zone == "Zone B":
    price2 = weight * 7
    print("The shipping cost:", price2 )

print()
print()

'''
Exercise 6:
Determine the type of a triangle based on side lengths.
Equilateral, Isosceles, Scalene, or Not a triangle.
'''
#Determined based on the side lengths if the triangle is Equilateral, isoceles, scalene, or not a triangle.
Side1=8
Side2=6
Side3=8

if Side1 == Side2 == Side3 :
   print('Equilateral triangle')
elif Side1==Side2 or Side2==Side3 or Side3==Side1:
   print("Isocelese Triangle")
elif Side1!=Side2 or Side2!=Side3 or Side3!=Side1:
   print('Scaline Triange')
else:
   print("Not A Triangle")
print()
print()