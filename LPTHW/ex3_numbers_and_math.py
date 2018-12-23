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

print("Hens", 25 + 30 / 6)
print("Roosters", 100 - 25 * 3 % 4)

print("Now I will count the eggs:")

print(3 + 2 + 1 - 5 + 4 % 2 - 1 / 4 + 6)

print("It is true that 3 + 2 < 5 - 7?")

print(3 + 2 < 5 - 7)

print("What is 3 + 2?", 3 + 2)
print("What is 5 - 7?", 5 - 7)

print("Oh, that's why it's False.")

print("How about some more.")

print("Is it greater?", 5 > -2)
print("Is it greater or equal?", 5 >= -2)
print("Is it less or equal?", 5 <= -2)
