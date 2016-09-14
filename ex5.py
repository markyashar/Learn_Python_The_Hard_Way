# -*- coding: utf-8 -*-
# Exercise 5: More Variables and Printing
name = 'Zed A. Shaw'
age = 35 # not a lie
height = 74 # inches
height_cm = 74*2.54 # there are 2.54 cm in an inch
weight = 180 # lbs
weight_kg = 180 * 0.453  # there are 0.453 kg in a lb
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

print "Let's talk about %s." % name
print "He's %d inches tall." % height
print "He's %d centimeters tall." % height_cm
print "He's %d pounds heavy." % weight
print "He's %d kilograms heavy." % weight_kg
print "Acually that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth
print "His teeth are usually %r depending on the coffee." % teeth

# this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (age, height, weight, age + height + weight)
print "If I add %r, %r, and %r I get %r." % (age, height, weight, age + height + weight)

"""
EXAMPLE OUTPUT:
bash-3.2$ python ex5.py
Let's talk about Zed A. Shaw.
He's 74 inches tall.
He's 187 centimeters tall.
He's 180 pounds heavy.
He's 81 kilograms heavy.
Acually that's not too heavy.
He's got Blue eyes and Brown hair.
His teeth are usually White depending on the coffee.
His teeth are usually 'White' depending on the coffee.
If I add 35, 74, and 180 I get 289.
If I add 35, 74, and 180 I get 289.

STUDY DRILL:
1. Change all the variables so there is no my_ in front of each one. Make sure you change the name everywhere, 
not just where you used = to set them.
2. Try to write some variables that convert the inches and pounds to centimeters and kilograms. Do not just type in the 
measurements. Work out the math in Python.
3. Search online for all of the Python format characters.
4. Try more format characters. %r is a very useful one. It's like saying "print this no matter what."

ADDITIONAL COMMENTS:

%s, %r, and %d are formatters. They tell Python to take the variable on the right and put it in to replace the %s with 
its value. 

You can round a floating point number by using the round() like this: round(1.7333) 

If you get this error:  "TypeError: 'str' object is not callable.", it probaby means that you forgot
the % between the string and the list of variables.
"""