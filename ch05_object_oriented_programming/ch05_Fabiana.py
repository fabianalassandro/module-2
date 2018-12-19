# -*- coding: utf-8 -*-
"""
Created on Wed Dec  5 09:12:52 2018

@author: fabia
"""

##########################################

#CHAPTER 05 - OBJECT ORIENTED PROGRAMMING

##########################################


#----------------------------------------
# Task 01 - Using classes
#----------------------------------------

print()
class Customer(object):
    """
    A customer of ABC Bank with a checking account. Customers have the following properties:
    Attributes:
        name: A string representing the customer's name.
        balance: A float tracking the current balance of the customer's account.
    """
    
    def __init__(self, name, balance=0.0):
        """Return a Customer object whose name is *name* and starting balance is *balance*."""
        self.name = name
        self.balance = balance
        
    def withdraw(self, amount):
        """Return the balance remaining after withdrawing *amount* dollars."""
        if amount > self.balance:
            raise RuntimeError('Amount greater than available balance.')
        self.balance -= amount
        return self.balance
    
    def deposit(self, amount):
        """Return the balance remaining after depositing        *amount* dollars."""
        self.balance += amount
        return self.balance
    
    def __str__(self):
        """Return a sentence (string) with the number of the balance converted in a string -take a look at the second string- in order to place the information in the sentence"""
        return ("Customer " + self.name + " has a balance of " + str(self.balance) + "."  )    
        
jason = Customer('Jason Taylor', 1000.0)
fabiana = Customer('Fabiana Lassandro', 2000.0)
print(fabiana.balance)   
print(jason) 

  
#----------------------------------------------------------
# Task 02 & 3 - Create my own object (Classes and Superclasses)
#----------------------------------------------------------

# Using Inheritance

print()
class Robot():
    def move(self):
        print('...move move move..')
        
class CleanRobot(Robot):
    def clean(self):
        print('I vacuum dust')
        return('I vacuum dust')
        
class CookRobot(Robot):
    def cook(self):
        print('I make rice')
        
bob = CleanRobot()
bob.clean()
bob.move()

print('Hello I\'m Bob and '+ str(bob.clean()))

bob = CookRobot()
bob.cook()


#----------------------------------------------------------
# Task 04 - How to use Classes ans Superclasses 
#----------------------------------------------------------

# Using Association
print()

class Animal():
    def eat(self):
        print('yum')
class Dog(Animal):
    def bark(self):
        print('Woof!')
        return('Woof!')#try to comment it and check the console again
        
class Robot():
    def move(self):
        print('...move move move...')
class CleanRobot(Robot):
    def clean(self):
        print('I vacuum dust')
        
class SuperRobot():
    def __init__(self):
        #This class contains 3 objects
        self.o1 = Robot()
        self.o2 = Dog()
        self.o3 = CleanRobot()
            
    def playGame(self):
        print('alphago game')
    def move(self):
        return self.o1.move() #using robot class method
    def bark(self):
        return self.o2.bark() #using dog class method
    def clean(self):
        return self.o3.clean() #using cleanrobot method
        
gianni = SuperRobot()
gianni.move()
gianni.bark()

print('Gianni is the best robotdog ever! Let\'s talk with him. So, what can you do ?' + str(gianni.bark() ))
        
