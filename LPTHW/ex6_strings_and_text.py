types_of_people = 10
x = "There are {} types of people.".format(types_of_people)

binary = "binary"
do_not = "don't"
y = "Those who know {} and those who {}.".format(binary, do_not)

print(x)#--> There are 10 types of people.
print(y)#--> Those who know binary and those who don't.

print("I said: {}").format(x)#--> I said: There are 10 types of people.
print("I also said: {}").format(y)#--> I also said: Those who know binary and those who don't.

hilarious = False
joke_evaluation = "Isn't that joke so funny?! {}"

print (joke_evaluation.format(hilarious))#--> Isn't that joke so funny?! False
w = "This is the left side of..."
e = "a string with a right side."

print (w + e)#--> This is the left side of...a string with a right side.
# By using + I can add a string to another one

#By using format I can insert variables in strings. A variable can be just a word or an entire strings, formatted as wellself.
