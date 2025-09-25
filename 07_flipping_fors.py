"""
Exercise 1:
Write a program to print each character of a given string using a for loop.
"""
#Created a variable for my name and then made the loop print all the characters seperately.
name = "Jannatul Prity"
for char in name:
    print(char)

"""
Exercise 2:
Write a program to calculate the sum of elements in a list using a for loop.
"""
#Made a list of numbers and then created a variable to hold the result so it kept adding the next number on the list until all the numbers were added.
print()
print()
num = [1, 2, 3, 4 ]
sum = 0
for x in num:
    sum += x
    print(sum)

"""
Exercise 3:
Write a program to print the length of each word in a sentence using a for loop and a list.
"""
#Cretaed a sentence and then made the string sperated into a list with each word seperate. Then I made a loop that measured the length of each world in my list.
print()
print()


sentence= ["Hello people of the world"]
words = sentence[0].split()

for x in words:
    print(len(x))


"""
Excercise 4:
Write a program that creates a dictionary (atleast 4 key:value pairs) and then
iterates through a dictionary and prints the result



In a comment, answer the following, what do you notice about the output of your code?
Is it what you expected?
"""
#Created a dictionary and then a loop to print the keys and then the values which are labled as x together.
print()
print()
num = { 
"Num1": 20,                
"Num2": 30,
"Num3": 40,
"Num4": 50

}

for x in num:
    print(x)
    print(num[x])