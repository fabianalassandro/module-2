#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan  9 09:54:15 2019

@author: Fabiana
"""

###################################

# CHAPTER 14 - DATABASES

###################################



#----------------------------------------
# Task 1 - Create a table and insert data
#----------------------------------------


#### SETTINGS
import sqlite3 #To import SQLite toolkit in this file

conn = sqlite3.connect('task1.db') #Here I'm connecting to a database that I'm creating now named: task1.db

c = conn.cursor() #This is to link my database to a low level pointer to find positions of data in each data table


#### CREATION OF A TABLE
def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS stuffToBuild(unix REAL, datestamp TEXT, keyword TEXT, value REAL)') #This is a function to create a table. In this way I can call the function later on just when I need to create a table.
# The code after execute, inside the parenthesis is SQL
# stuffToBuild is the db name
# unix, datestamp, keyword and value are the columns name of the table. 
# TEXT and REAL are the data types
    
    
#### HOW TO INSERT DATA INTO TABLES
def data_entry():
    c.execute("INSERT INTO stuffToBuild VALUES(142233222, '2018-01-01', 'python', 5)")
    # Here I'm inserting the values in the columns of the tables (unix, datestamp, keyword, value) created above.
    conn.commit() #This is to "publish" what I just did
#    c.close() #To close table if I finishe to work with it.
#    conn.close() #To close table and database if I finishe to work with it.
    
    
#### LET'S RUN THE FUNCTION TO CREATE THE TABLE
create_table()
data_entry()

    
#----------------------------------------
# Task 2 - Insert data using variables
#----------------------------------------

#import sqlite3 #This is not necessary in this specific case because I'm working on a file that has already imported sqlite3.
import time
import datetime
import random


#INSERTING DATA DYNAMICALLY (STREAM DATA)
def dynamic_data_entry():
    unix = time.time()
    date = str(datetime.datetime.fromtimestamp(unix).strftime('%Y-%m-%d %H:%M:%S'))
    keyword = 'Python'
    value = random.randrange(0, 10)
    c.execute('INSERT INTO stuffToBUild(unix, datestamp, keyword, value) VALUES (?, ?, ?, ?)',                  (unix, date, keyword, value))
    conn.commit()

#The one above is a function that is setting up variables and then inserting data in the stuffToBuild database
    
for i in range(10):
    dynamic_data_entry()
    time.sleep(1)# sleep is to slow the creation of values in order to get different time values in the database. Otherwise there's the risk to create the same values for every entry because computers are very fast.
    



#--------------------------------------------
# Task 3 - Read and select data from database
#--------------------------------------------

def read_from_db_all():
    c.execute('SELECT * FROM stuffToBuild WHERE value =8 ')
    for row in c.fetchall():
        print(row)
# Above I'm selectiong everything from the database named "stuffToBuild" that has the value 8
# fetchall is how we get (pull) the data after select it
#        
#read_from_db_all()
# PS: the values generated for unix could be approximated for excess once in the database table.


def read_from_db2():
    c.execute('SELECT * FROM stuffToBuild WHERE value =8 and unix > 1547033295.88268 and unix < 1547034080.43906 ')
    for row in c.fetchall():
        print(row[0]) # By using [0] I'm printing just the value in the first position, such as the unix one.

read_from_db2()        
        
c.close() #To close table if I finishe to work with it. It's better to use it at the end of the file, so at the very bottom of it.
conn.close() #To close table and database if I finishe to work with it. It's better to use it at the end of the file, so at the very bottom of it.        

 