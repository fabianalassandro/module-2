# -*- coding: utf-8 -*-
"""
Created on Mon Dec  3 10:48:14 2018

@author: fabia
"""
#
#def convert_distance(miles):
#    kilometers = (miles * 8.0) / 5.0
#    print ("Converting distance in miles to kilometers:")
#    print ("Distance in miles:", miles)
#    print ("Distance in kilometers:", kilometers)



##################################
#TO DO LIS AS HOMEWORK
##################################

#celsius = float(input("What's the temperature in your city today?"))
#
#def convert_temperature(celsius):
#    fahrenheit = (celsius *  9.0 / 5.0 + 32)
#    kelvin = celsius + 273.15
#    print ("That's {} degrees in fahrenheit and {} degrees in kelvin".format(fahrenheit, kelvin))

##################################

def convert_temp ():
    centigrade = float(input("What temperature in Celsius do you want?"))
    kelvin = centigrade + 273.15
    fahrenheit = centigrade *9.0/5.0 + 32
    #print ("converting temperature in c to fahrenheit and kelvin ")
    #print ("the temperature in fahrenheit is {} and the temperature in kelvin is {} ".format(fahrenheit, kelvin))
    return fahrenheit, kelvin

conversion = convert_temp()
print(conversion)

f, k = convert_temp()
print("The temperature in fahrenheit is {} and the temperature in kelvin is {} ".format(f, k))



