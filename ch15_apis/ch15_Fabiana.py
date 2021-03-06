#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 10 14:00:48 2019

@author: Fabiana
"""

######################################

#CHAPTER 15 - APIs

######################################

#--------------------------------------------
# Task 1 - using Mailgun API to send an email
#--------------------------------------------

import requests #requests is a library that comes built-in with Python.
import config #to hide the api key. In the config.py file there is the api key stored in a variable.

def send_simple_message():
    return requests.post(
        "https://api.mailgun.net/v3/sandboxfd484f6c94514f2f965319b7da86eb41.mailgun.org/messages",
        auth=("api", config.api_key), #here I'm calling the API stored in a variable called "api_key" inside the file confif.py
        data={"from": "Fabiana <hellohello@fakedomain.com>",
              "to": ["fabianalassandro@gmail.com"],
              "subject": "I'm an interesting subject",
              "text": "Hello, how are you?"})

send_simple_message()    


#--------------------------------------------------
# Task 2 - get current weather information from API 
#--------------------------------------------------


#import requests #I commented this out becasue it's already at the top of this file.

endpoint = "http://api.openweathermap.org/data/2.5/weather"
payload = {"q": "Ranzo,IT", "units":"metric", "appid": config.api_key_weather}
response = requests.get(endpoint, params=payload)
print (response.url)#--> http://api.openweathermap.org/data/2.5/weather?q=Ranzo%2CIT&units=metric&appid=ee78e9fbd81eb24eabf882b6506fcc1a
print (response.status_code) #--> 200
print (response.headers["content-type"]) #--> application/json; charset=utf-8

print()
data = response.json()
print(type(data)) #--> <class 'dict'> So, json is a dictionary
print(data)

print()
print(response.text)







