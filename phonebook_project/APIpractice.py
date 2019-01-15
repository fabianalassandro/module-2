# -*- coding: utf-8 -*-
"""
Created on Mon Jan 14 10:06:31 2019

@author: mluci
"""

import sqlite3 
import json
import random
import requests
import string


conn = sqlite3.connect('phonebook.db') 

c = conn.cursor()

###Get API###
endpoint="https://api.postcodes.io/postcodes/"



def PeoplePostcodeAPI(): 
    c.execute('SELECT postcode FROM people')
    for row in c.fetchall():
        postcode = str(row).replace(' ', '')
        postcode = postcode.strip("'(),'")
        

        
        postcode_response = requests.get(endpoint + postcode)


        data_postcode = postcode_response.json()
        if data_postcode['status'] == 200:
            print(data_postcode['result']['longitude'])
            print(data_postcode['result']['latitude'])
                
PeoplePostcodeAPI()


        