cars = 100
space_in_a_car = 4.0
drivers = 30
passengers = 90
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers / cars_driven

print("There are", cars, "cars available.")#--> 'There are', 100, 'cars available.'
print("There are only", drivers, "drivers available.")#-->'There are only', 30, 'drivers available.'
print("There will be", cars_not_driven, "empty cars today.")#-->'There will be', 70, 'empty cars today.'
print("We can trasport", carpool_capacity, "passengers today.")#-->'We can trasport', 120.0, 'passengers today.'
print("We have", passengers, "places to carpool today.")#-->'We have', 90, 'places to carpool today.'
print("We need to put about", average_passengers_per_car, "passengers in each car.")#-->'We need to put about', 3, 'passengers in each car.'
