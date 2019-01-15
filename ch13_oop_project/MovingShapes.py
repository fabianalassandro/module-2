# -*- coding: utf-8 -*-
"""
Created on Wed Dec 19 20:13:29 2018

@author: fabia
"""

from Shapes import *
from pylab import random as r

class MovingShape:
    def __init__(self,frame,shape,diameter):
        self.shape = shape
        self.diameter = diameter
        self.figure = Shape(shape,diameter)
        
        self.minx = (frame.width*0.01) + self.diameter / 2
        self.miny = (frame.height*0.01) + self.diameter / 2
        
        self.maxx = (frame.width*0.985) - self.diameter / 2
        self.maxy = (frame.height*0.985) - self.diameter / 2
        
        self.x = self.minx + (r()* (self.maxx - self.minx))
        self.y= self.miny + (r()* (self.maxy - self.miny))
        
        self.dx = 5 + 10 * r()
        self.dy = 5 + 10 * r()
         
        self.goto(self.x, self.y)
        
    
    def startMove(self):
       if r() > 0.5: #07/07
           self.dx = 5 + 10*r() #07/06
           self.dy = 5 + 10*r() #07/06
       else: #07/07
           self.dx = -(5 + 10*r()) #07/06
           self.dy = -(5 + 10*r()) #07/06     
     
        
    def goto(self,x,y):
        self.figure.goto(x,y)
        
        
    
    def moveTick(self):  
        if self.x >= self.maxx or self.x <=self.minx:
            self.dx = self.dx * -1 
    
        if self.y >= self.maxy or self.y <=self.miny:
            self.dy=self.dy *-1
           
        self.x= self.x +self.dx
        self.y= self.y+ self.dy 
        
        self.goto(self.x,self.y)
        
        
        
class Square(MovingShape):
    def __init__(self,frame,diameter):
        MovingShape.__init__(self,frame,'square',diameter)
      
        
class Diamond(MovingShape):
    def __init__(self,frame,diameter):
        MovingShape.__init__(self,frame,'diamond',diameter)
#        self.diameter = (2*(diameter**2)**0.5) # this is to calculate the diameter of a diamond that is longer than a square diameter.
        self.minx = (frame.width*0.009) + self.diameter / 2
        self.miny = (frame.height*0.009) + self.diameter / 2
        
        self.maxx = (frame.width*0.98) - self.diameter / 2
        self.maxy = (frame.height*0.965) - self.diameter / 2
       
        
class Circle(MovingShape):
    def __init__(self,frame,diameter):
        MovingShape.__init__(self,frame,'circle',diameter)
 

       
# Change colour and size by moving - take a look at the code fo beginners book      