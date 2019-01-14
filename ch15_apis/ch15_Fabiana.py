#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 10 14:00:48 2019

@author: Fabiana
"""

#-------------------------------------
# Task 1 
#-------------------------------------

import requests #requests is a library that comes built-in with Python.

def send_simple_message():
    return requests.post(
        "https://api.mailgun.net/v3/sandboxfd484f6c94514f2f965319b7da86eb41.mailgun.org/messages",
        auth=("api", "api key"), #because I'm using github it's better don't put api key available for everyone
        data={"from": "Fabiana <ciaociao@gino.com>",
              "to": ["fabianalassandro@gmail.com"],
              "subject": "Hello Testa di Banana",
              "text": "Voglio la zuppina!"})

send_simple_message()    


#-------------------------------------
# Task 2
#-------------------------------------

#import requests

endpoint = "http://api.openweathermap.org/data/2.5/weather"
payload = {"q": "Ranzo,IT", "units":"metric", "appid":"ee78e9fbd81eb24eabf882b6506fcc1a"}
response = requests.get(endpoint, params=payload)
print (response.url)#--> http://api.openweathermap.org/data/2.5/weather?q=Ranzo%2CIT&units=metric&appid=ee78e9fbd81eb24eabf882b6506fcc1a
print (response.status_code) #--> 200
print (response.headers["content-type"]) #--> application/json; charset=utf-8

data = response.json()
print(type(data)) #--> <class 'dict'> So, json is a dictionary







