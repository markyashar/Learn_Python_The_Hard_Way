# -*- coding: utf-8 -*-
# Exercise 38: Doing Things to Lists

'''
When you write mystuff.append('hello') you are actually setting off a chain of events inside Python 
to cause something to happen to the mystuff list. Here's how it works:

1. Python sees you mentioned mystuff and looks up that variable. It might have to 
look backward to see if you created with =, if it is a function argument, or if it's 
a global variable. Either way it has to find the mystuff first.

2. Once it finds mystuff it reads the . (period) operator and starts to look at variables 
that are a part of mystuff. Since mystuff is a list, it knows that mystuff has a bunch of functions.

3. It then hits append and compares the name to all the names that mystuff says it owns. If append is 
in there (it is) then Python grabs that to use.

4. Next Python sees the ( (parenthesis) and realizes, "Oh hey, this should be a function." At this point it 
calls (runs, executes) the function just like normally, but instead it calls the function with an extra argument.

5. That extra argument is 'mystuff' I know, weird, right? But that's how Python works so it's best to just 
remember it and assume that's the result. What happens, at the end of all this, is a function call that looks 
like: append(mystuff, 'hello') instead of what you read which is mystuff.append('hello').

Here's an exercise that mixes strings and lists:

'''

ten_things = "Apples Oranges Crows Telephone Light Sugar"

print "Wait there are not 10 things in that list. Let's fix that."

stuff = ten_things.split(' ')
more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]
while len(stuff) != 10:
    next_one = more_stuff.pop()
    print "Adding:", next_one
    stuff.append(next_one)
    print "There are %d items now." % len(stuff)

print "There we go: ", stuff

print "Let's do some things with stuff."

print stuff[1]
print stuff[-1]  # whoa! fancy
print stuff.pop()
print ' '.join(stuff) # what? cool!
print '#'.join(stuff[3:5]) # super stellar!

'''
EXAMPLE OUTPUT:

bash-3.2$ python ex38.py
Wait there are not 10 things in that list. Let's fix that.
Adding: Boy
There are 7 items now.
Adding: Girl
There are 8 items now.
Adding: Banana
There are 9 items now.
Adding: Corn
There are 10 items now.
There we go:  ['Apples', 'Oranges', 'Crows', 'Telephone', 'Light', 'Sugar', 'Boy', 'Girl', 'Banana', 'Corn']
Let's do some things with stuff.
Oranges
Corn
Corn
Apples Oranges Crows Telephone Light Sugar Boy Girl Banana
Telephone#Light

-------------
ADDITIONAL NOTES -- WHAT LISTS CAN DO

Let's say you want to create a computer game based on Go Fish. To do this you would
need to have some way of taking the concept of a "deck of cards" and put it into your 
Python program. You then have to write Python code that knows how to work this imaginary
version of a deck of cards so that a person playing your game thinks that it's real, 
even if it isn't. What you need is a "deck of cards" structure, and programmers call 
this kind of thing a "data structure".

A "data structure" is just a formal way to structure (organize) some data (facts). 
It really is that simple, even though some data structures can get insanely complex, 
all they are is just a way to store facts inside a program so you can access them 
in different ways. They structure data.

Lists are one of the most common data structures programmers use. They are simply 
ordered lists of facts you want to store and access randomly or linearly by an index. 
Let's look at the deck of cards as an example of a list:

1. You have a bunch of cards with values.
2. Those cards are in a stack, list, or list from the top card to the bottom card.
3. You can take cards off the top, the bottom, the middle at random.
4. If you want to find a specific card, you have to grab the deck and go through it one at a time.

* "An ordered list" -- a deck of cards is in order with a first and a last.

* "of things you want to store" -- cards are things we want to store

* "and access randomly" -- we can grab a card from anywhere in the deck

* "or linearly" -- if we want to find a specific card we can start at the beginning and go in order.

* "by an index" -- Almost, since with a deck of cards if I told you to get the card at index 19 you'd
have to count until you found that one. In our Python lists the computer can just jump right to any
index you give it.

WHEN TO USE LISTS:

You use a list whenever you have something that matches the list data structure's useful features:

1. If you need to maintain order. Remember, this is listed order, not sorted order. Lists do not sort for you.
2. If you need to access the contents randomly by a number. Remember, this is using cardinal numbers starting at 0.
3. If you need to go through the contents linearly (first to last). Remember, that's what for-loops are for.


ADDITIONAL NOTES:

* more_stuff.pop() reads as, "Call pop on more_stuff."  Meanwhile, pop(more_stuff) means, 
"Call pop with argument more_stuff." Understand how they are really the same thing.

* join() is a method we call on the inserted string to put between the list to be joined. 

* stuff[3:5] extracts a "slice" from the stuff list that is from element 3 to element 4, 
meaning it does not include element 5. It's similar to how range(3,5) would work.

'''




    