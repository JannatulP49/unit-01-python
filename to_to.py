#I created an empty list
print("YOUR TO-DO LIST")
print()
my_list= []

#made sure the condition of the loop is always true
while True:
    #printed the empty list 
    
    print
#allow the user to choose whether they want to add or remove something
    addrem = input("Would you like to add or remove something: ")
    print()
#made it so that if its add then they could add a new element to the list 
    if addrem == 'add':
        add= input("What would you like to add: ")
        print()
        my_list.append(add)
        for x in my_list:
            print(x)
#made it so that if its remove then they could remove an element to the list 
    elif addrem == 'remove':
         print()
#We ask them what number they want to remove and them subtract 1 since the user doesnt know it starts at 0.
         rem= int(input("What number you like to remove: "))
         del my_list[rem - 1]
 #Then I use the for loop to to list out the differnet things in the list.
         for x in my_list:
             print(x)
        


