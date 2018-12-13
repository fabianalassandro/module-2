# -*- coding: utf-8 -*-
"""
Created on Mon Dec 10 10:24:27 2018

@author: jenni
"""

from ch06_jennifer import *

firstName = input('Hi!! What\'s your name? ').title()
starSign = input('Hey {}, what\'s your starsign? '.format(firstName)).title()



person = musicRobot(firstName, starSign)
person.musicType()


