# -*- coding: utf-8 -*-
# Exercise 31: Making Decisions
# In this script you will ask the user questions and make decisions based on 
# their answers

print "You enter a dark room with two doors. Do you go through door #1 or door #2?"

door = raw_input ("> ")

if door =="1":
    print "There's a giant bear here eating a cheese cake. What do ou do?"
    print "1. Take the cake."
    print "2. Scream at the bear."
    
    bear = raw_input("> ")
    
    if bear == "1":
        print "The bear eats your face off. Good job!"
    elif bear == "2":
        print "The bear eats your legs off. Good job!"
    else:
        print "Well, doing %s is probably better. Bear runs away." % bear
        
elif door == "2":
    print "You stare into the endless abyss at Cthulhu's retina."
    print "1. Blueberries."
    print "2. Yello jacket clothespins."
    print "3. Understanding revolvers yelling melodies."
    
    insanity = raw_input("> ")
    
    if insanity == "1" or insanity == "2":
        print "Your body survives powered by a mind of jello. Good job!"
    else:
        print "The insanity rots your eyes into a pool of muck. Good job!"
      
elif door == "3":
    print "You are asked to select one candy from two and eat it. One is red, and the other is blue."
    print "1. take the red one."
    print "2. take the blue one."

    candy = raw_input("> ")

    if candy == "1":
        print "You wake up and found this is just a ridiculous dream. Good job!"
    elif candy == "2":
        print "It's poisonous and you died."
    else:
        print "The man got mad and killed you."
      
      
else:
    print "You stumble around and fall on a knife and die. Good job!"
    
"""
ADDITIONAL NOTES:

A key point here is that you are now putting the if-statements inside if-statements
as code that can run. This is very powerful and can be used to create "nested" 
decisions, where one branch leads to another and another.

EXAMPLE OUTPUT:

bash-3.2$ python ex31.py
You enter a dark room with two doors. Do you go through door #1 or door #2?
> 2
You stare into the endless abyss at Cthulhu's retina.
1. Blueberries.
2. Yello jacket clothespins.
3. Understanding revolvers yelling melodies.
> 3
The insanity rots your eyes into a pool of muck. Good job!
bash-3.2$ python ex31.py
You enter a dark room with two doors. Do you go through door #1 or door #2?
> 1
There's a giant bear here eating a cheese cake. What do ou do?
1. Take the cake.
2. Scream at the bear.
> 1
The bear eats your face off. Good job!
bash-3.2$ python ex31.py
You enter a dark room with two doors. Do you go through door #1 or door #2?
> 1
There's a giant bear here eating a cheese cake. What do ou do?
1. Take the cake.
2. Scream at the bear.
> 2
The bear eats your legs off. Good job!
bash-3.2$ python ex31.py
You enter a dark room with two doors. Do you go through door #1 or door #2?
> 2
You stare into the endless abyss at Cthulhu's retina.
1. Blueberries.
2. Yello jacket clothespins.
3. Understanding revolvers yelling melodies.
> 1
Your body survives powered by a mind of jello. Good job!

bash-3.2$ python ex31.py
You enter a dark room with two doors. Do you go through door #1 or door #2?
> 3
You are asked to select one candy from two and eat it. One is red, and the other is blue.
1. take the red one.
2. take the blue one.
> 1
You wake up and found this is just a ridiculous dream. Good job!
bash-3.2$ python ex31.py
You enter a dark room with two doors. Do you go through door #1 or door #2?
> 3
You are asked to select one candy from two and eat it. One is red, and the other is blue.
1. take the red one.
2. take the blue one.
> 2
It's poisonous and you died.


ADDITIONAL COMMENTS:

* We can replace elif with a sequence of if-else combinations in some situations, but it depends
on how each if/else is written. It also means that Python will check every if-else combination, 
rather than just the first false ones like it would with if-elif-else.

* To tell if a number is between a range of numbers, we have 2 options:
(1) Use 0 < x < 10 or 1 <= x < 10, which is classic notation, or
(2) use x in range(1, 10)

* If we wanted more options in the if-elif-else blocks, we can add more elif blocks for each possible choice.

"""
