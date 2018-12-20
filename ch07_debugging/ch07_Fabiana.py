# -*- coding: utf-8 -*-
"""
Created on Tue Dec 11 09:27:35 2018

@author: fabia
"""

########################################

# CHAPTER 07 - DEBUGGING

#######################################


#How to debug
# Other than print() I can use other ways to check my code.

# . Breakpoints: I can use them to let run the file until that point and avoid to run the everything. To create a Breakpoint I need to click two times in the number of the line.
# . The blue buttons in the menu are used to debug. Let's start from the first one on the left:
#- Debug file: It runs the file until the breakpoint
#- Run corrent line: It runs the code just on the selected line 
#- Step into function or method of current line: to discover more about a function
#- Run until current function or method returns: to go to the next breakpoint
#- Stop debugging: to exit from the debugging mode



userInput = input('please give a number ')
result = userInput - 2

userInput = input('please give a number ')
print = (type(userInput))

userInput = input('please give a number ')
def simpleOperation(userInput):
    result = userInput - 2
    return result

result = simpleOperation(userInput)
print(result)

def nestedOperation():
    result = nestedOperation(userInput)
    result2 = result * 2
    return result2

result = simpleOperation(userInput)
result2 = nestedOperation()
print(result2)

