# -*- coding: utf-8 -*-
"""
Created on Tue Dec 18 18:30:22 2018

@author: fabia
"""

from Shapes import Shape, Frame
import time

frame = Frame()
s1 = Shape('square',100)
s1.goto(200,100)
#frame.close()

x = 0
y = 0

for i in range(100):
    s1.goto(x,y)
    x = x + 5
    y = x + 5
    time.sleep(0.01)#I'm importing the time 
    
    
