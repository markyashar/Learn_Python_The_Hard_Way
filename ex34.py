# -*- coding: utf-8 -*-
# Exercise 34: Accessing Elements of Lists

"""
Here's how we would access the first element of a list:

animals = ['bear', 'tiger', 'penguin', 'zebra']
bears = animals[0]

You take a list of animals, and then you get the first (1st) one using 0 because
Python starts its lists at 0 rather than 1.

Every time you say to yourself, "I want the third animal," you translate this "ordinal" 
number to a "cardinal" number by subtracting 1. The "third" animal is at index 2 and is 
the penguin. You have to do this because you have spent your whole life using ordinal 
numbers, and now you have to think in cardinal. Just subtract 1 and you will be good.

Remember: ordinal == ordered, 1st; cardinal == cards at random, 0.

Recall: if we say "first," "second," then we're using ordinal, so subtract 1. 
If we have a cardinal (like "The animal at 1"), then use it directly.

"""

animals = ['bear', 'python', 'peacock', 'kangaroo', 'whale', 'platypus']

def printAnimal(index):
    if index == 1:
        number = "1st"
    elif index == 2:
        number = "2nd"
    elif index == 3:
        number = "3rd"
    else:
        number = str(index)+"th"
    print "The %s animal is at %d and is a %s" % (number, index-1, animals[index-1])
    print "The animal at %d is the %s animal and is a %s" % (index-1, number, animals[index-1])
    
for i in range(1, 7):
    printAnimal(i)
    
"""
EXAMPLE OUTPUT:

bash-3.2$ python ex34.py
The 1st animal is at 0 and is a bear
The animal at 0 is the 1st animal and is a bear
The 2nd animal is at 1 and is a python
The animal at 1 is the 2nd animal and is a python
The 3rd animal is at 2 and is a peacock
The animal at 2 is the 3rd animal and is a peacock
The 4th animal is at 3 and is a kangaroo
The animal at 3 is the 4th animal and is a kangaroo
The 5th animal is at 4 and is a whale
The animal at 4 is the 5th animal and is a whale
The 6th animal is at 5 and is a platypus
The animal at 5 is the 6th animal and is a platypus

"""