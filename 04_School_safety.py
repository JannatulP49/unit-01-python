Grade= int(input("What grade are you in: "))
Student= int(input("How many students are there: "))
Minutes= int(input("How many minutes until lunch ends: "))
Money= input('Do you have lunch money "yes" or "no":' )
Free=input('Are you on the free lunch list "yes" or "no": ')

if Student > 30:
  if Grade == 6 or Grade == 7 or Grade == 8:  
     print("You get priority ")
  else:
     print('You dont get priority')    
else:
   print('There are not enough students to get priority!')   
    
if Money == "yes" or Free == "yes":
   print('You can get lunch because you have money!')
else:
   print('Sorry you need either lunch momey or be on the free lunch list! ')

if Student > 25:
   if Minutes >= 15:
    print ('Great there is enough time to get your lunch!')
   else:
      print('Sorry, there isnt enough time to get lunch')


   
