# -*- coding: utf-8 -*-
"""
Created on Thu Nov 29 13:58:35 2018

@author: fabia
"""

###########################################

#CHAPTER 03 - FUNCTIONS & IMPORTING MODULES

###########################################


#---------------------------------------
#Task 02 - MY FIRST FUNCTION
#---------------------------------------

def hello_world():
    print ("Hello World!")#On the console there's nothing because I'm not calling the function. To call a function is enough type: hello_world() - give it a try
    
def name_surname():
    print ("What's your name?")
    name = input()#I use an input when I need to collect data from the user. 
# Here I'm creating the variable "name" to reuse tha data collected from there in the formatted string below.  
    print ("My name is {}".format(name))

name_surname()#-->What's your name? | To trigger a function I need to call it. In order to call it I need to type the name of the function followe by (). In this case: name_surname() 
 
print()   
def addition():
    print (4)
    
addition()#--> 4
#Here I'm just using a function to print the number 4. Of course, it would be enough print directly print(4), but it's just an example to show how a function works.



#----------------------------------------------
# Task 04 - Add two numbers ( and Return value)
#----------------------------------------------

# Task 04.1 - Add two numbers
print()
number1 = 1
number2 = 2

def add_two_numbers(number, anotherNumber):
    
    answer = number + anotherNumber
    print ("{} plus {} is {}".format(number, anotherNumber, answer))
    
add_two_numbers (number1, number2)#--> 1 plus 2 is 3 | by calling this function I'm printing what's on the print() function above.

#In order to build a function - that is basically a reusable calculation or let's say operation - I need to build something abstract by using words instead of real values. Then when I want to use a function for a real operation what I need to do is:
# 1. Call the function
# 2. insert in the variables the values that I want to calculate



# Task 04.2 - How to use RETURN value
print()
def add_two_numbers_and_return_value():
    number1 = 1
    number2 = 2
    answer = number1 + number2
    return answer
returned_value = add_two_numbers_and_return_value()
print(returned_value)#--> 3
print(returned_value - 5)#--> -2

print()
def add_two_numbers_and_return_value(n1, n2):
    return n1+n2
Result1 = add_two_numbers_and_return_value(4, 5)
print(Result1)#--> 9

def add_two_numbers_and_return_value(n1, n2):
    answer = n1+n2
    return answer
Result1 = add_two_numbers_and_return_value(6, 7)
print(Result1)#--> 13

#Return value is really important! I need to use it in order to save a value in the computer. Print() function is to show what I'm doing with on the console, that's it, while Return is let me save the result in order to reuse it later on and something with that.


#---------------------------------------
# Task 05 - Temperature Conversion
#---------------------------------------
print()
def convert_temp ():
    centigrade = float(input("What temperature in Celsius do you want?"))
    kelvin = centigrade + 273.15
    fahrenheit = centigrade *9.0/5.0 + 32
    print ("Converting temperature in C to Fahrenheit and Kelvin in progress... ")
    print ("The temperature in Fahrenheit is: {} and the temperature in Kelvin is: {} ".format(fahrenheit, kelvin))
    return fahrenheit, kelvin# By using , I can return the result of both the variables: fahrenheit, kelvin

conversion = convert_temp()
print(conversion)#--> (39.2, 277.15) | I need to assign a variable to the function convert_temp in order to let me print what stored in the Return value. 
#PS: note that I'm doing this out of the function.
#To show a function in the console is enough to call it like this: convert_temp(), but in order to use the result to do something I have to assign a variable to the function and then print it.

f, k = convert_temp()
print("The temperature in Fahrenheit is {} and the temperature in Kelvin is {} ".format(f, k))

#Here I assign two variables in order to save the two results returned on top in two different variables and reuse the separately. This is much more convenient if we need to do some calculation with them. 



#---------------------------------------
# OTHER FUNCTIONS TO IMPORT IN THE FILE
#---------------------------------------


def hello_world_3args(d, e, f): 
    print ("{} {} {}".format(d, e, f))
    
a1 = 'hello'
b1 = 'world'
c1 = "!"

a2 = 'love'
b2 = 'coding'
c2 = "!"

hello_world_3args(a1, b1, c1)
hello_world_3args(a2, b2, c2)


#Imagine "d" as "placeholder1", "e" as "placeholder 2" and "f" as "placeholder3.
#In print I set how it should look like the sentence. I have to add a pair of curly brackets for every placeholders, so in this case 3 pairs of curly brackets.

#To delete or add a space in the sentence I have to add it or delete it between the 2 pairs curly brackets in the print() function.

print()
def convert_temperature(celsius):
    fahrenheit = (celsius *  9.0 / 5.0 + 32)
    kelvin = celsius + 273.15
    print ("That's {} degrees in fahrenheit and {} degrees in kelvin".format(fahrenheit, kelvin))


print()
def convert_distance(miles):
    kilometers = (miles * 8.0) / 5.0
    print ("Converting distance in miles to kilometers:")
    print ("Distance in miles:", miles)
    print ("Distance in kilometers:", kilometers)


print()
def add_two_numbers_and_return_value():
    number1 = 1
    number2 = 2
    answer = number1 + number2 # answer = 3
    return answer # 3


print()
def add_two_numbers_and_return_value(n1, n2):
    answer = n1+n2
    return answer


print()
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print ("You have {} cheeses!".format(cheese_count))
    print ("You have {} boxes of crackers!".format(boxes_of_crackers))
    print ("Man that's enough for a party!")
    print ("Get a blanket.\n")
    
# ok, that *args is actually pointless, we can just do this
def print_two_again(arg1, arg2):
    print ("arg1: {}, arg2: {}".format(arg1, arg2))

# this just takes one argument
def print_one(arg1):
    print ("arg1: {}".format(arg1))

# this one takes no arguments
def print_none():
    print ("I got nothin'.")