#no. of cars
cars = 100
#space available in a car
space_in_a_car = 4.0
#drivers available for driving
drivers = 30
#no. of passengers
passengers = 90
#cars not in action
cars_not_driven = cars - drivers
#cars used my drivers
cars_driven = drivers
#space that can be occupied
carpool_capacity = cars_driven * space_in_a_car
#no. of passengers in a car
average_passengers_per_car = passengers / cars_driven


print("There are", cars, "cars available.")
print("There are only", drivers, "drivers available.")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We have", passengers, "to carpool today.")
print("We need to put about", average_passengers_per_car, "in each car.")
