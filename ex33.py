# -*- coding: utf-8 -*-
# Exercise 33: While Loops
"""
A while-loop will keep executing the code block under it as long as a boolean expression is True.

While-loops do a test like an if-statement, but instead of running the code block once, they jump back to the 
"top" where the while is, and repeat. A while-loop runs until the expression is False.

Here's the problem with while-loops: Sometimes they do not stop. This is great if your intention is to just 
keep looping until the end of the universe. Otherwise you almost always want your loops to end eventually.

To avoid these problems, there are some rules to follow:

1. Make sure that you use while-loops sparingly. Usually a for-loop is better.
2. Review your while statements and make sure that the boolean test will become False at some point.
3. When in doubt, print out your test variable at the top and bottom of the while-loop to see what it's doing.

In this exercise, we'll learn the while-loop while doing these three checks:
"""

i = 0
numbers = []

while i < 6:
    print "At the top i is %d" % i
    numbers.append(i)
    
    i = i + 1
    print "Numbers now: ", numbers
    print "At the bottom i is %d" % i
    
print "The numbers: "

for num in numbers:
    print num

"""
EXAMPLE OUTPUT:

bash-3.2$ python ex33.py
At the top i is 0
Numbers now:  [0]
At the bottom i is 1
At the top i is 1
Numbers now:  [0, 1]
At the bottom i is 2
At the top i is 2
Numbers now:  [0, 1, 2]
At the bottom i is 3
At the top i is 3
Numbers now:  [0, 1, 2, 3]
At the bottom i is 4
At the top i is 4
Numbers now:  [0, 1, 2, 3, 4]
At the bottom i is 5
At the top i is 5
Numbers now:  [0, 1, 2, 3, 4, 5]
At the bottom i is 6
The numbers: 
0
1
2
3
4
5

ADDITIONAL NOTES

* The difference between a for-loop and a while-loop is that a for-loop can only iterate
(loop) "over" collections of things. A while-loop can do any kind of iteration (looping)
you want. However, while-loops are harder to get right and you normally can get many 
things done with for-loops.

* The main reason people don't understand loops is because they can't follow the "jumping" 
that the code does. When a loop runs, it goes through its block of code, and at the end it 
jumps back to the top. To visualize this, we can put print statements all over the loop printing
 out where in the loop Python is running and what the variables are set to at those points.
 We can write print lines before the loop, at the top of the loop, in the middle, and at the bottom. 
 We can study the output and try to understand the jumping that's going on.

"""