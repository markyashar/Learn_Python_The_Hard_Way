# -*- coding: utf-8 -*-
# Exercise 21: Functions Can Returen Something
"""
We've been use the '=' character to name variables and set them to numbers or
strings. Here, we demonstrate how to use '=' and a new Python word 'return'
to set variables to be a value from a function. 
"""

def add(a,b):
    print "ADDING %d + %d" % (a, b)
    return a + b
    
def subtract(a,b):
    print "SUBTRACTING %d - %d" % (a, b)
    return a - b

def multiply(a,b):
    print "MULTIPLYING %d * %d" % (a, b)
    return a * b
    
def divide(a, b):
    print "DIVIDING %d / %d" % (a, b)
    return a / b
    
print "Let's do some math with just functions!"
    
age = add(30, 5)
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)

print "Age: %d, Height: %d, Weight: %d, IQ: %d" % (age, height, weight, iq)

# A puzzle for the extra credit, type it in anyway.
print "Here is a puzzle."

what = add(age, subtract(height, multiply(weight, divide(iq, 2))))

print "That becomes: ", what, "Can you do it by hand?"

# Switch the order of multiply and divide
what_switch = add(age, subtract(height, divide(weight, multiply(iq,2))))

print "That becomes: ", what_switch, "Can you do that by hand?"

# A different puzzle
print "Here is another puzzle."
puzzle = multiply(weight, add(age,divide(add(iq,3),height)))
print "That now becomes:", puzzle

# New puzzle.

print "Here's a new puzzle for you:"

# Write a simple formula and the function again

height = 80
weight =120
iq=100
what_again = divide(multiply(weight, add(height,iq)), 3)

print "That becomes: ", what_again, "Can you do that by hand?"


"""
ADDITIONAL NOTES AND COMMENTS:

We're now doing our own math functions for 'add', 'subtract', 'multiply', and 'divide'.
The important thing to notice is in the last line where we say 'return a + b' (in 'add').
What this does is the following:


1. Our function is called with two arguments: a and b.
2. We print out what our function is doing, in this case "ADDING."
3. Then we tell Python to do something kind of backward: we return the addition of a + b. 
You might say this as, "I add a and b then return them."
4. Python adds the two numbers. Then when the function ends, any line that runs it will be able 
to assign this a + b result to a variable.

EXAMPLE OUTPUT:

bash-3.2$ python ex21.py 
Let's do some math with just functions!
ADDING 30 + 5
SUBTRACTING 78 - 4
MULTIPLYING 90 * 2
DIVIDING 100 / 2
Age: 35, Height: 74, Weight: 180, IQ: 50
Here is a puzzle.
DIVIDING 50 / 2
MULTIPLYING 180 * 25
SUBTRACTING 74 - 4500
ADDING 35 + -4426
That becomes:  -4391 Can you do it by hand?
Here is another puzzle.
ADDING 50 + 3
DIVIDING 53 / 74
ADDING 35 + 0
MULTIPLYING 180 * 35
That now becomes: 6300
Here's a new puzzle for you:
ADDING 80 + 100
MULTIPLYING 120 * 180
DIVIDING 21600 / 3
That becomes:  7200 Can you do that by hand?


ADDITIONAL NOTES

* At the end of the script is a puzzle. We're taking the return value of one
function and using it as the argument of another function. We're doing this in a
chain so that we're kind of creating a formula using the functions. 

* Python prints the formula or the functions "inside out". When we start breaking down the
function into separate formulas and function calls we'l see how this works

"""

