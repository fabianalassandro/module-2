# -*- coding: utf-8 -*-
"""
Created on Fri Dec 14 10:03:07 2018

@author: fabia
"""
#####################################

#CHAPTER 10 - DICTIONARIES

#####################################


#-----------------------------------
#Task 1
#-----------------------------------

#salary = {}
#salary['al'] = 2000
#salary['bo'] = 5000
#{}


#-----------------------------------
#Task 2 - Create a Dictionary
#-----------------------------------
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


#-----------------------------------
#Task 3 - Look and update
#-----------------------------------

#How to delete a key from a Dictionary
print()
print('***Delete a key from a Dictionary***')
del tel ['Fabiana']
print(tel)

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


#########################
counts = {'a': 3, 'c': 1, 'b': 5}
labels = list(counts.keys())
print(labels)

labels.sort(key=lambda v:counts[v])
print(labels)

######################### 
# *** Whinnie The Pooh - Example ***
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



#########################
#Sorting dictionary values in descending order
#########################

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


#########################
#Exercise in class
#########################

print()
print('Sorting dictionary by key')
something = {'iron':[7.8, 1.1, 10], 'gold':[19.3, 1.2, 20], 'zinc':[7.13, 1.3, 30], 'lead':[11.4, 1.4, 40]}
#something = list(something.keys())
print(something)

print(sorted(something.keys(), key=lambda k: k))
print(sorted(something))#This is theshort versione of the one on top 
 

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

