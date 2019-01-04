#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan  3 10:21:49 2019

@author: Fabiana
"""
########################################

# TURTLE DRAWINGS - EX. 4 SNOWSTORM

########################################

#In this exercise I use the variable "size" that I'm going to add in each functions.
# "size" variable is used as placeholder in order to replace the size with a random size. 
# The random size is created by the last function.


import random # To import the random function already existing and available in Python
from turtle import *
shape("turtle")
speed(10)
#pencolor("white") #To allow snowflakes in different colours
pensize(6)

Screen().bgcolor("turquoise") #To set the background color by picking the screen

colours = ["blue", "purple", "cyan", "white", "yellow", "green", "orange", "aquamarine", "plum", "dark orchid", "LimeGreen", "goldenrod", "lemon chiffon", "HotPink", "DarkKhaki", "DarkOrange"]

def vshape(size):
    right(25)
    forward(size)
    backward(size)
    left(50)
    forward(size)
    backward(size)
    right(25)
#Here I'm creating a "V" shape that I'll use later on 
    
def snowflakeArm(size):
    for x in range(0,4): #This for loop will run 4 times creating a line (forward(size)) with 4 shapes (vshape(size))
        forward(size)
        vshape(size)
    backward(size*4) #This is to set the cursor going back to the start.
    
def snowflake(size):
    for x in range(0,6): #The loop will run 6 times creating 6 arms by using the snowflakeArm(size) function that I just created above
        color(random.choice(colours)) #This picks a random colour from the list "colours" created above
        snowflakeArm(size)
        right(60)# This makes the cursor turn 60° before starting the next arm

for i in range(0,10): # Here I'm setting the number of snowflakes
    size = random.randint(5,30)  # This is setting the random number for the size
    x = random.randint(-300,400) # This is setting the random numbers for the coordinates
    y = random.randint(-300,400) # This is setting the random numbers for the coordinates
    penup()
    goto(x,y) 
    pendown()
    snowflake(size)
    