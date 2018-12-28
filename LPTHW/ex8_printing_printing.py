formatter = "{} {} {} {} {}"

print(formatter.format(1,2,3,4,5))
print(formatter.format("one", "two", "three", "four", "five"))
print(formatter.format(True, False, False, True, True))
print(formatter.format(formatter, formatter, formatter, formatter, formatter))
print(formatter.format(
    "Try your",
    "Own text here",
    "Maybe a poem",
    "Or a song about fear",
    "test"
))

#I need to have the same amount of "elements" contained in the formatter. So if in formatter I have 5 curly brackets, then I need 5 elements everytime I'm using the variable formatter 
