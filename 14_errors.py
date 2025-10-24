"""
Identify the potential errors in the following code snippets and modify 
them to include appropriate try/except blocks to handle exceptions gracefully.
"""


"""
Example 1: Division
"""
print()
def divide_numbers(num1, num2):
    #This tries the code
    try:
      result = num1 / num2
      print("Result:", result)
    #This prevents the user from dividing a number by zero
    except ZeroDivisionError:
      print('You cannot divide by zero.')

# Example usage:
divide_numbers(10, 0)
print()
print()
"""
Example 2: Opening Files
"""

def read_file(filename):
    #This tries the code
    try:
      file = open(filename, 'r')
      contents = file.read()
      print("File contents:", contents)
    #This communicates to the user that the file wasnt created   
    except FileNotFoundError:
       print('The File doesnt exist.')
       #This closes the previous files
       try:
          file.close()
        #This is for if the file was never actually created then it would do nothing
       except UnboundLocalError:
          pass

# Example usage:
read_file("nonexistent.txt")
print()
print()
"""
Example 3: List Items
"""

def get_item(lst, index):
    #This tries the code
    try:
      item = lst[index]
      print("Item:", item)
      #This tells the user that the index is out of the exixting range
    except IndexError:
       print('The input isnt in the lists range.')

# Example usage:
my_list = [1, 2, 3]
get_item(my_list, 5)
print()
print()

"""
Example 4: Dictionaries
"""

def get_value(dictionary, key):
    #This tries the code
    try:
      value = dictionary[key]
      print("Value:", value)
      #This tells the user that the key that they are looking for is not in the dictionary
    except KeyError:
      print('That key is not in the dictionary')

# Example usage:
my_dict = {"a": 1, "b": 2}
get_value(my_dict, "c")
print()
print()

"""
Example 5: Else/Finally
Modify the following code to include an else block to execute code if no exceptions occur 
and a finally block to ensure that a certain action is always performed, regardless of whether an exception is raised.
"""
def process_file(filename):
    #This tries the code
    try:
        with open(filename, 'r') as file:
            contents = file.read()
            print("File contents:", contents)
            #This tells the user that the file doesnt exist
    except FileNotFoundError:
        print("Error: File not found.")
        #If the file does exist then it tells you the contents of the list
    else:
       print("File contents:", contents)
       #This tells the user if the code was successfully found the file
    finally:
       ('File is found')

# Example usage:
process_file("example.txt")
print()
print()