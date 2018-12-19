# -*- coding: utf-8 -*-
"""
Created on Mon Dec  3 15:33:32 2018

@author: fabia
"""

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


