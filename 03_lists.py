"""
Task 1: Create a list
Create a list with 4 elements and print it.
"""
print()
#I crated a list with four different animals.
my_list=["panda", "cats", "dogs", 'mouse']
print(my_list)
print()
print()
print()
"""
Task 2: Add Element to a List
Add an element to the end of the list. Print the updated 
list.
"""
#Created a list of animals and added a turtle to my list of animals.

my_list=["panda", "cats", "dogs", "mouse"]
my_list.append("turtle")
print(my_list)
print()
print()
print()

"""
Task 3: Remove Element from a List
Remove a specific element from the list. Print the 
updated list.
"""
#I removed a turtle from my list of animals.
my_list=["panda", "cats", "dogs", "mouse", "turtle"]
my_list.remove("turtle")
print(my_list)
print()
print()
print()

"""
Task 4: Modify Element in a List
Modify an element at a specific index with a new value. 
Print the updated list.
"""

#I modifided my panda element to a sloth.
my_list=["panda", "cats", "dogs", "mouse"]
my_list[0]="sloth"
print(my_list)
print()
print()
print()

"""
Task 5: Append Multiple Elements to a List
Append multiple elements to the end of the list. Print 
the updated list.
"""
#I added multiple new animals to my existing list.
my_list=["sloth", "cats", "dogs", "mouse"]
my_list.append("whale")
my_list.append("shark")
my_list.append("salmon")
print(my_list)
print()
print()
print()
"""
Task 6: Delete Element at a Specific Index
Delete an element at a specific index. Print the updated 
list.
"""
#I deleted mouse from the list of animals.
my_list=["sloth", "cats", "dogs", "mouse","whale", "shark", "salmon"]
del my_list[3]
print(my_list)
print()
print()
print()
"""
Task 7: Slicing lists
Create a new variable equal to the first 2 items of your list
Then print out the new variable
"""
#I got rid of all the animals except the first two items on my list.
my_list=["sloth", "cats", "dogs", "whale", "shark", "salmon"]
items= my_list[0:2]
print(items)
print()
print()
print()
"""
Task 8: Extend a List
Extend the list with the elements of another list. Print 
the updated list.
"""
#I created two lists and then proceeded to add the lists together.
my_list=["sloth", "cats"]
my_list2=["monkey", "fox", "wolf"]
lists_12= my_list + my_list2
print(lists_12)
print()
print()
print()
