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

name=raw_input('Enter your name : ')
print ("Hi %s, Let us be friends!" % name);

"""
EXAMPLE OUTPUT:

bash-3.2$ python ex13_raw_input.py apple orange grapefruit cherry 
The script is called: ex13_raw_input.py
Your first variable is: apple
Your second variable is: orange
Your third variable is: grapefruit
Your fourth variable is: cherry
Enter your name : Mark
Hi Mark, Let us be friends!

"""