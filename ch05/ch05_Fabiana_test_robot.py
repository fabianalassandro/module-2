# -*- coding: utf-8 -*-
"""
Created on Wed Dec  5 12:08:02 2018

@author: fabia
"""

# -*- coding: utf-8 -*-
"""
Created on Wed Dec  5 12:01:00 2018

@author: fabia
"""

class Robot():
    def move(self):
        print('...move move move..')
        
class CleanRobot(Robot):
    def clean(self):
        print('I vacuum dust')
        return('I vacuum dust')
        
class CookRobot(Robot):
    def cook(self):
        print('I make rice')
        
c1po = CleanRobot()
c1po.clean()
c1po.move()

#print('Hello I\'m C1po and '+ str(c1po.clean()))

#bob = CookRobot()
#bob.cook()
