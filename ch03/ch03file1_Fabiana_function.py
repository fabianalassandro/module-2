# -*- coding: utf-8 -*-
"""
Created on Thu Nov 29 13:58:35 2018

@author: fabia
"""

###########################################

#CHAPTER 03 - FUNCTIONS & IMPORTING MODULES

###########################################

#---------------------------------------
#Task 01 - Input from a user
#---------------------------------------

print ("What's your name? ")
name = input()# Type: Fabiana
print ("Hello {}!".format(name.title()))#-->Hello Fabiana!

print()# To print a break line
print ("Where do you come from?")#-->Where do you come from?
country = input()# Type: Italy
print ("I come from {}!".format(country.title()))#--> Where do you come from?

#Another way to do the thing above is the following one:
print()
name = input("What's your name? ")
city = input("What's your city? ")
print ("Hello {}! from {}".format(name,city))

#---------------------------------------
#Task 02 - MY FIRST FUNCTION
#---------------------------------------

def hello_world():
    print ("Hello World!")
    
def name_surname():
    print ("What's your name?")
    name = input()
  
    print ("My name is {}".format(name))
    
def addition():
    print (4)
    
name_surname()


######################################################################

# 03/12/2018

######################################################################

#def hello_world_3args(d, e, f): 
#    print ("{} {} {}".format(d, e, f))
#    
#a1 = 'hello'
#b1 = 'world'
#c1 = "!"
#
#a2 = 'love'
#b2 = 'coding'
#c2 = "!"
#
#hello_world_3args(a1, b1, c1)
#hello_world_3args(a2, b2, c2)
#
"""
#Imagine "d" as "placeholder1", "e" as "placeholder 2" and "f" as "placeholder3
#in print I set how it should look like the sentence. I have to ad a pair of 
#curly brackets for every placeholders in this case 3 pairs of curly brackets.
#
#To delete the space before the "!" I have to delete it from the 2 curly brackets
#in print.
"""

################################

# add two numbers
#number1 = 1
#number2 = 2
#
#def add_two_numbers(number, anotherNumber):
#    
#    answer = number + anotherNumber
#    print ("{} plus {} is {}".format(number, anotherNumber, answer))
#    
#add_two_numbers (number1, number2)

################################



#def add_two_numbers_and_return_value(n1, n2):
#    return n1+n2
#Result1 = add_two_numbers_and_return_value(4, 5)


def add_two_numbers_and_return_value(n1, n2):
    answer = n1+n2
    return answer

Result1 = add_two_numbers_and_return_value(4, 5)

"""
To see the result I can use two methods:
    1. add print in this way: Result1 = print (add_two_numbers_and_return_value(4, 5))
    2. go to the console and type direcly: Result1


"""
