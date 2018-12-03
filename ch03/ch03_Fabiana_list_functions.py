# -*- coding: utf-8 -*-
"""
Created on Mon Dec  3 15:47:14 2018

@author: fabia
"""

def convert_temp ():
    centigrade = int(input("What temperature in Celsius do you want?"))
    kelvin = centigrade + 273.15
    fahrenheit = centigrade *9.0/5.0 + 32
    return fahrenheit, kelvin

    print("The temperature in fahrenheit is {} and the temperature in kelvin is {} ".format(fahrenheit, kelvin))



def convert_temperature(celsius):
    fahrenheit = (celsius *  9.0 / 5.0 + 32)
    kelvin = celsius + 273.15
    print ("That's {} degrees in fahrenheit and {} degrees in kelvin".format(fahrenheit, kelvin))


def convert_distance(miles):
    kilometers = (miles * 8.0) / 5.0
    print ("Converting distance in miles to kilometers:")
    print ("Distance in miles:", miles)
    print ("Distance in kilometers:", kilometers)


def add_two_numbers_and_return_value():
    number1 = 1
    number2 = 2
    answer = number1 + number2 # answer = 3
    return answer # 3

def add_two_numbers_and_return_value(n1, n2):
    answer = n1+n2
    return answer


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