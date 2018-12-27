# + plus --> addition
# - minus --> subtraction
# / slash | no priority on calculations
# * asterisk | has priority on calculations
# % percent | has priority on calculations
# < less-than --> this will give a False or True result
# > greater-than --> this will give a False or True result
# <= less-than-equal --> this will give a False or True result
# >= greater-than-equal --> this will give a False or True result

print("I will now count my chickens:")

print("Hens", 25 + 30 / 6)#--> 'Hens', 30
#Before the division, then + 25

print("Roosters", 100 - 25 * 3 % 4)#--> 'Roosters', 97
#Before the moltiplication (25*3=75), then the modulo operation (75%4=3), finally 100-3= 97

print("Now I will count the eggs:")#-->Now I will count the eggs:

print(3 + 2 + 1 - 5 + 4 % 2 - 1 / 4 + 6)#--> 7

print("It is true that 3 + 2 < 5 - 7?")#-->It is true that 3 + 2 < 5 - 7?

print(3 + 2 < 5 - 7)#--> False
#By using <, >, <=, => the result is True or False
print("What is 3 + 2?", 3 + 2)#-->'What is 3 + 2?', 5
print("What is 5 - 7?", 5 - 7)#-->'What is 5 - 7?', -2

print("Oh, that's why it's False.")

print("How about some more.")

print("Is it greater?", 5 > -2)
print("Is it greater or equal?", 5 >= -2)
print("Is it less or equal?", 5 <= -2)
