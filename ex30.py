# -*- coding: utf-8 -*-
# Exercise 30: Else and if

"""
NOTES:

1. An if-statement creates what is called a "branch" in the code. It's kind of 
like those choose your own adventure books where you are asked to turn to one page
if you make one choice, and another if you go a different direction. The if-statement
tells your script, "If this boolean expression is True, then run the code under it, 
otherwise skip it."

2. A colon at the end of a line is how you tell Python you are going to create a 
new "block" of code, and then indenting four spaces tells Python what lines of 
code are in that block. This is exactly the same thing you did when you made 
functions.

3. If it isn't indented, you will most likely create a Python error. Python 
expects you to indent something after you end a line with a : (colon).


"""
# assign 30 to variable people
people = 30
# assign 40 to variable cars
cars = 40
# assign 15 to the variable trucks
trucks = 15
# assign 35 to buses
buses = 35

# if cars are greater than people
if cars > people:
    # print "We should take the cars."
    print "We should take the cars."
# (else) if cars are less than people
elif cars < people:
    # print "We should not take the cars."
    print "We should not take the cars."
# if cars are equal to people
else:
    print "We can't decide."
    
if trucks > cars:
    print "That's too many trucks."
elif trucks < cars:
    print "Maybe we could take the trucks."
else:
    print "We still can't decide."
    
if people > trucks:
    print "Alright, let's just take the trucks."
else:
    print "Fine, let's stay home then."

# if buses are more than cars    
if buses > cars:
    # print "That's too many buses."
    print "That's too many buses."
# if buses are less than cars    
elif buses < cars:
    # print "Maybe we could take the buses."
    print "Maybe we could take the buses."
# if buses are equal to cars    
else:
    # print "We still can't decide."
    print "We still can't decide."

# if people are more than buses
if people > buses:
    # print "Alright, let's just take the buses."
    print "Alright, let's just take the buses."
# if people are less than buses
else:
    # print "Fine, let's stay home then."
    print "Fine, let's stay home then."

# if people are more than cars (and) but less than buses
if people > cars and people < buses:
    # print "There are many Buses but few cars."
    print "There are many Buses but few cars."
# if people are less than cars but more than buses
elif people < cars and people > buses:
    # print "There are many cars but few busses."
    print "There are many cars but few busses."
# if people are more than cars and buses
elif people > cars and people > buses:
    # print "There are few buses and cars."
    print "There are few busses and cars."
# if people are less than cars and buses    
else:
    # print "There are many busses and cars."
    print "There are many buses and cars."
    
"""
EXAMPLE OUTPUT:

bash-3.2$ python ex30.py
We should take the cars.
Maybe we could take the trucks.
Alright, let's just take the trucks.
Maybe we could take the buses.
Fine, let's stay home then.
There are many buses and cars

ADDITIONAL NOTES:

If multiple elif blocks are True, then Python starts and the top runs the first 
block that's True, so it will run only the first one.


"""