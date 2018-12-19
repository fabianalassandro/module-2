# -*- coding: utf-8 -*-
"""
Created on Mon Dec 17 11:53:25 2018

@author: fabia
"""


#############################
#CHAPTER 10 - DICIONARY

#Phone Book exercise
#############################


def dataCollection(phoneBook, count_users):
    print()
    print('What\'s your name?')
    name = input()
    print('Hello {}! Can you type the last 3 digits of your phone number?'.format(name))
    phoneNumber = input()
    print('Thank you {}'.format(name))
    print('What\'s your lucky number?')
    luckyNumber = input()
    print('Awww {}. It\'s my favourite too!'.format(luckyNumber))
    print('What\'s your postcode?')
    postcode = input()
    print('What\'s your city?')
    city = input()
    print('Thank you {}! What\'s your age?'.format(name))
    age = input()
    print('Wow {}! You\'re so young!'.format(name))

    #phoneBook = {name : [phoneNumber, luckyNumber, postcode, city]} #--> This was my first attempt to create a dictionary that automatically updates with data inserted by the users. Unfortunately with this method every time a new user inserts data is replacing the data of the last user.
    
    phoneBook[name] = [phoneNumber, luckyNumber, postcode, city, int(age)]#--> By using this way to create a dictionary we're moving the key outside the dictionary.  In this way the new data inserted from users are adding to the dictionary instead of replacing the previous one.
    
    max_count = 1#--> (*)
    if count_users <= max_count: 
      count_users += 1
      print('Counter', count_users, '- completed')
      phoneBook = dataCollection(phoneBook, count_users)
      return phoneBook
    else:
        print('The phonebook is now updated.')
    return phoneBook

#(*) Why 1? Because the function run automatically the first time. Then I run it a second time - that is going to be [0].Then I run it a third time - that is [1] indeed.  

#-----------------------------------------
# The conditional above run the dataCollection() function 3 times. Basically I'm using it to ask the questions to 3 different users and not more.
#-----------------------------------------

count_users = 0
phoneBook = {}#--> in this way I'm setting an EMPTY DICTIONARY
phoneBook = dataCollection(phoneBook, count_users)

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
  