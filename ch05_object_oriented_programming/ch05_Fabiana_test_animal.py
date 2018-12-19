# -*- coding: utf-8 -*-
"""
Created on Wed Dec  5 12:01:00 2018

@author: fabia
"""

class Animal():
    def eat(self):
        print('yum')
    def poo(self):
        print('doh!')
        return('doh!')

class Dog(Animal):
    def bark(self):
        print('woof!')
        
class Cat(Animal):
    def meow(self):
        print('meow')
    def prrr(self):
        print('prrr')
    def notSoMeow(self):
        print('not so meow')    

Snoopy = Dog()
Snoopy.bark() #subclass method - here we're using a subclass method
Snoopy.eat() #superclass method - here we're using a superclass method
        



#My very own version with the name of my fat cat :)
Muffa = Cat()
answer = input('How are you?')
if answer == 'good':
    Muffa.meow()
elif answer == 'very good':
    Muffa.prrr()     
else:
    Muffa.notSoMeow()   
Muffa.meow()

surpise = input('Muffa is pooing')
surpise = Muffa.poo()

