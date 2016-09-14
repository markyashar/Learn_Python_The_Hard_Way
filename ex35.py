# -*- coding: utf-8 -*-
# Exercise 35: Branches and Functions

from sys import exit

def gold_room():
    '''A room full of gold'''
    print "This room is full of gold. How much do you take?"
    
    choice = raw_input("> ")
    if "0" in choice or "1" in choice:
        how_much = int(choice)
    else:
        dead("Man, learn to type a number.")
        
    if how_much < 50:
        print "Nice, you're not greedy, you win!"
        exit(0)
    else: 
        dead("You greedy bastard!")
        
def bear_room():
    '''A room with a bear'''
    print "There is a bear here."
    print "The bear has a bunch of honey."
    print "The fat bear is in front of another door."
    print "How are you going to move the bear?"
    bear_moved = False
    
    while True:
        choice = raw_input("> ")
        
        if choice == "take honey":
            dead("The bear looks at you then slaps your face off.")
        elif choice == "taunt bear" and not bear_moved:
            print "The bear has moved from the door. You can go through it now."
            bear_moved = True
        elif choice == "taunt bear" and bear_moved:
            dead("The bear gets pissed off and chews your leg off.")
        elif choice == "open door" and bear_moved:
            gold_room()
        else:
            print "I got no idea what that means."
            
def cthulhu_room():
    '''A room with the un-great evil Cthulhu.'''
    print "Here you see the great evil Cthulhu."
    print "He, it, whatever stares at you and you go insane."
    print "Do you flee for your life or eat your head?"
    
    choice = raw_input("> ")
    
    if "flee" in choice:
        start()
    elif "head" in choice:
        dead("Well that was yummy!")
    else:
        cthulhu_room()
        
def dead(why):
    ''' Call this when our hero dies'''
    print why, "Good job!"
    exit (0)
        
def start():
    ''' Beginning of the game story'''
    print "you are in a dark room."
    print "There is a door to your right and left."
    print "Which one do you take?"
        
    choice = raw_input("> ")
        
    if choice == "left":
        bear_room()
    elif choice == "right":
        cthulhu_room()
    else:
        dead("You stumble around the room until you starve.")
            
start()
        
    
"""
EXAMPLE OUTPUT:

bash-3.2$ python ex35.py
you are in a dark room.
There is a door to your right and left.
Which one do you take?
> left
There is a bear here.
The bear has a bunch of honey.
The fat bear is in front of another door.
How are you going to move the bear?
> right
I got no idea what that means.
> left
I got no idea what that means.
> honey
I got no idea what that means.
> take honey
The bear looks at you then slaps your face off. Good job!
bash-3.2$ python ex35.py
you are in a dark room.
There is a door to your right and left.
Which one do you take?
> right
Here you see the great evil Cthulhu.
He, it, whatever stares at you and you go insane.
Do you flee for your life or eat your head?
> flee
you are in a dark room.
There is a door to your right and left.
Which one do you take?
> right
Here you see the great evil Cthulhu.
He, it, whatever stares at you and you go insane.
Do you flee for your life or eat your head?
> eat
Here you see the great evil Cthulhu.
He, it, whatever stares at you and you go insane.
Do you flee for your life or eat your head?
> eat my head
Well that was tasty! Good job!
bash-3.2$ python ex35.py
you are in a dark room.
There is a door to your right and left.
Which one do you take?
> right
Here you see the great evil Cthulhu.
He, it, whatever stares at you and you go insane.
Do you flee for your life or eat your head?
> flee for my life
you are in a dark room.
There is a door to your right and left.
Which one do you take?
> left
There is a bear here.
The bear has a bunch of honey.
The fat bear is in front of another door.
How are you going to move the bear?
> taunt bear
The bear has moved from the door. You can go through it now.
> open door
This room is full of gold. How much do you take?
> all
Man, learn to type a number. Good job!


ADDITIONAL NOTES

* Recall, when we get stuck understanding a piece of code, simply write an English
comment above every line explaining what that line does. Keep your comments short 
and similar to the code. Then either diagram how the code works or write a paragraph 
describing it. If you do that you'll get it.

* 'while True' makes an infinite loop.

* On many operating systems a program can abort with exit(0), and the number passed 
in will indicate an error or not. If you do exit(1) then it will be an error, but exit(0) 
will be a good exit. The reason it's backward from normal boolean logic (with 0==False) is
that you can use different numbers to indicate different error results. You can do exit(100)
for a different error result than exit(2) or exit(1).

* The parameter to raw_input is a string that it should print as a prompt before getting the user's input.

"""
