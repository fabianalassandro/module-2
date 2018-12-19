# -*- coding: utf-8 -*-
"""
Created on Tue Dec  4 09:25:17 2018

@author: fabia
"""

########################################

#CHAPTER 4 - CONDITIONALS

########################################


#------------------------------------------------------
# Task 3 - Using conditional statements (IF statements)
#------------------------------------------------------

number = input("Enter a number between 1 and 10: ")
number = int(number) #Converts the input string to an integer. We're using it because by default it's a string, so first of all I have to set it as a number.

if number > 10:
    print ("Too high!")
if number <= 0:
    print ("Too low!")



#------------------------------------------------------
# Task 4 - Using conditional statements (ELSE statements)
#------------------------------------------------------
   
number = input("Enter a number between 1 and 10: ")
number = int(number) #Converts the input string to an integer. We're using it because by default it's a string, so first of all I have to set it as a number.

if number > 10:
    print ("Too high!")
if number <= 0:# This second if should be an elif. I'm usinf if just for this example
    print ("Too low!")
else: print("Cool")

#If the number typed by the user is larger then 10 I print: Too high!. If the number is less equal to 0 I print: Too low!. If the number is between 0 or 10 I print: Cool!.


#------------------------------------------------------
# Task 5 - Using conditional statements (ELIF statements)
#------------------------------------------------------

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

#I use elif to state all the cases between the first one (if) and the very last one (else) that is closing the if conditional.
    