# -*- coding: utf-8 -*-
"""
Created on Mon Dec  3 14:46:37 2018

@author: fabia
"""

""" =============================================================================
Task 5
What do you think the returned value will be if you don’t have a return line in your function? Copy the code from add_two_numbers_and_return_value() above into your my_arguments.py file and run the file. Then remove only the line return answer and see what happens.
 =============================================================================
"""

def add_two_numbers_and_return_value():
    number1 = 1
    number2 = 2
    answer = number1 + number2 # answer = 3
    return answer # 3

returned_value = add_two_numbers_and_return_value()

print (returned_value)
print (returned_value-5)