# -*- coding: utf-8 -*-
"""
Created on Mon Dec 17 11:53:25 2018

@author: fabia
"""


#############################
#CHAPTER 11 - WHILE LOOP

#Phone Book exercise solved by using While Loop
#############################

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
  