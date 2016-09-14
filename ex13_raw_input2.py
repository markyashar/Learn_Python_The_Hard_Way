# -*- coding: utf-8 -*-


# -*- coding: utf-8 -*-
# Exercise 13: Parameters, Unpacking, Variables
from sys import argv    # argv is the "argument variable". This variable holds
                        # holds the arguments you pass to your Python scrtip
                        # when you run it.
# Here, we "unpack" argv so that, rather than holding all the arguments, it gets
# assigned to 4 variables we can work with: 'script', 'first', 'second', and 'third'.
# It says "Take whatever is in argv, unpack it, and assign it to all of these variables
# on the left in order."

# Also, combine 'raw_input' with 'argv' to make a script that gets more input 
# from a user. Don't over think it. Just use argv to get something, and raw_input 
# to get something else from the user.
# script, first, second, third, fourth = argv

script, first, second, third, fourth = argv

print "The script is called:", script
print "Your first variable is:", first
print "Your second variable is:", second
print "Your third variable is:", third
print "Your fourth variable is:", fourth

fifth=raw_input("On which days are you going to work next week?")
print "Next week, I'm going to work on %s, %s, %s, %s, %s." % (first, second, third, fourth, fifth)

"""
EXAMPLE OUTPUT:

bash-3.2$ python ex13_raw_input2.py Monday Tuesday Wednesday Thursday
The script is called: ex13_raw_input2.py
Your first variable is: Monday
Your second variable is: Tuesday
Your third variable is: Wednesday
Your fourth variable is: Thursday
On which days are you going to work next week? Friday
Next week, I'm going to work on Monday, Tuesday, Wednesday, Thursday,  Friday.

"""
