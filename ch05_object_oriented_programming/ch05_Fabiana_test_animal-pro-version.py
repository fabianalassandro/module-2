# -*- coding: utf-8 -*-
"""
Created on Wed Dec  5 14:00:42 2018

@author: fabia
"""

class Animal():
    def __init__(self, name, age=0):
        self.name = name
        
    def eat(self):
         print('yum')
         
class Dog(Animal):
    def __init__(self, name, age=0,barkNumber=0):
        self.barkNumber = barkNumber
        
    def bark(self):
        print('Woof! '*self.barkNumber)
        
        
class DogAgent(Dog):
    def detect(self):
        if self.barkNumber>=3:
            print('strenger coming!!!')
        
class Cat(Animal):
    def meow(self):
        print('Meow')
name = input('what is your pet\'s name:')        
age = int(input('what is your pet\'s age: '))
bark = int(input('how many times you heard it barked: '))

dog007 = DogAgent(name, age, bark) #always inheritant ancester's
dog007.bark()
dog007.eat()
dog007.detect()