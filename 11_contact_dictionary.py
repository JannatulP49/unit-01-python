#This creates an empty dictionary
my_dict = {}
#This lists the the various options and repeats over in a while loop
while True:
 print()
 print("1. Add Contact")
 print()
 print("2. Delete Contact")
 print()
 print("3. List Contacts")
 print()
 print("4. Exit")
 print()
#This allows you to input any choice 
 choice1 = input("Pick a choice (1-4)")
#If its to add you can add your contact name and number
 if choice1 == '1':
  name = input('Name: ')
  phone = input('Phone Number: ')
  my_dict[name] = phone
#If its to delete then you name a contacts that is already in the dictionary and deletes it.
 elif choice1 == '2':
  name = input('Name: ')
  if name in my_dict:
   del my_dict[name]
   print(my_dict)
#If its to list your contacts it uses a for loop to and then prints the contacts in the form of name : phone so it looks presentable.
 elif choice1 == '3':
  print()
  print('MY CONTACT LIST: ')
  for x in my_dict:
   print(x, ":", my_dict[x])
#If its to exit your program then this would break your code. 
 elif choice1 == '4':
  print()
  print('Exited!')
  break 
 