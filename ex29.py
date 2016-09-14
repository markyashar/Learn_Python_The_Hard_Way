# -*- coding: utf-8 -*-
# Exercise 29: What if

people = 20
cats = 30
dogs = 15

if people < cats:
    print "Too many cats! The world is doomed!"
    
if people > cats:
    print "Not many cats! The world is saved!"
    
if people < dogs:
    print "The world is drooled on!"
    
if people > dogs:
    print "The world is dry!"
    
dogs += 5

if people >= dogs:
    print "People are greater than or equal to dogs."
    
if people <= dogs:
    print "People are less than or equal to dogs."
    
if people == dogs:
    print "People are dogs."
    
if (dogs < cats) and (people < cats):
    print "Cats are greater than dogs, and some people are afraid of cats!"
    
if (dogs < cats) and (people < cats):
    print "Cats are greater than dogs but cats are not greater than people!"
    
if (dogs == cats) or (cats < 10):
    print "Cats or equivalent to dogs but they're less than 10!"
    
if cats != 0:
    print "Cats still exist, so the mice are still afraid!"

"""
EXAMPLE OUTOPUT:

bash-3.2$ python ex29.py
Too many cats! The world is doomed!
The world is dry!
People are greater than or equal to dogs.
People are less than or equal to dogs.
People are dogs.
Cats are greater than dogs, and some people are afraid of cats!
Cats are greater than dogs but cats are not greater than people!
Cats still exist, so the mice are still afraid!


ADDITIONAL NOTES

The code x += 1 is the same as doing x = x + 1 but involves less typing. You can 
call this the "increment by" operator. The same goes for -= and many other expressions
you'll learn later.

"""