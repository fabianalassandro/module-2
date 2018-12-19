# -*- coding: utf-8 -*-
"""
Created on Fri Dec 14 10:03:07 2018

@author: fabia
"""
#####################################

#CHAPTER 10 - DICTIONARIES

#####################################


#-----------------------------------
#Task 1 - Let's start a Dictionary
#-----------------------------------

#salary = {}
#salary['al'] = 2000
#salary['bo'] = 5000
#{}


#--------------------------------------------------------
#Task 2 - Create a Dictionary. Retrieve and update values
#--------------------------------------------------------
print()
print('***Create a Dictionary***')
tel = {'Ellen':680, 'Jennifer':222, 'Fabiana':628, 'Muna':856}
print(tel)#--> {'Ellen': 680, 'Jennifer': 222, 'Fabiana': 628, 'Muna': 856}

#How to access to a value inside a Dictionary
print()
print('***Access to a value***')
print(tel['Fabiana'])


#How to update a value inside a Dictionary
print()
print('***Update a Dictionary***')
tel['Fabiana'] = 620 
print(tel)#--> {'Ellen': 680, 'Jennifer': 222, 'Fabiana': 620, 'Muna': 856}


#---------------------------------------
#Task 3 - Look, update and delete values
#---------------------------------------

#How to delete a key from a Dictionary
print()
print('***Delete a key from a Dictionary***')
del tel ['Fabiana']
print(tel)

#-----------------------------------------------------
# Task 4 - Retrieving keys and vales from a dictionary
#-----------------------------------------------------  

#Get keys and values from a Dictionary
print()
print('***Get keys from a Dictionary***')
print(tel.keys())

print()
print('***Get values from a Dictionary***')
print(tel.values())

#Get a specific key or value from a Dictionary
print()
print('***Get a specific key from a Dictionary***')
#tel.keys()[0]#--> A dictionay cannot be indexed. To do that we have to transform it in a list before as below.
print(list(tel.keys())[0])

print()
print('***Get a specific value from a Dictionary***')
print(list(tel.values())[0])

#########################
whatever = 'Muna'

if whatever in tel:
    print(whatever, ':', tel[whatever])
else:
    print(whatever, 'not found!')#--> Muna : 856
    
    
#Let's try another example    
whatever = 'Gianni'

if whatever in tel:
    print(whatever, ':', tel[whatever])
else:
    print(whatever, 'not found!')#--> Gianni not found!    


#---------------------------------------------------
# Task 5 - Convert keys and values in list data type
#---------------------------------------------------    
counts = {'a': 3, 'c': 1, 'b': 5}
labels = list(counts.keys())
print(labels)

# Sorting a dictionary by values by using lambda
labels.sort(key=lambda v:counts[v])
print(labels)


 
#********** Whinnie The Pooh - Example **********
#Create a dictionary with keys and 2 values for evey key and then sort it for the second value using lampba function.

friends = { 'Pooh':[123, 'honey'], 'Tigger':[456, 'lollipop'], 'Eeyore':[789, 'carrots'], 'Piglet':[000, 'cakes'] }

print(sorted(friends.items(), key=lambda c: c[1][1]))#--> 
#[('Piglet', [0, 'cakes']), 
#('Eeyore', [789, 'carrots']), 
#('Pooh', [123, 'honey']), 
#('Tigger', [456, 'lollipop'])]


#########################
#PS: discover how to transform a dictionary to a list

friends = { 'Pooh':123, 'Tigger':456, 'Eeyore':789, 'Piglet':000}

friends_list=list(friends.values())
print(friends_list)

friends_list.append('P')#???????????????????????????


#----------------------------------------------
# Task 6 - How to avoid key errors
#----------------------------------------------
print()
tel = {'Ellen':680, 'Jennifer':222, 'Fabiana':628, 'Muna':856}

k = 'Eric'
if k in tel:
    print(k, ':', tel[k])
else:
    print(k, 'not found!')    

# PS: if I try to set j = Muna and I replace k with j I'm going to print the key and the value connected to Muna, so --> Muna : 856

#----------------------------------------------
# Task 7 and 8 
# Sorting dictionary values in descending order
#----------------------------------------------

#Sorting dictionary by key
print()
print('Sorting dictionary by key')
densities = {'iron':7.8, 'gold':19.3, 'zinc':7.13, 'lead':11.4}
metals = list(densities.keys())
print(metals)#--> ['iron', 'gold', 'zinc', 'lead']
#By using '.keys' we're sorting by keys

#Sorting dictionary by value
print()
print('Sorting dictionary by value')
metals_values = list(densities.values())
print(metals_values)
#By using '.values' we're sorting by values


#-------------------
#Exercise in class
#-------------------

print()
print('Sorting dictionary by key')
something = {'iron':[7.8, 1.1, 10], 'gold':[19.3, 1.2, 20], 'zinc':[7.13, 1.3, 30], 'lead':[11.4, 1.4, 40]}
#something = list(something.keys())
print(something)

print(sorted(something.keys(), key=lambda k: k))
print(sorted(something))#This is the short versione of the one on top 
 
#Order them by first value
print()
print('Sorting dictionary by value [0]')
print(sorted(something.values(), key=lambda v : v[0]))

#Order them by second value
print()
print('Sorting dictionary by value [1]')
print(sorted(something.values(), key=lambda v : v[1]))

#Order them by third value
print()
print('Sorting dictionary by value [2]')
print(sorted(something.values(), key=lambda v : v[2]))



#############################

# PHONEBOOK EXERCISE

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
  
