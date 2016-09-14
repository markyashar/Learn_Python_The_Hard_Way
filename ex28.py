# -*- coding: utf-8 -*-
# Exercise 28: Boolean Practice

"""
Take each of these logic problems and write what you think the answer will be. 
In each case it will be either True or False. 

1. True and True: True
2. False and True: False
3. 1 == 1 and 2 == 1: False
4. "test" == "test": True
5. 1 == 1 or 2 != 1: True
6. True and 1 == 1: True
7. False and 0 != 0: False
8. True or 1 == 1: True
9. "test" == "testing": False
10. 1 != 0 and 2 == 1: False
11. "test" != "testing": True
12. "test" == 1: False
13. not (True and False): True
14. not (1 == 1 and 0! = 1): False
15. not (10 == 1 or 1000 == 1000): False
16. not (1 != 10 or 3 == 4): False
17. not ("testing" == "testing" and "Zed" == "Cool Guy"): True
18. 1 == 1 and (not("testing" == 1 or 1 == 0)): True
19. "chunky" == "bacon" and (not (3 == 4 or 3 == 3)): False
20. 3 == 3 and (not("testing" == "testing" or "Python" == "Fun")): False

Whenever you see these boolean logic statements, you can solve them easily by this 
simple process:

1. Find an equality test (== or !=) and replace it with its truth.
2. Find each and/or inside parentheses and solve those first.
3. Find each not and invert it.
4. Find any remaining and/or and solve it.
5. When you are done you should have True or False.

We can demonstrate all of this with a variation on # 20 above:

3 != 4 and not ("testing" != "test" or "Python" == "Python")

Here we show going through each of the steps and showing the translation until we've
boiled it down to a single result:

1. 3 != 4 is TRUE: TRUE AND NOT ("TESTING" != "TEST" OR "PYTHON" == "PYTHON")
"TESTING" != "TEST" IS TRUE: TRUE AND NOT (TRUE OR "PYTHON" == "PYTHON")
"PYTHON" == "PYTHON": TRUE AND NOT (TRUE OR TRUE)

2. Find each and/or in parentheses():
(TRUE OR TRUE) IS TRUE: TRUE AND NOT (TRUE)

3. Find each not and invert it:
NOT (TRUE) IS FALSE: TRUE AND FALSE

4. Find any remaining and/or and solve them:

TRUE AND FALSE is FALSE

With that we're done and know the result is False

EXAMPLE OUTPUT

>>> True and True
True
>>> False and True
False
>>> 1 == 1 and 2 == 2
True
>>> not False
True
>>> 1 == 1 and 2 == 1
False
>>> "test" == "test"
True
>>> 1 == 1 or 2 != 1
True
>>> True and 1 == 1
True
>>> False and 0 != 0
False
>>> True or 1 == 1
True
>>> "test" == "testing"
False
>>> 1 != 0 and 2 == 1
False
>>> "test" != "testing"
True
>>> "test" == 1
False
>>> not (True and False)
True

ADDITIONAL EXAMPLES

>>> 5 <= 6
True
>>> 6<=6
True
>>> 4 != 9
True
>>> 6 != 8 or  6>9
True
>>> 6 != 8 and  6>9
False
>>> 7 == 9

COMMONT STUDENT QUESTIONS

1. Why does "test" and "test" return "test" or 1 and 1 return 1 instead of True?
Python and many languages like to return one of the operands to their boolean expressions
rather than just True or False. This means that if you did False and 1 you get the first 
operand (False) but if you do True and 1 your get the second (1). Play with this a bit.

2. Is there any difference between != and <>?
Python has deprecated <> in favor of !=, so use !=. Other than that there should be no difference.

3. Note that any 'and' expression that has a False is immediately False, so you can
stop there. Any 'or' expression that has a True is immediately True, so you can stop 
there. But make sure that you can process the whole expression because later it becomes helpful.


"""

 

