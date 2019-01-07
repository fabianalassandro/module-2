# -*- coding: utf-8 -*-
"""
Created on Wed Dec 19 20:25:46 2018

@author: fabia
"""

from MovingShapes import *
from Shapes import Frame

frame = Frame()
shape1 = Square(frame,100)
shape2 = Circle(frame, 120)

for i in range(100):
    shape1.moveTick()
    
for i in range(100):
    shape2.moveTick()    