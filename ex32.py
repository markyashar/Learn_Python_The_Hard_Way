# -*- coding: utf-8 -*-
# Exercise 32: Loops and Lists
"""
Before you can use a for-loop, you need a way to store the results of loops somewhere. 
The best way to do this is with lists. Lists are exactly what their name says: 
a container of things that are organized in order from first to last. It's not complicated; 
we just have to learn a new syntax. First, there's how we make lists:

hairs = ['brown', 'blond', 'red']
eyes = ['brown', 'blue', 'green']
weights = [1, 2, 3, 4]

We start the list with the [ (left bracket) which "opens" the list. Then you put 
each item you want in the list separated by commas, similar to function arguments. 
Lastly, end the list with a ] (right bracket) to indicate that it's over. Python 
then takes this list and all its contents and assigns them to the variable.
"""

the_count = [1,2,3,4,5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

# this first kind of for-loop goes through a list
for number in the_count:
    print "This is count %d" % number
    
# same as above
for fruit in fruits:
    print "A fruit of type: %s" % fruit
    
# also we can go through mixed lists too
# notice we have to use %r since we don't know what's in it
for i in change:
    print "I got %r" % i
    
# we can also build lists, first start with an empty one
elements = []

# then use the range function to do 0 to 5 counts
for i in range(0, 6):
    print "Adding %d to the list." % i
    # append is a function that lists understand
    elements.append(i)
    
# now we can print them out too
for i in elements:
    print "Element was: %d" % i
    
"""
EXAMPLE OUTPUT:

bash-3.2$ python ex32.py
This is count 1
This is count 2
This is count 3
This is count 4
This is count 5
A fruit of type: apples
A fruit of type: oranges
A fruit of type: pears
A fruit of type: apricots
I got 1
I got 'pennies'
I got 2
I got 'dimes'
I got 3
I got 'quarters'
Adding 0 to the list.
Adding 1 to the list.
Adding 2 to the list.
Adding 3 to the list.
Adding 4 to the list.
Adding 5 to the list.
Element was: 0
Element was: 1
Element was: 2
Element was: 3
Element was: 4
Element was: 5

STUDY DRILLS:
1. Make sure to understand the 'range' function
2. Note that there are cases were for-loops can be avoided and range functions can be used instead.
3. Understand lists and the various operations we can do on them such as 'append'.

ADDITIONAL NOTES:
* An example of a 2-dimensional (2D) list is [[1,2,3],[4,5,6]]

* Whether a lists and arrays are the same thing depends on the language and the implementation.
 In classic terms a list is very different from an array because of how they're implemented. In 
 Ruby though they call these arrays. In Python they call them lists. Just call these lists for 
 now since that's what Python calls them.
 
 * A for-loop is able to use a variable that isn't defined yet because the variable 
is defined by the for-loop when it starts, initializing it to the current element of 
the loop iteration, each time through.

* The expression 'for i in range(1,3):' only loops two times instead of 3 times because
the 'range()' function only does numbers from the first to the last, not including the last.
So it stops at two, not three in the above. This turns out to be the most common way to do
this kind of loop.

* elements.append() simply appends to the end of the list.


"""



