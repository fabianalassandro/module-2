# -*- coding: utf-8 -*-
"""
Created on Thu Dec 13 09:29:26 2018

@author: fabia
"""
###################################

#CHAPTER 09 - LISTS AND TUPLES

###################################



#----------------------------------
#Task 1 - Create a list
#----------------------------------

my_favourite_fruits = ['apple', 'orange', 'banana']
x = ['this', 55, 'that', my_favourite_fruits]
#As shown above list can contain mix type of data!

print (x[0]) # --> this 
print (x[1]) # --> 55 
print (x[2]) # --> that 

print (x[3]) # --> ['apple', 'orange', 'banana']  

print (x[-1][-2]) #This is the way to pick an element inside of the list --> orange

print (x[-1][-2][-3])#This is the way to pick an element inside of an element contained in the list --> n

#print(x[4]) --> This returns an error because there's no a fourth element in the list



#----------------------------------
#Task 2 - Modify the list
#----------------------------------

#Delete an item in list
print()
print('Delete an item in list')
x = ['this', 55, 'that', my_favourite_fruits]
x.remove(my_favourite_fruits)
print(x)#--> ['this', 55, 'that']

#Above I'm trying to delete an item from a list. In fact in the list there's not anymore the items contained in the list "my_favourite_fruits".
#PS: A list is a MUTABLE type. That means that I can edit it.


#Replacing an item in list
print()
print('Update the list by replacing an item')
x[1] = 'and'#Here we're replacing the item '55' with 'and'
print(x)#--> ['this', 'and', 'that']


#Add an item in list
print()
print('Add an item in list')
x.append('again')
print(x)

#----------------------------------
#List Operations
#----------------------------------

print()
print('List Operators')
x = ['the', 'cat', 'sat']
y = ['on', 'the', 'mat']
z = x + y
print (z)# --> ['the', 'cat', 'sat', 'on', 'the', 'mat']

#q = x * y  
#print(q) --> It's not possible moltiplicate,devide or substract lists 

print()
print('Set type')
print (set(x+y))#Set gives the list of items available. So it will cut the duplicates and it will show them in a random way.

x = ['this', 'and', 'that', 'once', 'again']
print(x[1:-2]) 



#----------------------------------
#Task 3 - Slicing a list
#----------------------------------
# Slicing means select a portion of a list. It's pick a range of items.
#Rememeber the we start to count from 0. The range 1:4 is slicing the items from 1 to before 4, such as 3. 
print()
print('Slicing a list')
x = ['this', 'and', 'that', 'once', 'again']
print(x[1:4])# --> ['and', 'that', 'once']
#


#Let's try something else
print()
z = ['the', 'cat', 'sat', 'on', 'the', 'mat']
print(z)
print('Slicing with a range larger than the available items --> [3:10]')
print(z[3:10])#-->['on', 'the', 'mat'] I
print('Slicing with a range of not avaialable items --> [8:10]')
print(z[8:10])#--> [] If there are no available items, then the brackets are empty. But no errors in the console
# This method is more permessive than access by index - see the last bit of Task 1 - in fact if I try 




#----------------------------------
#Task 4 - Sorting a list
#----------------------------------
print ()
print ('Sorting list with sorted()')
x = [7,11,3,9,2]
y = sorted(x)
print (y)#--> [2, 3, 7, 9, 11] I'm ordering the items from smaller to bigger

print ()
print ('Sorting list with .sort()')
x.sort()
print (x.sort())#--> None. I DON'T KNOOOOW!


# REVERSE SORT WITH SORTED()
print ()
print ('Reverse sort - sorted()')
print(sorted(x,reverse=True))

# REVERSE SORT WITH .SORT()
# At the moment is just enough now that there are two ways to sort the order of elements in a list
print ()
print ('Reverse sort - .sort()')
x = [7,11,3,9,2]
x.sort()
print(x.sort())#--> None. It's still CONFUSING, but basically here I'm not storin the information. I don't have any output. So,it's like not having the return by default. This is why I don't have any value.

print(x.sort(reverse=True))#--> None. Take a look above.

#----------------------------------
#Task 4 - Sorting a list
#----------------------------------
print()
print ('List VS Tuples')

#List example n.1
print()
print ('List example n.1')
a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
del a[-1]
print(a)#--> [0, 1, 2, 3, 4, 5, 6, 7, 8] In the lists I can delete an item because is mutable.


#Tuple example n.1
#b = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
#del b[-1]
#print(b)  #--> TypeError: 'tuple' object doesn't support item deletion ||| In tuple is not possible delete an item because TUPLES are immutable

#Tuples are immutable, for this reason if I run "b" I receive an error saying: tuple object doesn't support item deletion. This is not possible to make any change to tuple. 

###################

#List example n.2
print()
print ('List example n.2')
a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
a[0] = 50
print (a)#--> [50, 1, 2, 3, 4, 5, 6, 7, 8, 9] I'm replacing 0 with 50

#Tuple example n.2
#b = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
#b[0] = 50
#print(b)   #--> TypeError: 'tuple' object does not support item assignment ||| In tuple is not possible replace an item because TUPLES are immutable

###################

#List example n.3
print()
print ('List example n.3')
a.append('z')
print(a)#--> [50, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'z'] I'm adding an item at the end of the list


#Tuple example n.3
#b = (0, 1, 2, 3, 4, 5, 6, 7, 8,
#9)
#b.append('z')
#print(b)

# as mentioned above it's not possible to do any change to a Tuple. For this reason if I try to add an element by using .append() I receive an error on the console saying: 'tuple' object has no attribute 'append'


#----------------------------------
#Lambda function
#----------------------------------
print()
print('Sorted type')

a = [0,1,2,3,4,5,6,7,8,9]
b = (0,1,2,3,4,5,6,7,8,9)
c = [7,11,3,9,2]
myFavF = ["apple", "orange", "banana"]
x = ["az", "cx", "by", "dw"]
z = ["ev", "fu", "gt", "hs"]
y = sorted(x)

x2 = [('a', 3, z), ('c', 1, y), ('b', 5, x)]
print(sorted(x2))#--> [('a', 3, ['ev', 'fu', 'gt', 'hs']), 
                        #('b', 5, ['az', 'by', 'cx', 'dw']), 
                        #('c', 1, ['az', 'by', 'cx', 'dw'])] 
#now the items are in alphabetical order. Check the letters inside the elements.
print()
print('Lambda function s:s[1]')
print(sorted(x2, key=lambda s:s[1]))#-->[('c', 1, ['az', 'by', 'cx', 'dw']), 
#                                        ('a', 3, ['ev', 'fu', 'gt', 'hs']), 
#                                        ('b', 5, ['az', 'by', 'cx', 'dw'])]
#Here I'm saying go inside each elements, pick the "1" item, such us the second item (because it starts from 0) and using it as key to order them from smaller to bigger.
                                        
print()
print('Lambda function s:s[2]')
print(sorted(x2, key=lambda s:s[2]))#--> [('c', 1, ['az', 'by', 'cx', 'dw']), 
#                                         ('b', 5, ['az', 'cx', 'by', 'dw']), 
#                                         ('a', 3, ['ev', 'fu', 'gt', 'hs'])]
#Here I'm saying go inside each elements, pick the "2" item, such us the third item (because it starts from 0) and using it as key to order them from smaller to bigger. But this time is a bit more complicated because I'm going inside x, y and z and again picking the third item and 


###########
print()
print('Let\'s try again this Lambda thing')
x = [1, 2, 3, 4]
y = [3, 4, 10, 3]
z = [20, 10, 30, 40]

x2 = [('a', 3, z), ('c', 1, y), ('b', 5, x)]

print(sorted(x2, key=lambda s:s[2]))
# Below what we're printig
#[('b', 5, [1, 2, 3, 4]), 
# ('c', 1, [3, 4, 10, 3]),
# ('a', 3, [20, 10, 30, 40])]
# Basically above I'm saying check each of the 3 elements inside x2, then pick the third item inside of each one and using it as a key to order the 3 elements from the smaller one to the bigger one. Because, the third elements  are all variables, then I'm going again inside each list and I'll check and pick the third item and using it as key to order the elements.


###########
print()
print (sorted(x2, key=lambda s:s[2][2]))

