name = 'Zed A. Shaw'
age = 35 # not a lie
height = 74 #inches
weight = 180 #lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

#print(f"Let's talk about {my_name}.") # | Previous way to use format
print("Let's talk about {}").format(name)
print("He's {} inches tall.").format(height)
print("He's {} pounds heavy.").format(weight)
print("Actually that's not too heavy.")
print("He's got {} eyes and {} hair.").format(eyes, hair)
print("His teeth are usually {} depending on the coffee.").format(teeth)

total = age + height + weight
print("If I add {}, {}, and {} I get {}.").format(age, height, weight, total)


#Convert measures from inches to centimeters
print("\n")
height = int(round(height * 2.54))# Here I'm rounding the result and then transforming it in an integer
weight = int(round(weight * 0.453592))

print("Let's talk about {}").format(name)
print("He's {} cm tall.").format(height)
print("He's {} kg heavy.").format(weight)
print("Actually that's not too heavy.")
print("He's got {} eyes and {} hair.").format(eyes, hair)
print("His teeth are usually {} depending on the coffee.").format(teeth)

total = age + height + weight
print("If I add {}, {}, and {} I get {}.").format(age, height, weight, total)
