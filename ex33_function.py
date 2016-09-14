# -*- coding: utf-8 -*-
# ex33_function.py: Replace while-loop with a function

"""
STUDY DRILLS
1. In ex33.py convert this while-loop to a function that you can call, and replace 6 in the test (i < 6) with a variable.
2. Use this function to rewrite the script to try different numbers.
3. Add another variable to the function arguments that you can pass in that lets you change the 
+ 1 (on line 8 or whatever) so you can change how much it increments by.
4. Rewrite the script again to use this function to see what effect that has.
5. Write it to use for-loops and range. Do you need the incrementor in the middle anymore? What happens if you do not get rid of it?
If at any time that you are doing this it goes crazy (it probably will), just hold down CTRL and press c (CTRL-c) and the program will abort.
"""

def createNumbers(max, step):
    i = 0
    numbers = []
    for i in range(0, max, step):
        print "At the top i is %d" % i
        numbers.append(i)
        
        print "Numbers now: ", numbers
        print "At the bottom i is %d" % i
    return numbers
    
numbers = createNumbers(10, 2)

print "The numbers: "

for num in numbers:
    print num

"""
EXAMPLE OUTPUT

bash-3.2$ python ex33_function.py
At the top i is 0
Numbers now:  [0]
At the bottom i is 0
At the top i is 2
Numbers now:  [0, 2]
At the bottom i is 2
At the top i is 4
Numbers now:  [0, 2, 4]
At the bottom i is 4
At the top i is 6
Numbers now:  [0, 2, 4, 6]
At the bottom i is 6
At the top i is 8
Numbers now:  [0, 2, 4, 6, 8]
At the bottom i is 8
The numbers: 
0
2
4
6
8
"""

