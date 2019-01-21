#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 21 09:31:59 2019

@author: Fabiana
"""

import requests


endpoint = "http://api.openweathermap.org/data/2.5/weather"
city = input('Type the city: ')
payload = {"q": city, "appid":"ee78e9fbd81eb24eabf882b6506fcc1a"}
response = requests.get(endpoint, params=payload)
data = response.json()


def request():
#    print(data)
    print(response.url)
    weather1 = data['weather'][0]['description']
    tempMin = int(data['main']['temp_min']-273.15)
    tempMax = int(data['main']['temp_max']-273.15)
    print((weather1).title()+' in '+(city).title()+' with the minimum temperature set at: '+(str(tempMin))+'° C and the maximum at: '+(str(tempMax))+'° C')
    
request()


def weatherMessage():
    weatherConditions = data['weather'][0]['description']
    if weatherConditions == "light intensity drizzle":
        print('Tip: Take a raincoat ;)')
    elif weatherConditions == "clear sky":
        print('Tip: oh such a nice day. Why don\'t go to have a walk?')
    elif weatherConditions == "few clouds":
        print('Tip: you can leave you sunglasses at home ;)')
    elif weatherConditions == "scattered clouds":
        print('Tip: just a few clouds, tomorrow will be better.')
    elif weatherConditions == "broken clouds":
        print('Tip: don\'t be sad, it\'s not raining (yet)')
    elif weatherConditions == "shower rain":
        print('Tip: don\'t forget your umbrella')
    elif weatherConditions == "rain":
        print('Tip: dress you raincoat don\'t forget your umbrella and umbrella')
    elif weatherConditions == "thunderstorm":
        print('Tip: close all the windows and stay in bed')
    elif weatherConditions == "snow":
        print('Tip: ready to make your snowman?')
    elif weatherConditions == "mist":
        print('Tip: be careful and turn on the fog lights')
    else:
        print('Unexpected weather. Be careful.')        
        

weatherMessage()        
        
    