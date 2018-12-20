# -*- coding: utf-8 -*-
"""
Created on Wed Dec 19 20:13:29 2018

@author: fabia
"""

from Shapes import Shape
from pylab import random as r
class MovingShape:
    def __init__(self,frame,shape,diameter):
        self.x = 0
        self.y = 0
        self.dx = delta-x#???
        self.dy = delta-y#???
        self.shape = shape
        self.diameter = diameter
        self.figure = Shape(shape,diameter)
    def goto(self,x,y):
        self.figure.goto(x,y)
        self.x = x
        self.y = y
    def moveTick(self):
        pass
class Square(MovingShape):
    def __init__(self,frame,diameter):
        MovingShape.__init__(self,frame,'square',diameter)

class Diamond(MovingShape):
    def __init__(self,frame,diameter):
        MovingShape.__init__(self,frame,'diamond',diameter)
class Circle(MovingShape):
    def __init__(self,frame,diameter):
        MovingShape.__init__(self,frame,'circle',diameter)