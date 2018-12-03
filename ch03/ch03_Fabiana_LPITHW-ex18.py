# -*- coding: utf-8 -*-
"""
Created on Mon Dec  3 13:43:23 2018

@author: fabia
"""

##############################################

#LEARN PYTHON IN THE HARD WAY - Ex. 18 

##############################################


# this one is like your scripts with argv
def print_two(*args):
    arg1, arg2 = args
    print ("arg1: {}, arg2: {}".format(arg1, arg2))

# ok, that *args is actually pointless, we can just do this
def print_two_again(arg1, arg2):
    print ("arg1: {}, arg2: {}".format(arg1, arg2))

# this just takes one argument
def print_one(arg1):
    print ("arg1: {}".format(arg1))

# this one takes no arguments
def print_none():
    print ("I got nothin'.")

print_two("Zed","Shaw")
print_two_again("Zed","Shaw")
print_one("First!")
print_none()
