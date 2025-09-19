print()
print()
#Printed a welcome statemnet for the user
print("Welcome To The Calculatinator-inator 9000")
print()
print()
#User to input two numbers for my variable
num1= float(input('Enter the first number: '))
num2= float(input('Enter the second number: '))
print()
#Set the operation choices
print('Select Operation:')
print()
print('1. Addition')
print('2. Subtraction')
print('3. Multiplication')
print('4. Division')
print('5. Floor Division')
print('6. Exponential')
print('7. Remainder')  
print()
#Allow them to choose the operation
operation= input('Enter choice: ')
#Depending on the operation chosen the math would be applied 
if operation == '1':
    print('Result:', num1 + num2)
elif operation == '2':
    print('Result:',num1 - num2)
elif operation == '3':
    print('Result:',num1 * num2)
elif operation == '4':
    #If number 2 is zero it would be undefined and the calculation would not work
    if num2 == 0:
        print('Can not calculate with that number!')
    else:
        print('Result:',num1 / num2)
elif operation == '5':
    print('Result:',num1 // num2)
elif operation == '6':
    print('Result:',num1 ** num2)
elif  operation == '7':
    print('Result:',num1 % num2)
#If user puts anything else it will be considered invaild
else: 
    print('That operation is invalid!')


