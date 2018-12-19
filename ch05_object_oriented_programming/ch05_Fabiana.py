# -*- coding: utf-8 -*-
"""
Created on Wed Dec  5 09:12:52 2018

@author: fabia
"""

class Customer(object):
    """
    A customer of ABC Bank with a checking account. Customers have the following properties:
    Attributes:
        name: A string representing the customer's name.
        balance: A float tracking the current balance of the customer's account.
    """
    
    def __init__(self, name, balance=0.0):
        """Return a Customer object whose name is *name* and starting balance is *balance*."""
        self.name = name
        self.balance = balance
        
    def withdraw(self, amount):
        """Return the balance remaining after withdrawing *amount* dollars."""
        if amount > self.balance:
            raise RuntimeError('Amount greater than available balance.')
        self.balance -= amount
        return self.balance
    
    def deposit(self, amount):
        """Return the balance remaining after depositing        *amount* dollars."""
        self.balance += amount
        return self.balance
    
    def __str__(self):
        """Return a sentence (string) with the number of the balance converted in a string -take a look at the second string- in order to place the information in the sentence"""
        return ("Customer " + self.name + " has a balance of " + str(self.balance) + "."  )    
        
jason = Customer('Jason Taylor', 1000.0)
fabiana = Customer('Fabiana Lassandro', 2000.0)
print(fabiana.balance)   
print(jason) 

  