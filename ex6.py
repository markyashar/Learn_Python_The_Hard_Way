# -*- coding: utf-8 -*-
# Exercise 6: Strings and Text
# We set the variable x to a string: "There are 10 types of people."
x = "There are %d types of people." % 10
# We set the variable 'binary' to the string "binary".
binary = "binary"
# We set the variable 'do_not' to the string "don't"
do_not = "don't"
# Those who know binary and those who don't
y = "Those who know %s and those who %s." % (binary, do_not) # a string is put inside a string here

print x
print y

print "I said: %r." % x
print "I also said: '%s'." % y

hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"

print joke_evaluation % hilarious

w = "This is the left side of..."
e = "a string with a right side."
# We add up the 2 strings here to make a longer string.
print w + e

"""
EXAMPLE OUTPUT:

bash-3.2$ python ex6.py
There are 10 types of people.
Those who know binary and those who don't.
I said: 'There are 10 types of people.'.
I also said: 'Those who know binary and those who don't.'.
Isn't that joke so funny?! False
This is the left side of...a string with a right side.

ADDITIONAL COMMENTS:

* We use %r for debugging purposes, since it displays the "raw" data of the variable, but the others such as
%s are used for displaying variables to users.

* If you get the error "TypeError: not all arguments converted during string formatting", it indicates
that we have more % format characters in the string than variables to put in them.

* We put single quotes (') around some strings and not others mostly because of style, but we can use
single quotes inside a string that has double quotes. 


"""