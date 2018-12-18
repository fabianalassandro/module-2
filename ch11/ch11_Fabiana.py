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


#--------------------------------
# Task 2 - Computing triangular numbers
#--------------------------------

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
    
#--------------------------------
# Task 4 - Using the break statement in a while loop
#--------------------------------  
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
    
    

    
    