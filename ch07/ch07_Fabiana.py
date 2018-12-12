# -*- coding: utf-8 -*-
"""
Created on Tue Dec 11 09:27:35 2018

@author: fabia
"""

#userInput = input('please give a number ')
#result = userInput - 2

userInput = input('please give a number ')
print = (type(userInput))

userInput = input('please give a number ')
def simpleOperation(userInput):
    result = userInput - 2
    return result

def nestedOperation():
    result = nestedOperation(userInput)
    result2 = result * 2
    return result2

result = simpleOperation(userInput)
result = nestedOperation()

print(result2)