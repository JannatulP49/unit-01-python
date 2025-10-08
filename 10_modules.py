import os
import sys

"""
Task 1 (os module):
Write a Python program that prints the current folder (working directory) using the os module.
"""
print()
print()
#Set a variable to to get the current working directory. 
working_directory = os.getcwd()
print(working_directory)
print()
print()
"""
Task 2 (os module):
Create a new directory called "test_folder" in the current directory.
Then print a list of all files and directories in the current directory.
"""
print()
print()
#Lists all the current directories and files
dlist = os.listdir()
#prints the list of files and directories
print(dlist)
print()
print()
"""
Task 3 (os module):
Write a program that checks if a directory called "data" exists in the current 
working directory. If it doesn't exist, create it. If it does exist, print 
"Directory already exists."
"""
print()
print()
#This code checks if the directory named data exists already.
if os.path.exists("data"):
    print("Directory already exists.")
#If it doesn't exists then this code creates a new directory.
else:
    os.mkdir("data")
print()
print()

"""
Task 4 (os.path module):
Write a program that checks if a file called "config.txt" exists in the current directory.
If it exists, print its path. If it doesn't exist, print "File not found."
"""
print()
print()
if os.path.isfile("config.text"):
    print(os.path.abspath("config.txt"))
else:
    print("File not found.")
print()
print()
"""
Task 5 (sys module):
Write a program that prints the Python version you are currently using.
"""
print()
print()
#This prints the version of python that is currently being used.
print(sys.version)
print()
print()
"""
Task 6 (sys module):
Write a program that prints the platform your Python interpreter is running on
(e.g., 'linux', 'win32', 'darwin'). The output should be user friendly names
"Linux", "Windows", "MacOS"
"""
print()
print()
#Get the name of the platforms operating system 
platform = sys.platform
#Check if the platform is with linux
if platform.startswith('linux'):
    print ("linux")
#Check if the platform is with windows
elif platform == 'win32':
    print('Windows')
#Check if the platform is with MacOS
elif platform == 'darwin':
    print('MacOS')
else: 
    print('Platform does not exits')
print()
print()