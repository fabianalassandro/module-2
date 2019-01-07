#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan  2 14:57:44 2019

@author: Fabiana
"""

from MovingShapes import *
frame = Frame()
numshapes = 3
shapes = []
size = 60
for i in range (numshapes):
    shapes.append(Square(frame,size))
    shapes.append(Diamond(frame,size))
    shapes.append(Circle(frame,size))

    
for i in range(300):
    for shape in shapes:
        shape.moveTick()