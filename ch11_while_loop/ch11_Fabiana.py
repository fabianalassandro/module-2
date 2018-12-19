# -*- coding: utf-8 -*-
"""
Created on Mon Dec 17 09:50:12 2018

@author: fabia
"""

###################################

#CHAPTER 11 - THE "WHILE" LOOP 

##################################


#--------------------------------
# Task 1 - Repeated division
#--------------------------------

x = 33
while x >= 1:
    print(x, ': ', end='')#--> ‘end=’ is a print parameter that means to print a space rather than a new line. Basically, it's saying at the end add a blank space and concatenate what's next, in fact wihin the single quotes is empty.
    x = x / 2
print(x)#--> 33 : 16.5 : 8.25 : 4.125 : 2.0625 : 1.03125 : 0.515625

#Above I'm dividing a number - in this case is "33" - per 2 and I keep doing this until I arrive to 1. While purpose is exactly this last bit: do this until you meet this condition - in this case is until you reach 1 as a result.


#--------------------------------------
# Task 2 - Computing triangular numbers
#--------------------------------------

# So, what is a TRIANGULA NUMBER? 
# Any of the series of numbers (1, 3, 6, 10, 15, etc.) obtained by continued summation of the natural numbers 1, 2, 3, 4, 5, etc.

print()
print('Computing triangular numbers')
def triangular(n):
    trinum = 0
    while n > 0:
        trinum = trinum + n
        n = n - 1
    return trinum
print(triangular(1))#--> 1 | Because here I'm doing 0 + 1
# The function is working because I'm typing a number in the the argument place. By doing that 1 will replace n in all the function.

#Other examples
print(triangular(3))#--> 6 | Because here I'm doing (((0 + 1)+2)+3) 

print(triangular(5))#--> 15 | Because here I'm doing (((((0 + 1)+2)+3)+4)+5) 


#--------------------------------
# Task 3 - Student marks
#--------------------------------
# INSTRUCTIONS:
# 1.	Create a loop to determine if student marks are a pass/fail/ﬁrst.
# 2.	Make a plan, e.g. mark >= 70 is first class, mark>= 40 is pass and mark < 40 is fail.
# 3.	Write the pseudocode.
# 4.	Note in this programme you can use user inputs and use conditional logic
#to interact.

print()
print('Student Mark calculation')
mark = 1
while mark > 0:
    mark = input('Enter mark: ')
    mark = int(mark)
    print("Mark is", mark, end='')
    if mark >= 70:
        print(" - first class!")
        break#--> To stop the loop. Try to comment "break"
    elif mark >= 40:
        print(" - that's a pass")
        break
    else:
        print(" - that's a fail")
        break

# "break" is used to stop the while loop. In fact, if I comment out "break", on the console I'll keep see asking the same thing, such as --> Enter mark:
# "break" has to stay after the first "if", but after print. If I put it before print() on the console I'll see --> Mark is 80 (or any number I type on the console)      
        
print()
print()
print('Student Mark calculation 2 - The revenge of the marks')
mark = 1
while mark > 0:
    mark = input('Enter mark: ')#--> input is inside the while because I need to update the value
    mark = int(mark)
    print("Mark is", mark, end="")
    if mark >= 80:
        print(" - first class! :D")
        break#--> To stop the loop. Try to comment "break"
    elif mark >= 60:
        print(" - that's a pass :)")
        break
    elif mark >= 40:
        print(" - that's a barely pass -_-")   
        break
    else:
        print(" - that's a fail :(")
        break        
    
#----------------------------------------------------
# Task 4 - Using the BREAK statement in a while loop
#----------------------------------------------------  
#INSTRUCTIONS:
#Using the break statement in a while loop
#Write a little application that prints a greeting for the name entered, until the user enters ’done’. Using a while True loop will run indefi nitely.
#Think about how to go about this before you start coding.        

print() 
print('Let\'s break the loop! Enter your name below.')    
while True:
    name = input('Enter name: ')
    if name == 'done':
        break
    print('Hello', name)# PS: print has to be indented   
    
#Above I'm creating a conditional to trigger the BREAK STATEMENT. I'm saying if you don't want to type your name over and over again then type the magic word "done". PS: done could be any word. Try use ciao instead of done.  
    
    
   
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
    


################################################

#Phone Book exercise solved by using While Loop

################################################

# In this exercise I'm building a dictionary called "phoneBook" -- as I did in the file ch10 > ch10_phonebook_exrcise_Fabiana.py -- by replacing the count_users conditional function with the while loop. This solution is way to neat and clear. CLEAN CODE.

#Furthermore, I'm also "cleaning the dataCollection() function by using directly the input() function.
#*** For example:
#print('What\'s your name?')
#    name = input() 
#***it could be condensed in:
#name = input('What\'s your name? ')


def dataCollection(phoneBook):
    print()
    while True:
        name = input('What\'s your name? ')
        if name == 'stop':
            break
        phoneNumber = input('Hello {}! Can you type the last 3 digits of your phone number? '.format(name))
        print('Thank you {}'.format(name))
        luckyNumber = input('What\'s your lucky number? ')
        print('Awww {}. It\'s my favourite too!'.format(luckyNumber))
        postcode = input('What\'s your postcode? ') 
        city = input('What\'s your city? ')
        age = input('Thank you {}! What\'s your age? '.format(name))
        print('Wow {}! You\'re so young!'.format(name))
        print('The phonebook is now updated.')
        

    #phoneBook = {name : [phoneNumber, luckyNumber, postcode, city]} #--> This was my first attempt to create a dictionary that automatically updates with data inserted by the users. Unfortunately with this method every time a new user inserts data is replacing the data of the last user.
    
        phoneBook[name] = [phoneNumber, luckyNumber, postcode, city, int(age)]#--> By using this way to create a dictionary we're moving the key outside the dictionary.  In this way the new data inserted from users are adding to the dictionary instead of replacing the previous one. 
#PS: Be careful the dictionary has to stay inside the function. Pay attentiont to the indentation. Otherwise I'll justa save the information of the last user.        
    
    
    return phoneBook#--> without "return phoneBook" is not possible to save any data insterted trough the inputs above. 


phoneBook = {}#--> in this way I'm setting an EMPTY DICTIONARY
phoneBook = dataCollection(phoneBook)#--> In this way I'm calling the Dictionay and "activate it".     
        


print(phoneBook)# --> 
  #{'Fabi': ['543', '7', 'wsd', 'Milan'], 'Joke': ['765', '27', 'le11', 'lboro'], 'zsazsa': ['876', '8', 'kon', 'Rome']} 

print('\n')
print(sorted(phoneBook.items(), key=lambda kv:kv[0]))
#--> Sorting dictionary by "name"

print('\n')
print(sorted(phoneBook.items(), key=lambda kv:kv[1][3]))#--> Sorting dictionary by "city"

print('\n')
print(sorted(phoneBook.items(), key=lambda kv:kv[1][1]))#--> Sorting dictionary by "lucky number"


#-----------------------------
#Compare the age of a user to the Queen's age
#-----------------------------
def queenDifference():
    QueenAge = 90
    className = input('What\'s the name of the person that you like to compare to the Queen?')
    diff = QueenAge - phoneBook[className][4]
    print(diff)

queenDifference()
    
# What am I doing in this function?
# 1. I need to define the Queen's age in the first variable
# 2. define the variable necessary for the user to select the person that wants to use to get age difference using the Queen's age as reference.
# 3. This variable is the most important bit. Here I'm doing the calculation. I'm picking the Queen's age (QueenAge) and set the difference between that and the one chose by the user among the 3 persons stored in the phoneBook dictionary. So, in: phoneBook[className][4] I'm saying pick the selection made by the user - className - and go to the dictionary to retrieve the value stored in age key.
      