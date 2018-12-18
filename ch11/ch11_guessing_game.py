# -*- coding: utf-8 -*-
"""
Created on Tue Dec 18 13:58:58 2018

@author: fabia
"""

    
#--------------------------------
# Task 5 and 6 - The guessing game
#--------------------------------  

from random import randint
def guess(attempts,roofNumber):
    number = randint(1,roofNumber)# number equal to a random number between 1 and the number I set as roofNumber. In this case I set 10 as roofNumber.
    print(number)
    print ("Welcome! Can you guess my secret number?")
    while attempts > 0:# this seems an obvious assumption to start the while. I'm wonderin if there's another way.
        userNumber = int(input('Please type here: '))
        if userNumber == number:
            print('Wow! You win! You have other', attempts - 1, 'attempts')
            break
        elif userNumber < number:
            print('Try a bigger number. You have other', attempts - 1, 'attempts')  
        else:
            print('Try a small number. You have other', attempts - 1, 'attempts')
        attempts = attempts - 1# the shortcut is attempts -= 1
    print ("END-OF-GAME: thanks for playing!")
    
guess(3, 10)#--> Here I'm saying the computer use 3 "attempts" and 10 as "roofNumber" to came with a randm number between 1 and 10.
# guess(attempts,roofNumber)
# is replacing by
# guess(3, 10)


# In this exercise I'm asking to a user to guess the secret number created in a random way from the computer starting from the roofNumber.  