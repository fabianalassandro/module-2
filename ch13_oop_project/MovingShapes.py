# -*- coding: utf-8 -*-
"""
Created on Wed Dec 19 20:13:29 2018

@author: fabia
"""

from Shapes import *
from pylab import random as r

class MovingShape:
    def __init__(self,frame,shape,diameter):
        self.x = 0
        self.y = 0
        
        self.dx = 5 + 10 * r()
        self.dy = 5 + 10 * r()
        
        self.shape = shape
        self.diameter = diameter
        self.figure = Shape(shape,diameter)
        
        self.goto(self.x, self.y)
        
        self.minx = self.diameter
        self.miny = self.diameter
        
        self.maxx = frame.width - self.diameter
        self.maxy = frame.height - self.diameter
        
        self.x = self.minx + (r()* (self.maxx - self.minx))
        self.y= self.miny + (r()* (self.maxy - self.miny))
        
    def goto(self,x,y):
        self.figure.goto(x,y)
  
    def moveTick(self):
        self.x += self.dx
        self.y += self.dy
        
        if self.x >= self.maxx:
            self.dx = self.dx * -1 
    
        if self.y >= self.maxy:
            self.dy=self.dy *-1
            
        if self.x <= self.minx:
            self.dx = self.dx * -1 
    
        if self.y <= self.miny:
            self.dy=self.dy *-1
            

        self.x= self.x +self.dx
        self.y= self.y+ self.dy 
        
        self.goto(self.x,self.y)
        
class Square(MovingShape):
    def __init__(self,frame,diameter):
        MovingShape.__init__(self,frame,'square',diameter)
        self.minx = self.diameter/2
        self.miny = self.diameter/2
        

class Diamond(MovingShape):
    def __init__(self,frame,diameter):
        MovingShape.__init__(self,frame,'diamond',diameter)
        self.diameter =2 *self.diameter
        self.minx = self.diameter/2
        self.miny = self.diameter/2
        
class Circle(MovingShape):
    def __init__(self,frame,diameter):
        MovingShape.__init__(self,frame,'circle',diameter)