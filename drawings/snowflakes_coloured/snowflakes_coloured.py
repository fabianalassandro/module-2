#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan  3 10:21:49 2019

@author: Fabiana
"""
########################################

# TURTLE DRAWINGS - COLOURED SNOWFLAKES

########################################


import random # To import the random function already existing and available in Python
from turtle import *
shape("turtle")
speed(10)
#pencolor("white") #To allow snowflakes in different colours
pensize(6)

Screen().bgcolor("turquoise") #To set the background color by picking the screen

colours = ["blue", "purple", "cyan", "white", "yellow", "green", "orange", "aquamarine", "plum", "dark orchid", "LimeGreen", "goldenrod", "lemon chiffon", "HotPink", "DarkKhaki", "DarkOrange"]

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
        color(random.choice(colours)) #This picks a random colour from the list "colours" created above
        snowflakeArm()
        right(60)# This makes the cursor turn 60° before starting the next arm
   