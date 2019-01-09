#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan  8 13:51:51 2019

@author: Fabiana
"""

####################################################

# CODING QUESTIONS - 5 BT CODING INTERVIEW EXAMPLES

###################################################

# Write the letters "A" to "Z" (in upper case) to the console, placing each letter on a new line

alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","w","v","x","y","z"]

for i in alphabet:
    print((i).upper())
    

#print(alphabet)
#
#alphabet = str(alphabet).upper()
#
#print(alphabet)
    

# For every third letter, write it to the console in lowercase instead    

print()
for i in range(len(alphabet)):
    
    if (i+1) % 3 == 0:
        alphabet[i] = alphabet[i].lower()
    else:
        
        


# For every fourth letter, write its numeric position in the alphabet to the console instead (e.g. instead of outputting 'D' output '4).
    

    