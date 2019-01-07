#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan  7 09:12:29 2019

@author: Fabiana
"""

######################################

# CHAPTER 13 - OOP PROJECT

######################################


#--------------------------------------
# Task 1 - Initialise the person class
#--------------------------------------

class Person:
        def __init__(self,name,age,gender):
           self.name = name
           self.age = age
           if gender == 'm':
              self.isMale = True
           elif gender == 'f':
              self.isMale = False
           else:
              print('Gender not recognised!')
              
p1 = Person('Finn', 12, 'm') # THIS IS AN OBJECT
print(p1.name,p1.age,p1.isMale)
# note that I'm not using "gender", but "isMale" to get the gender information

p2 = Person('Jake', 7, 'm')
print(p2.name)

p3 = Person('Marceline', 700, 'jsjsdj')# ???????????
#print(p3.isMale)              


#---------------------------------------------------
# Task 2 - More functionalities for the Person class
#---------------------------------------------------
print()
class Person:
   def __init__(self,name,age,gender):
           self.name = name
           self.age = age
           if gender == 'm':
              self.isMale = True
           elif gender == 'f':
              self.isMale = False
           else:
              print('Gender not recognised!')
   def greetingInformal(self):
      print('Hi', self.name)
   def greetingFormal(self):
      if self.isMale:
         print('Welcome, Mr', self.name)# I use self to access to the information of name in this case.
      else:
         print('Welcome, Ms', self.name)

p1 = Person('Harry',12,'m')
p2 = Person('Jean',30,'f')

print(p1.greetingInformal())#--> Hi Harry
print(p2.greetingFormal())#--> Welcome, Ms Jean
print(p1.greetingFormal())#--> Welcome, Mr Harry

#Above I'm taking the p1 object with all the stored data about the first person and I'm attaching the function by using .
#So here I'm saying print the sentence defined in the function greetingInformal or greetingFormal by using the information stored in the variables p1 or p2.

#------------------------------
# Task 3 - A greeting filter
#------------------------------

print()
class Person:
    def __init__(self,name,age,gender):
       self.name = name
       self.age = age
       if gender == 'm':
          self.isMale = True
       elif gender == 'f':
          self.isMale = False
       else:
          print('Gender not recognised!')
    def greetingInformal(self):
      print('Hi', self.name)
    def greetingFormal(self):
      if self.isMale:
         print('Welcome, Mr', self.name)
      else:
         print('Welcome, Ms', self.name)
    def greetingAgeBased(self):
       if self.age < 18:
          print('Welcome, young', self.name)
       elif self.age > 60:
          print('Welcome, venerable', self.name)
       else:
          self.greetingFormal()

p1 = Person('Harry',12,'m')
p2 = Person('Minerva',88,'f')
p3 = Person('Sirius',50,'m')

print(p1.greetingAgeBased())#--> Welcome, young Harry
print(p2.greetingAgeBased())#--> Welcome, venerable Minerva
print(p3.greetingAgeBased())#--> Welcome, Mr Sirius
  
            
#-------------------------------------------------
# Task 4 - Create a subclass for the Person class
#-------------------------------------------------

print()
class Wizard(Person): #Wizard here is a subclass of Person
    def greetingFormal(self):
       print('Welcome, Mr ', self.name, end=' ')# end=' ' is usede to connect this sentence with the following one.
       print('- you\'re a fine wizard!')

p1 = Person('Harry',12,'m')
print(p1.greetingFormal())#--> Welcome, Mr Harry
# Here I'm using the information stored in the superclass "Person"

p1 = Wizard('Harry',12,'m')
print(p1.greetingFormal())#--> Welcome, Mr  Harry - you're a fine wizard!
#Here I'm using the information stored in the subclass "Wizard"

           
# Subclasses can use functions of superclasses, but not viceversa 


#-------------------------------------------------
# Task 5 - Create a subclass for the Person class
#-------------------------------------------------

#Subclasses inherit what we set on __init__. If we want we can redefine it as shown below:

class Wizard(Person):
   def __init__(self,name,age):# Here I'm redefining the subclass by not using "gender", but just: name and age.
      self.name = name
      self.age = age
      self.isMale = True
      
# How to redefine it in a cleaner way

class Wizard(Person):
   def __init__(self,name,age,gender):
      Person.__init__(self,name,age,'m')
# Here I'm defining 'm' as default gender for Wizard subclass      


#----------------------------------------------
# Task 6 - Add new methods to the Wizard class
#----------------------------------------------
      
# Adding extra methods to subclasses
      
class Wizard(Person):
    def spell(self):
        print('Expelliarmus!')

p1 = Wizard('Hermione', 17, 'f') #Remember to add class or subclass after = in order to make it work and create an object.
print(p1.spell())           
