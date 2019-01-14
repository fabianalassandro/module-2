#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan  3 10:21:49 2019

@author: Fabiana
"""

from turtle import *
shape("turtle")
speed(10)
pencolor("white")
pensize(6)

Screen().bgcolor("turquoise") #To set the background color by picking the screen

def vshape():
    right(25)
    forward(50)
    backward(50)
    left(50)
    forward(50)
    backward(50)
    right(25)
#Here I'm creating a "V" shape that I'll use later on 
    
def snowflakeArm():
    for x in range(0,4): #This for loop will run 4 times creating a line (forward(30)) with 4 shapes (vshape())
        forward(30)
        vshape()
    backward(120) #This is to set the cursor going back to the start.
    
def snowflake():
    for x in range(0,6): #The loop will run 6 times creating 6 arms by using the snowflakeArm() function that I just created above
        snowflakeArm()
        right(60)# This makes the cursor turn 60° before starting the next arm

def snowflake10():
    for x in range(0,10):
        snowflakeArm()
        right(36)   
# Snowflake with 10 arms with a turn of 36 degrees  


def snowflake18():
    for x in range(0,18):
        snowflakeArm()
        right(20)
# Snowflake with 18 arms with a turn of 20 degrees     
        
    
        
        
        