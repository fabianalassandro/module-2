# -*- coding: utf-8 -*-
"""
Created on Tue Dec 11 13:54:32 2018

@author: fabia
"""

def DataBundlePurchase(truePasscode, balance):
    if passwordCheck(truePasscode) == True:
        transactionRequest = transaction()
        if transactionRequest == '1':
            print('Your balance is {}'.format(balance))
            return ('Your balance is {}'.format(balance))
        elif transactionRequest == '2':
             buyData(balance)
             return 'Buy data' 
        else:
            print('Your balance is not sufficient:{}'.format(balance))
            return ('Your balance is not sufficient:{}'.format(balance))
    else:
        return ('Wait 10 minutes and try again.')
        
    
def passwordCheck(truePasscode):
    attempt1 = input('Insert your password: ')
    if attempt1 != truePasscode:
        attempt2 = input('Please try to type your password again - 2 of 3 attempts: ')
        
        if attempt2 != truePasscode:
            attempt3 = input('Please try for the last time - 3 of 3 attempts: \n')
            
            if attempt3 != truePasscode:
                print ('Sorry you tried too many times.')
                return 'User tried more than 3 times'
            else:
                print('Third attempt successfully')
                return True
        else: 
            print('2nd attempt successfully, ')
            return True
    else: 
        print('1nd attempt successfully, ')
        return True
# 
    
def checkBalance(balance):
    if balance > 0:
        return True
    else:
        return False
    
def transaction():
    transactionRequest = input('If you want to check your credit balance type 1. If you want to purchase a data bundle type 2: ')
    return transactionRequest

def MultipleOfFive(amount):
    return amount == int(amount / 5.0) * 5

def buyData(balance):
    maxDataPurchase = 100.00
    print ('\n Please type the phone number you need to top-up: ')
    number1 = input()
    print ('\n Please re-enter the phone number')
    number2 = input()
    
    if number1 == number2:
        print ('Cool! Now you can top-up your number.\n Maximum Top-up is 100 GPB.\n You can top-up just with multiple of 5.')
        amount = float(input('How much do you want to top-up? Remember that has to be a multiple of 5. '))
    
        if amount > maxDataPurchase:
            print ('Amount exceeds maximum top-up allowed.')
            print ('Request denied')
            return ('Request denied. Sorry the maximum top-up is 100 GPB')
        
        elif amount > balance:
            print ('Amount exceeds balance available.')
            print ('Request denied')
            return ('Request denied. Sorry your balance is not enough.')
        
        elif MultipleOfFive(amount):
            print ('Transaction authorised.')
            print ('The new account balance is', round(balance - amount, 2), 'GPB')
            return ('You\'re top-up is: ', amount, '. Your new account balance')
        
        else:
            print ('Amount is not a multiple of 5.')
            print ('Request denied.')
            return 'Top-up request: denied.'
        
    else:
        print ('Error. the two numbers entered are different.')
        print ('Transaction cancelled.')
        return 'Top-up request: denied'        
   
        
           
        
    