from datetime import date
from datetime import datetime
"""
Exercise 1:
Write a Python program that prints the current date and time using the datetime module.
"""
#This prints the date and time at the present momment.
my_dt = datetime.now()
print(my_dt)

"""
Exercise 2:
Write a Python program that prints the current date and time using the datetime module.
Using the strftime function format the date in standard U.S. date format (MM/DD/YYYY)
"""
print()
print()
#This prints the date of today
my_time = date.today()
#This prints the day in the format of month, day, and year
my_string = my_time.strftime("%m/%d/%Y")
print(my_string)




"""
Exercise 3:
Using the strptime function, convert two strings into dates.
Then find the difference in days between the two.
"""
print()
print()
#This formats the string into your first date 
my_string1 = "10/14/2025"
my_date1 = datetime.strptime(my_string1, "%m/%d/%Y")
print(my_date1)
#This formats the string into your second date 
my_string2 = "04/02/2014"
my_date2 = datetime.strptime(my_string2, "%m/%d/%Y")
print(my_date2)
#This subtracts the two dates and then gives you the difference in days
difference = my_date1 - my_date2
print(difference)

"""
Excercise 4:
Write a program that asks the user for their birthdate and calculates their current 
age using the datetime module.
"""
#This asks the user for its brithday in a specific format
birthday = input("Enter Your Birthdate (write it Month/Date/Year): ")
#This formats the string in the correct way 
birth_date = datetime.strptime(birthday, "%m/%d/%Y")
#This prints the time and day now
today = datetime.now()
#This subtacts the date you inputed and todays date to calculate your age in years.
age = today.year - birth_date.year
print("You are", age)

