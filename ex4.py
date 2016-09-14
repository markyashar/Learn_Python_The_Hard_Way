# Exercise 4: Variables and Names

# The total number of cars
cars = 100
# The amount of space in a car
space_in_a_car = 4  # Recall that the "_" in space_in_a_car is called and underscore character.
# The total number of drivers
drivers = 30
# The total number of drivers
passengers = 90
# The cars not driven are the total number of cars minus the total number of drivers
cars_not_driven = cars - drivers
# The number of cars driven are the same as the total number of drivers
cars_driven = drivers
# The carpool capacity is the number of cars driven multiplied by the amount of space in the car
carpool_capacity = cars_driven * space_in_a_car
# The average number of passengers per car are the total number of passengers divided by total # of cards driven
average_passengers_per_car = passengers / cars_driven


print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."

"""
EXAMPLE OUTPUT:

bash-3.2$ python ex4.py
There are 100 cars available.
There are only 30 drivers available.
There will be 70 empty cars today.
We can transport 120.0 people today.
We have 90 to carpool today.
We need to put about 3 in each car.

STUDY DRILLS:

1. When I wrote this program the first time I had a mistake, and Python told me about it like this:

Traceback (most recent call last):
  File "ex4.py", line 8, in <module>
    average_passengers_per_car = car_pool_capacity / passenger
NameError: name 'car_pool_capacity' is not defined

The name of the variable is 'carpool_capaciy', not 'car_pool_capcity', and this
is what lead fo this error message.

2. I used 4.0 for space_in_a_car, but is that necessary? What happens if it's just 4?
In this case, it doesn't make a difference. If we use space_in_a_car = 4, we get 
carpool_capaciy = 120 rather than 120.0 .

3. Remember that 4.0 is a floating point number. It's just a number with a decimal point, and you need 4.0 instead of
just 4 so that it is floating point.

4. Write comments above each of the variable assignments.

5. Make sure you know what = is called (equals) and that it's making names for things.

6. Remember that _ is an underscore character.

7. Try running python from the Terminal as a calculator like you did before and use variable names to do your 
calculations. Popular variable names are also i, x, and j.

i=4.3

x =9.5

j =3.3

i-x%j/i
Out[7]: 3.6255813953488367

ADDITIONAL NOTES:

The = (single-equal) assigns the value on the right to a variable on the left. 
The == (double-equal) tests if two things have the same value.

"""