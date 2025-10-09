import random

"""
Task 1 (random module):
Write a program that simulates rolling a six-sided die 10 times.
Print each roll result.
"""
#This code allows you to do th following code 10 times.
for i in range(10):
    #This tells the dice to pick a random number between 1 and 6
    dice= random.randint(1,6)
    print (dice)
    print()
    print()

"""
Task 2 (random module):
Write a program that generates 5 random floating-point numbers between 0 and 1.
Then generate 5 random floating-point numbers between 10 and 20.
Print both sets of numbers.
"""
#This created a list with five random decimals between 0.0 and 1.0
random1 = [random.uniform(0.0, 1.0) for x in range(5)]
print(random1)
#This created a list with five random decimals between 10.0 and 20.0
random2= [random.uniform(10.0, 20.0) for x in range(5)]
print(random2)
print()
print()

"""
Task 3 (random module):
Create a list of colors: ["red", "blue", "green", "yellow", "purple"].
Write a program that randomly selects and prints 3 colors from this list without replacement.
"""
#This list the various colors
colors= ['red', 'orange', 'yellow', 'green', 'blue']
#This picks three random colors from the list 
colurs = random.sample(colors, 3)
print(colurs)
print()
print()
"""
Task 4 (random module):
Write a program that creates a list of numbers from 1 to 10, then shuffles the list
and prints the shuffled result.
"""
#This list the numbers from 1 to 10
numbers = list(range(1,11))
#This shuffles the numbers into a random order
random.shuffle(numbers)
#This prints the shuffled list 
print(numbers)
print()
print()
