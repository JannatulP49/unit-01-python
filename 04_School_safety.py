#I created the inputs asking for student information!
Grade= int(input("What grade are you in: "))
Student= int(input("How many students are there: "))
Minutes= int(input("How many minutes until lunch ends: "))
Money= input('Do you have lunch money "yes" or "no":' )
Free=input('Are you on the free lunch list "yes" or "no": ')

#Created an if statement to check that if there are 30 or more studnents for priority
if Student > 30:
   #This is a nest if statement so if there are more than 30 students and they are in 6,7,8 grades they get priority if not they dont
  if Grade == 6 or Grade == 7 or Grade == 8:  
     print("You get priority ")
  else:
     print('You dont get priority')   
     #I there is not more than 30 people than there are not enough students for priority
else:
   print('There are not enough students to get priority!')   
    #If a student has either lunch money or on the list they can get lunch if not then they cant have lunch
if Money == "yes" or Free == "yes":
   print('You can get lunch because you have money!')
else:
   print('Sorry you need either lunch momey or be on the free lunch list! ')

#If there are more then 25 students then there must be 15 or more minutes left to feed the kids if not then they cant get lunch
if Student > 25:
   if Minutes >= 15:
    print ('Great there is enough time to get your lunch!')
   else:
      print('Sorry, there isnt enough time to get lunch')


   
