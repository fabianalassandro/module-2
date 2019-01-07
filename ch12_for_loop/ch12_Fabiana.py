# -*- coding: utf-8 -*-
"""
Created on Thu Dec 20 09:31:06 2018

@author: fabia
"""

######################################

#CHAPTER 12 - THE "FOR" LOOP

######################################


#--------------------------------------
# Task 01 - Using a for loop in a list
#--------------------------------------

my_shopping_cart = ["cake", "plates", "plastic forks", "juice", "cups"]

for item in my_shopping_cart:# "item" activates the loop for the items 
    print (item)#--> 
#cake
#plates
#plastic forks
#juice
#cups


    
# Brief Recap about LIST data type    
print()     
x = ['aa', 'bb', 'cc']
x[1] = 33
print(x)#--> ['aa', 33, 'cc']
#Here I'm replacing bb with 33

print()
x.append('dd')
print(x)#--> ['aa', 33, 'cc', 'dd']
 #Here I'm adding the value 'dd' in a list 

#-------------------------------------
# Task 02 - Update list values
#-------------------------------------

print()
values = [875, 23, 45]
for val in values:# "val" could be any other word 
    print('My magic number is:' + str(val+50))#-->
#My magic number is:875
#My magic number is:23
#My magic number is:45

# The loop starts and goes into the list. Once there, it will pick the value and print it after the sentence: My magic number is: 
#The loop will go ahead until it will find values in the list.  
    
    
#-------------------------------------
# Task 03 - Create your own list
#-------------------------------------
print()
values = ['this', 55, 'that']
for item in values:
    print('***', item)#-->
#*** this
#*** 55
#*** that    

#In my list I can have strings and numbers
    
#-------------------------------------
# Task 04 - Loop trough a string type
#-------------------------------------
    
print()    
for charachters in "Yes":# "char" activates the loop for the characters 
    print(charachters)#-->    
#Y
#e
#s

# With a loop I can also go inside of a string type and split it charachter by carachter
    
#-------------------------------------
# Task 05 - Loop through a tuple
#-------------------------------------   
print()    
tuple_list = ('meow', 'woof', 'roar')
for versi in tuple_list:
    print (versi)


#-------------------------------------
# Task 06 - Create a salary dictionary
#-------------------------------------    

al = 20000
bo = 50000
ced = 1500

  #???????????????????????????????????
  
  
#-------------------------------------
# Task 07 - Example
#-------------------------------------   
print()  
densities = {'iron':7.8, 'gold':19.3, 'zinc':7.13, 'lead':11.4}

metals = list(densities.keys())
print(metals)#-->['iron', 'gold', 'zinc', 'lead']

metals.sort(reverse=True,key=lambda m:densities[m])
print(metals)#-->['gold', 'lead', 'iron', 'zinc']

#PS: to sort a list by value I need to use lambda. So m or any other word I'll use instead of "m" stands for the key. 

#print() 
#for metal in metals:
#    print(metal, densities[metal][1]) --> This is not working

print() 
for metal in metals:
    print('{0:>8} = {1:5.1f}'.format(metal,densities[metal]))#-->
#    gold =  19.3
#    lead =  11.4
#    iron =   7.8
#    zinc =   7.1

print() 
for metal, value in densities.items():
    print('{0:>8} = {1:5.1f}'.format(metal,value))#-->
#    iron =   7.8
#    gold =  19.3
#    zinc =   7.1
#    lead =  11.4    

print() 
for metal in metals:
    print('{} = {}'.format(metal,densities[metal]))

print() 
for metal, value in densities.items():
    print('{} = {}'.format(metal,value))

#-------------------------------------
# Task 08 - Combine counting loop and conditionals to filter out values
#------------------------------------- 
# Think about how to use if and else conditional logic and the for loop to scan a list to search for/print a particular value. E.g. only print metals that have a density value > 8.
    
print()
christmasBag = {'christmas jumper': 1, 'laptop': 2, 'kitchen towel': 3, 'country music cd': 4}
for presents in christmasBag:
    if presents == 'laptop':
        print('yay')
    else:
        print('dho!')
    

print()
christmasBag = {'chocolate bars': 1, 'dark chocolate drops': 2, 'ferrero rocher': 3, 'kinder bueno': 4}

print(presents)
for presents, item in christmasBag.items():
    print('the gift is', presents)
    print('the item is', item)
    if item >= 31:
        print('Thank you!')  
    else:
        print('dho!')        


#-------------------------------------
# Task 09 - Desing a sum function
#-------------------------------------
    
print()    
valueList = [3, 12, 9]
total = 0

for value in valueList:
    print('before adding', value, 'total is ', total)
    
    total = value + total
    
    print('after adding', value, 'total is ', total)
    
    print('TOTAL:' + str(total))   #-->
#before adding 3 total is 0
#after adding 3 total is 3
#before adding 12 total is 3
#after adding 12 total is 15
#before adding 9 total is 15
#after adding 9 total is 24
#TOTAL:24   | Please note that this result is given by the "for loop" thing  
        

#-------------------------------------
# Loop list with index
#-------------------------------------

print(list(range(3)))#--> [0, 1, 2]

print(len('ciao'))#--> 4
# The len() function returns the number of items in an object. In this case is returning 4 because there are 4 characters in the word "ciao".

#------------------------------------------
# Task 10 - Using a loop with index values
#------------------------------------------

values = [3, 12, 9]
for i in range(len(values)):
    values[i] = values[i] * 2
print(values)#-->[6, 24, 18]



#-----------------------------------------------
# Task 11 - Using a loop with the range function
#-----------------------------------------------
values = ['fabi', 'marta', 'andrea', 'piero', 'alex']
for i in range(len(values)):
    values[i] = values[i] * 3
print(values)#-->['fabifabifabi', 'martamartamarta', 'andreaandreaandrea', 'pieropieropiero', 'alexalexalex']
# Using a loop to get values contained in a dictionary, repeat it 3 times and keep doing this until the 

for i in range(3,10,2):
    print(i)
#this is giving the numbers from a range that goes from 3 to 10, jumping from 2 to 2 



#------------------------------------------
# Task 12 - Using a break in for loops
#------------------------------------------
print()    
the_list = [1,5,30,200,101,100,22]
for item in the_list:
    if item > 100:
        print ('stop at:',item)
        break
#--> stop at: 200    

print() 
for index in range(len(the_list)):
    if the_list[index] > 100:
        print('stop:', the_list[index], 'with index', index)
        break
#--> stop: 200 with index 3
        
###############################
  
print()      
colours = ['red', 'green', 'red', 'green', 'blue', 'green', 'green']
d = {}

for item in colours:
    
    if item not in d:
        d[item] = 1
        print(d, 'first time')
    else:
        d[item] = d[item] + 1
        print(d)
      
#------------------------------------------
# Task 13 - Using nested loops
#------------------------------------------   
print()
numbers = [1, 2, 3]
letters = ['A', 'B', 'C']
for numbers_items in numbers:#--> outer loop
    for letters_items in letters: #--> inner loop
        print(numbers_items, letters_items)#-->
#1 A
#1 B
#1 C
#2 A
#2 B
#2 C
#3 A
#3 B
#3 C
        
print()  
outer_vals = [1, 2, 3]
inner_vals = ['A', 'B', 'C','D']
d = {}
for oval in outer_vals:
    for ival in inner_vals:
        d[oval] = ival
        print(d)#-->
#{1: 'A'}
#{1: 'B'}
#{1: 'C'}
#{1: 'C', 2: 'A'}
#{1: 'C', 2: 'B'}
#{1: 'C', 2: 'C'}
#{1: 'C', 2: 'C', 3: 'A'}
#{1: 'C', 2: 'C', 3: 'B'}
#{1: 'C', 2: 'C', 3: 'C'}      
        
#------------------------------------------
# Task 14 - Multiplication table
#------------------------------------------ 

print()        
for i in range(1,7):
   for j in range(1,11):
      print('{0:>3}'.format(i * j), end='')
   print('\n')#-->
#  1  2  3  4  5  6  7  8  9 10
#
#  2  4  6  8 10 12 14 16 18 20
#
#  3  6  9 12 15 18 21 24 27 30
#
#  4  8 12 16 20 24 28 32 36 40
#
#  5 10 15 20 25 30 35 40 45 50
#
#  6 12 18 24 30 36 42 48 54 60   

#So here I'm creating a loop that is taking the first range of number that is going from 1 to 7 and I start picking the first number, such as 1. 
#Then I go to the second loop (1 to 11) and I start to do: 1 * 1, then 1 * 2, 1 * 3 until 10. 
# After that, on the second row I'll pick 2 and I start: 2*1, 2*2, 2*3 until 10. 
#I'll keep doing this until I'll finish the loop. The very last bit is 6*10 --> 60       