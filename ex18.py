# -*- coding: utf-8 -*-
# Exercise 18: Names, Variables, Code, Functions
"""
Functions to 3 things:

1. They name pieces of code the way variables name strings and numbers.
2. They take arguments the way scripts take 'argv'
3. Using 1 and 2 they let you make your own "mini-scripts" or "tiny commands".

Can create a function by using the word 'def' in Python.
""" 

# this one is like your scripts with argv
def print_two(*args):
    arg1, arg2 = args
    print "arg1: %r, arg2: %r" % (arg1, arg2)
    
    # ok, that *args is actualy pointless, we can just do this
def print_two_again(arg1, arg2):
    print "arg1: %r, arg2: %r" % (arg1, arg2)
    
# this just takes one argument
def print_one(arg1):
    print "arg1: %r" % arg1
    
# this one takes no arguments
def print_none():
    print "I get nothin'."
    
print_two("Zed","Shaw")
print_two_again("Zed","Shaw")
print_one("First!")
print_none()

"""
For the first function, print_two:

1. First we tell Python we want to make a function using def for "define".
2. On the same line as def we give the function a name. In this case we just called 
it "print_two" but it could also be "peanuts". It doesn't matter, except that 
your function should have a short name that says what it does.
3. Then we tell it we want *args (asterisk args) which is a lot like your argv 
parameter but for functions. This has to go inside () parentheses to work.
4. Then we end this line with a : colon, and start indenting.
5. After the colon all the lines that are indented four spaces will become attached 
to this name, print_two. Our first indented line is one that unpacks the arguments 
the same as with your scripts.
6. To demonstrate how it works we print these arguments out, just like we would 
in a script.

The problem with print_two is that it's not the easiest way to make a function. 
In Python we can skip the whole unpacking arguments and just use the names we want 
right inside (). That's what print_two_again does.

After that you have an example of how you make a function that takes one argument
 in print_one.

Finally you have a function that has no arguments in print_none.

EXAMPLE OUTPUT:

bash-3.2$ python ex18.py
arg1: 'Zed', arg2: 'Shaw'
arg1: 'Zed', arg2: 'Shaw'
arg1: 'First!'
I get nothin'.

STUDY DRILLS:

Create a function checklist for later exercises:


1. Did you start your function definition with def?
2. Does your function name have only characters and _ (underscore) characters?
3. Did you put an open parenthesis ( right after the function name?
4. Did you put your arguments after the parenthesis ( separated by commas?
5. Did you make each argument unique (meaning no duplicated names)?
6. Did you put a close parenthesis and a colon ): after the arguments?
7. Did you indent all lines of code you want in the function four spaces? No more, no less.
8. Did you "end" your function by going back to writing with no indent (dedenting we call it)?

When you run ("use" or "call") a function, check these things:

1. Did you call/use/run this function by typing its name?
2. Did you put the ( character after the name to run it?
3. Did you put the values you want into the parenthesis separated by commas?
4. Did you end the function call with a ) character?

Note: To 'run,' 'call,' or 'use' a function all mean the same thing.

ADDITIONAL COMMENTS:

That which is allowed for a function name is the same as allowed for variable names:
Anything that doesn't start with a number, and is letters, numbers, and underscores will work.

The * in *args tells Python to take all the arguments to the function and then put them in 
args as a list. It's like argv that you've been using, but for functions. It's 
not normally used too often unless specifically needed.

"""


