"""
Task 1: People Class
Define a class called Person with attributes name and age.
Then, write a method within the class to introduce the person with their name and age.

Create a new object using this new class, and call the method you created.
"""
print()
print()
#You create a class called person
class Person:
    #You add your objcets name and age 
    def __init__(self, name, age):
      self.name = name #This created the perameter
      self.age = age #This created the perameter
      #This made the method and the sentence that will be outputed
    def hello(self):
        print('Hello, my name is ' + self.name + ' I am ' + str(self.age) + " years old.")
  #This sets the name and age that is inputed 
person = Person('Prity', 16 )
#This outputs the method with the inputs
person.hello()



"""
Task 2: Animals Speak
Create a base class Animal with a empty method called speak. 

Then create two subclasses, Dog and Cat, each with their own speak method. 

Create objects using these subclasses and call the speak method.
"""
print()
print()
#This created the class animal
class Animal:
   #This created the method speak
   def speak(self):
      #This creates an empty method
      pass
   #This created a subclass for dog under animal
class Dog(Animal):
   #This replaces the other classes speak and prints woof for the dog
   def speak(self):
      print("Woof")
    #This created a subclass for cat under animal
class Cat (Animal):
   #This replaces the other classes speak and prints meow for the cat
   def speak(self):
      print("Meow")
      #This creates the input for what the dog and cat says
animal1 = Dog()
animal2 = Cat()
      #This outputs the noises of animals
animal1.speak()
animal2.speak()

"""
Task 3: Banking
Create a class BankAccount with attributes balance and owner. 

Include methods for depositing and withdrawing money, which should modify the balance attribute.

Test these methods with instances of the class.
"""
print()
print()
#This created the class
class BankAccount:
   #This created the method
   def __init__(self, balance, owner):
      self.balance = balance #This is the initial banlance
      self.owner = owner #This is the accounts owners
   def deposit(self, money):
      self.balance += money #This adds money to your balance
   def wdraw(self, money):
      self.balance -= money #This subtracts money from your balance 
acct= BankAccount(45000, "Prity")

acct.deposit(10000) #This deposits the money
print(acct.balance)
print()
acct.wdraw(15000) #This withdraws the money
print(acct.balance)