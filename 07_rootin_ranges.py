"""
Exercise 1:
Write a program to print numbers from 1 to 10 using a for loop.
"""
print()
print()
print()
#Created a loop that starts from 1 counts to 10 and exluding 11.
for x in range(1, 11):
    print(x)

"""
Exercise 2:
Write a program to count by 10s from 900 to 1000
"""
#Created a loop that starts from 900 and goes to 1000 counting by 10s until it reaches 1000.
print()
print()
for x in range(900, 1001, 10):
    print(x)

"""
Exercise 3:
Write a program that counts form 1-100 by 9
"""
#Created a loop that starts from one and goes to 100 but counting by 9s instead of 1s, it keeps printing until it reaches 100.
print()
print()
for x in range(1, 101, 9):
    print(x)


"""
Exercise 4:
Write a program to calculate the sum of all numbers from 1 to 10 using a for loop.
"""

#The loop starts at 0 or sum and it goes from 1 to 10 and adds the number to the sum and then prints the sum which is 55.

print()
print()
sum = 0
for x in range(1,11):
    sum += x
print(sum)



"""
Excercise 5:
Uncomment the following code and run it. Then answer the following:
- What is the ouput of the code?

- Explain the iterative process that this code executes to get that output
"""

# The program first created a loop that goes from 1 to 5 and which
# each row the next loop prints the stars and whatever number the 
# row is that is how many starts will be in that row and it keeps doing
# that process until they hit five rows and then the program ends.
print()
print()
rows = 5

for i in range(rows):
 for j in range(i + 1):
  print('*', end=' ')
 print()