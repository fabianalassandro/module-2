#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 29 09:37:07 2018

@author: fabia
"""

###############################################

#CHAPTER 2 - OPERATIONS, STRINGS AND VARIABLES

###############################################

#--------------------------
# Task 1 - Simple operations with Python
#--------------------------

#Operators:
#  + plus
#  - minus
#  * multiply
#  / divide
#  ** exponent
#  % module --> This is tricky. By using module I receive the remainder (in Italian: rimanenza della divsione) as a result.

A = 5 - 6
B = 8 * 9
C = 6 / 2
D = 5 / 2
E = 5.0 / 2
F = 5 % 2
G = 2 * (10 + 3)
H = 2 ** 4

print(A)#--> -1 This is the result of 5 - 6. 

print(F)#--> 1 | This is a MODULO. We use it to get a REMAINDER. A Remainder is "la rimamenza" of number divided for another number.

print(H)#--> 16 | This is the result of ((2*2)*2)*2 . 

#PS: in order to see the result on the console when we run the file I need to use the print() function. It's just enough to put what we want to see on the console inside the parenthesis. NO "=". YES (). It's the same use or not space between number and operators.



#--------------------------
# Task 2 - Practicing with variables
#--------------------------

print()
age = 5
age = "almost three"
age = 29.5
age = "Almost 30!"
print(age)

# I use = to assign a variable.
# The power of a variable is that I can assign a value to a variable. Let's say that a variable works as a placeholder. If I change the value where the variable is defined than the change will go automaically on any other place where the variable is called in a function.


#--------------------------
# Task 3 - Basic string manipulation
#--------------------------

# STRINGS 
# Strings are a group of individual character. A sentence is a string.


#Below some examples of STRING OPERATIONS
print()
print ('hello' + 'world')# --> helloworld 
# I can use + to concatenate two strings
print ("Joke " * 3)# --> Joke Joke Joke 
# I can use * to repeat a string
print ("Chen" + "3")#--> Chen3

#Below some examples of how to use String Object Methods
print()
print ("hello".upper())#--> HELLO 
#To transform a string in uppercase
print ("GOODBYE".lower())#--> goodbye
#To transform a string in lowercase
print ("the lord of the rings".title())#--> The Lord Of The Rings
#To transform a string in upperlowercase
print ('\n') #THIS IS A BREAK LINE. It means go to a new line.

print (("Bob \n") * 3)#--> here I'm printing Bob in a new line for three times



#------------------------
# Another Example
#------------------------
S1 = 'hello ' + 'world\n'
S2 = "Fabiana " * 3
S3 = 5

print(S1+(S2*10))
print (S1 + S2 + str (S3)) # S3 is an integer so it cannot be added to strings as it is. To do this I have to transform the variable (S3) in a string.
print (str(S3))#--> 5 | This is a number transformed in a string. I cannot do operations with it.
print(S3)#--> 5 | This is a number.I can do operaions with it.

#PS: Multiplication has precedence on Addition



#------------------------
# Another Example n.2
#------------------------
print()
a = 1
a = a + 1
print (a)#--> 2
b = "hello"
print (b)#--> hello
c = b.title()
print (c)#-->Hello
d = "ciao"
e = d.upper()
print (d)#-->ciao
print (e)#-->CIAO
name = "Fabiana"
f = "Hello {0}! ".format(name)
print (f)#-->Hello Fabiana!
name = "Marta" #--> Here I'm changing the name, but because I'm doing that after the function, I'm not replacing Fabiana with Marta
print (f)#-->Marta
print (f *5)#--> Hello Fabiana! Hello Fabiana! Hello Fabiana! Hello Fabiana! Hello Fabiana! 



#--------------------------
# Task 4 - String formatting
#--------------------------
#

age = 5
like = "painting"

age_description = "My age is {} and I like {}.".format(age, like)
print (age_description)

age_description = "My age is {0} and I like {1}.".format(age, like)
print (age_description)
#Both the variables are giving the same result.
# {} is used as a placeholder to call the previous two variables


# How to split a string by usig the split() function
print()
strExample = 'a-b-c-d-happy'
splitStr = strExample.split ('-')
print (strExample.split('-'))


"""I'm a comment
on two lines. 
"""


