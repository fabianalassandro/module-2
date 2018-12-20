# -*- coding: utf-8 -*-
"""
Created on Mon Dec  3 15:33:32 2018

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
#HOW TO IMPORT A FUNCTION FROM ANOTHER FILE
#---------------------------------------

import ch03_Fabiana_list_functions as fabs

#---------------------------------------
#Task 02 - MY FIRST FUNCTION
#---------------------------------------

name_surname()#-->What's your name? | To trigger a function I need to call it. In order to call it I need to type the name of the function followe by (). In this case: name_surname() 


addition()#--> 4
#Here I'm just using a function to print the number 4. Of course, it would be enough print directly print(4), but it's just an example to show how a function works.


#----------------------------------------------
# Task 04 - Add two numbers ( and Return value)
#----------------------------------------------

add_two_numbers (number1, number2)#--> 1 plus 2 is 3 | by calling this function I'm printing what's on the print() function above.

#In order to build a function - that is basically a reusable calculation or let's say operation - I need to build something abstract by using words instead of real values. Then when I want to use a function for a real operation what I need to do is:
# 1. Call the function
# 2. insert in the variables the values that I want to calculate


#--------------------------------------
# Task 04.2 - How to use RETURN value
#--------------------------------------
returned_value = add_two_numbers_and_return_value()
print(returned_value)#--> 3
print(returned_value - 5)#--> -2

Result1 = add_two_numbers_and_return_value(4, 5)
print(Result1)#--> 9

Result1 = add_two_numbers_and_return_value(6, 7)
print(Result1)#--> 13


#---------------------------------------
# Task 05 - Temperature Conversion
#---------------------------------------

conversion = convert_temp()
print(conversion)#--> (39.2, 277.15) | I need to assign a variable to the function convert_temp in order to let me print what stored in the Return value. 
#PS: note that I'm doing this out of the function.
#To show a function in the console is enough to call it like this: convert_temp(), but in order to use the result to do something I have to assign a variable to the function and then print it.

f, k = convert_temp()
print("The temperature in Fahrenheit is {} and the temperature in Kelvin is {} ".format(f, k))

#Here I assign two variables in order to save the two results returned on top in two different variables and reuse the separately. This is much more convenient if we need to do some calculation with them. 


#---------------------------------------
# OTHER FUNCTIONS TO IMPORT IN THE FILE
#--------------------------------------

hello_world_3args(a1, b1, c1)
hello_world_3args(a2, b2, c2)

#Example 1
arg1 = 0
arg2 = 2
fabs.print_two_again(arg1, arg2)


# OR A QUICKER WAY:
fabs.print_two_again(1, 1)


#Example 2
cheese_count = 10
boxes_of_crackers = 20

fabs.cheese_and_crackers(cheese_count, boxes_of_crackers)


