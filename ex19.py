# -*- coding: utf-8 -*-
# Exercise 19: Functions and Variables
# Note that the variables in your function are not connected to the variables
# in your script. This exercise will get us thinking about this:

# We are creating a function with two variables for printing things out
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print "You have %d cheeses!" % cheese_count
    print "You have %d boxes of crackers!" % boxes_of_crackers
    print "Man that's enough for a party!"
    print "Get a blanket.\n"
 
# We give the variables of the function numbers and we call the function here.   
print "We can just give the function numbers directly:"
cheese_and_crackers(20, 30)

# We give the variables numbers and than call the function with these variables
print "OR, we can use variables from our script:"
amount_of_cheese = 10
amount_of_crackers = 50

# We call the function with the variables we just set 
cheese_and_crackers(amount_of_cheese, amount_of_crackers)

# We can do math operations inside the function
print "We can even do match inside too:"
cheese_and_crackers(10 + 20, 5 + 6)

# We can combine the variables and math operations within the function
print "And we can combine the two, variables and math:"
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)

def apples_and_oranges(apple_count, orange_count):
    print "You have %d apples!" % apple_count
    print "You have %d oranges!" % orange_count
    print "Man that's a really health meal!"
    print "Bring some knives, forks, plates, and cups. We can make orange juice too!\n"

apples_and_oranges(23,45)

amount_of_apples = 34
amount_of_oranges = 54 

apples_and_oranges(amount_of_apples, amount_of_oranges)
apples_and_oranges(34-5, 23*8)
apples_and_oranges(amount_of_apples+89, amount_of_oranges*2)

"""
COMMENTS:

This shows all the different ways we're able to give our function cheese_and_crackers 
the values it needs to print them. We can give it straight numbers. We can give 
it variables. We can give it math. We can even combine math and variables.

In a way, the arguments to a function are kind of like our = character when we 
make a variable. In fact, if you can use = to name something, you can usually 
pass it to a function as an argument.

EXAMPLE OUTPUT

bash-3.2$ python ex19.py
We can just give the function numbers directly:
You have 20 cheeses!
You have 30 boxes of crackers!
Man that's enough for a party!
Get a blanket.

OR, we can use variables from our script:
You have 10 cheeses!
You have 50 boxes of crackers!
Man that's enough for a party!
Get a blanket.

We can even do match inside too:
You have 30 cheeses!
You have 11 boxes of crackers!
Man that's enough for a party!
Get a blanket.

And we can combine the two, variables and math:
You have 110 cheeses!
You have 1050 boxes of crackers!
Man that's enough for a party!
Get a blanket.

You have 23 apples!
You have 45 oranges!
Man that's a really health meal!
Bring some knives, forks, plates, and cups. We can make orange juice too!

You have 34 apples!
You have 54 oranges!
Man that's a really health meal!
Bring some knives, forks, plates, and cups. We can make orange juice too!

You have 29 apples!
You have 184 oranges!
Man that's a really health meal!
Bring some knives, forks, plates, and cups. We can make orange juice too!

You have 123 apples!
You have 108 oranges!
Man that's a really health meal!
Bring some knives, forks, plates, and cups. We can make orange juice too!

ADDITIONAL COMMENTS

* If we want to ask the user for the numbers of cheese and crackers, we need to
use int() to convert what we get from raw_input(). 

* Making the variable amount_of_cheese does no change the variable cheese_count
in the function. These variables are separate and live outside the function. They
are then passed to the function and temporary versions are amde just for the function's
run. When the function exits these temporary variables go away and everything keeps
working. 

* It's bad to have global variables (like amount_of_cheese) with the same name as function
variables, since then you're not quite sure which one you're talking about. But sometimes
necessity means you have to use the same name, or you might do it on accident. Just avoid
it whenever you can.

* The limit to the number of arguments a function can have depends on the version of Python 
and the computer we're on, but it's fairly large. The practical limit though is about 5
arguments before the function becomes annoying to use.

* It's possible to call a function with a function.

""" 

