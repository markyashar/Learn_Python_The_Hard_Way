# -*- coding: utf-8 -*-
# Exercise 13: Parameters, Unpacking, Variables
from sys import argv    # argv is the "argument variable". This variable holds
                        # holds the arguments you pass to your Python scrtip
                        # when you run it.
# Here, we "unpack" argv so that, rather than holding all the arguments, it gets
# assigned to 4 variables we can work with: 'script', 'first', 'second', and 'third'.
# It says "Take whatever is in argv, unpack it, and assign it to all of these variables
# on the left in order."
script, first, second, third = argv

print "The script is called:", script
print "Your first variable is:", first
print "Your second variable is:", second
print "Your third variable is:", third

"""
EXAMPLE OUTPUT:

python ex13.py first 2nd 3rd
The script is called: ex13.py
Your first variable is: first
Your second variable is: 2nd
Your third variable is: 3rd

bash-3.2$ python ex13.py stuff things that
The script is called: ex13.py
Your first variable is: stuff
Your second variable is: things
Your third variable is: that

bash-3.2$ python ex13.py apple orange grapefruit
The script is called: ex13.py
Your first variable is: apple
Your second variable is: orange
Your third variable is: grapefruit

ADDITIONAL COMMENTS:

* We actually replace 'first', '2nd', and '3rd' with any three things we want.

* If you do not run it correctly, then you will get an error like this:

$ python ex13.py first 2nd

Traceback (most recent call last):
  File "ex13.py", line 3, in <module>
    script, first, second, third = argv
ValueError: need more than 3 values to unpack

This happens when you do not put enough arguments on the command when you run 
it (in this case just first 2nd). Notice when we you ran it you gave it 'first
2nd',  which caused it to give an error about "need more than 3 values to unpack" 
telling you that you didn't give it enough parameters.
"""