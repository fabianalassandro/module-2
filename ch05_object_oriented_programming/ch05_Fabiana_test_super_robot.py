# -*- coding: utf-8 -*-
"""
Created on Wed Dec  5 15:27:41 2018

@author: fabia
"""
import sys

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
    def __init__(self, name, age):
        #This class contains 3 objects
        self.name = name
        self.age = age
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
        
#bob = SuperRobot()
#bob.move()
#bob.bark()
#
#print('Bob is the best robotdog ever! Let\'s talk with Bob. So, Bob what can you do ?' + str(bob.bark() ))
        
name = sys.argv[1]
age = sys.argv[2]

print(name)
print(age)