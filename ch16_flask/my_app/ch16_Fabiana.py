#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 16 09:39:16 2019

@author: Fabiana
"""

#########################################################

# CHAPTER 16 - FLASK, AND USING PYTHON AND HTML TOGETHER

########################################################


#-----------------------------
# Task 1 - Create my app
#-----------------------------


from flask import Flask, render_template, request

app = Flask("MyApp")

@app.route("/")
def hello():
    return "<h1>Hello World</h1> <ul><li><a href=\"/morning\">Good Morning</a></li></ul><a href=\"style.css\"></a>"

@app.route("/morning")
def morning():
    return "<h1>Good Morning</h1>"

@app.route("/afternoon")
def afternoon():
    return "<h1>Good Afternoon</h1>"

@app.route("/night")
def night():
    return "<h1>Good Night</h1>"



#How to import a HTML file    
@app.route("/blabla")
def homepage():
    return render_template("/index.html")

@app.route("/hello/<name>")
def helloFile(name):
    return render_template("hello.html", name=name)

# CREATE A FORM


    
@app.route("/about")
def about():
    return render_template("about.html", title="about")

@app.route("/confirmation", methods=["POST"])
def confirmation():
    form_data = request.form
    email = form_data["email"] #what I put in the [] is the attribute name I added in the form in about.hml 
    result = "All OK"
    return render_template("confirmation.html", title="Form confirmation", **locals())#--> ** means that I can put as many arguments as I like without pre-set them.

app.run(debug=True) 

#When we run a code like this:

#rom flask import Flask, render_template
#
#app = Flask("MyApp")
#
#@app.route("/")
#def hello():
#    return "<h1>Hello World</h1>"
#app.run(debug=True) 

#This is what we get:
#--> Serving Flask app "MyApp" (lazy loading)
# * Environment: production
#   WARNING: Do not use the development server in a production environment.
#   Use a production WSGI server instead.
# * Debug mode: on
# * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
# * Restarting with stat
# * Debugger is active!
# * Debugger PIN: 263-454-907
#127.0.0.1 - - [16/Jan/2019 09:45:00] "GET / HTTP/1.1" 200 -
#127.0.0.1 - - [16/Jan/2019 09:45:00] "GET /favicon.ico HTTP/1.1" 404 -

#What I need is the URL created, such as: http://127.0.0.1:5000/. If I copy and paste this URL in the browser I will finally see "Hello World" on a blank page.

#Second step: if I try to add some HTML inside the "" after the return I will see my changes 


#---------------------------------
# Task 2 - Create different pages
#---------------------------------



 