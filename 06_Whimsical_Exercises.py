"""
1. Simple Counter:
Write a program that uses a while loop to print numbers from 1 to 10.
"""
print()
print()
#Created a variable starting from 1. 
i=1
#Added a while statement to keep adding 1 to the variable until it hits 11.
while i < 11:
    print(i)
    i += 1

print()
print()


"""
2. Countdown:
Write a program that uses a while loop to print numbers from 10 to 1 in descending order.
"""
#Created a variable to start from 10
i = 10
#Created a while statement to keep subracting 1 until i hits 0.
while i > 0:
    print(i)
    i -= 1

print()
print()


"""
3. Factorial Calculation:
Write a program that calculates the factorial of a given number using a while loop.
"""
#Asked the user to input a number
num1= int(input('Give me a number: '))
#This will act as the result holder for the following process
i = 1 
#Created a loop to keep going until num1 is greater than zero
while num1 > 0:
    #This is the math for the factorial so it multiplies i with the number inputed by the user and gives a new value for i.
    i = num1 * i
    #This is to go down so if num1 is 3 then the next number to be multiplied would be 2 and so on and so on.  
    num1 -= 1
    #printed the result and goes back to repeat the process
print(i)
print()
print()

"""
4. Password Guessing Game:
Create a simple password guessing game using a while loop. Ask the user to guess a predefined password and provide appropriate feedback.
"""

#This is the password variable I set!
password = 'Prity16'
#I ask the user to guess the password
pas= input('Guess My Password: ')
#if theu dont get the password then it will tell them to guess again.
while pas != password : 
    print('No Guess Agian')
    #This will allow the user to input the password again!
    pas= input('Guess My Password: ')   
    #If they did get it correct then they got it!
else: 
    print('You Got It Great Job!')
print()
print()

"""
6. Fibonacci Series:
Write a program that prints the first n numbers in the Fibonacci sequence using a while loop.
"""