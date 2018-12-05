# -*- coding: utf-8 -*-
"""
Created on Tue Dec  4 09:25:17 2018

@author: fabia
"""

#Q \ A 

# 1 argument
name= input("What's your name?")

# no arguments
print("what's your name?")
name = input()


# If/ else statement - first task
if 5>=10:
    print (True)
else:
    print(False)


# If/ else statement - second task
"""    
number = input("Enter a number between 1 and 10: ")
number = int(number) #Converts the input string to an integer. We're using it because by default it's a string, so first of all I have to set it as a number.

if number > 10:
    print ("Too high!")
elif number <= 0:
    print ("Too low!")
else: print("Cool")
"""

# If/ else statement - third task

age = input("How old are you?")
age = int(age)

if age <13:
    print("Child")
elif age <18:
    print("Teen")
elif age <65:
    print("Adult")
else:
    print("Pensioner")
    