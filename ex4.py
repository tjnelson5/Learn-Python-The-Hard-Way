# cars available
cars = 100

# number of seats in each car
space_in_a_car = 4

# number of drivers available
drivers = 30

# number of people hoping to carpool
passengers = 90

# number of empty cars
cars_not_driven = cars - drivers

# number of cars to be driven
cars_driven = drivers

# total number of people who can carpool
carpool_capacity = cars_driven * space_in_a_car

# number of people per car 
average_passengers_per_car = passengers / cars_driven

print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."
