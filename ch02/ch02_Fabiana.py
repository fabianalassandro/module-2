#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 29 09:37:07 2018

@author: fabia
"""

A = 5 - 6
B = 8 * 9
C = 6 / 2
D = 5 / 2
E = 5.0 / 2
F = 5 % 2
G = 2 * (10 + 3)
A = 2 ** 4

print(A)


age = 5
age = "almost three"
age = 29.5
age = "I really don't know!"


print(age)

print ('hello' + 'world')
print ("Joke " * 3)
print ("Chen" + "3")
print ("hello".upper())
print ("GOODBYE".lower())
print ("the lord of the rings".title())
print ('\n') #THIS IS A BREAK LINE 

print (("Bob \n") * 3)

S1 = 'hello ' + 'world\n'
S2 = "Joke " * 3
S3 = 5

print(S1+(S2*10))
print (S1 + S2 + str (S3)) # S3 is an integer so it cannot be added to strings. To do this I have to transform the variable (S3) in a string.
print (str(S3)) 

strExample = 'a-b-c-d-happy'
splitStr = strExample.split ('-')
print (strExample.split('-'))

age = 5
like = "painting"

age_description = "My age is {0} and I like {1}.".format(age, like)
print (age_description)

"""sono un commento
su due righe"""


