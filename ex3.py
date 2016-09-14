print "I will now count my chickens:"

print "Hens", 25 +30 / 6    # I'm counting how many hens I have: 25+5 =30 hens
print "Roosters", 100 - 25 * 3 % 4   # I'm counting the number of roosters

print "now I will count the eggs:"

print 3 + 2 + 1 - 5 + 4 % 2 - 1 / 4 + 6   # 5 % 2 - 1/4 + 6

print "Is it true that 3 + 2 < 5 - 7?" # It's not true that 5 < -2

print 3 + 2 < 5 - 7     # False: 5 is greater tha -2

print "What is 3 + 2?", 3 + 2     # 3 + 2 = 5
print "What is 5 - 7?", 5 -7      # 5-7 = -2

print "Oh, that's why it's False."

print "How about some more."

print "Is it greater?", 5 > -2     # TRUE
print "Is it greater or equal?", 5 >= -2   # TRUE
print "Is it less or equal?", 5 <= -2   # FALSE

"""
EXAMPLE OUTPUT:

bash-3.2$ python ex3.py
I will now count my chickens:
Hens 30
Roosters 97
now I will count the eggs:
7
Is it true that 3 + 2 < 5 - 7?
False
What is 3 + 2? 5
What is 5 - 7? -2
Oh, that's why it's False.
How about some more.
Is it greater? True
Is it greater or equal? True
Is it less or equal? False
"""

"""
ADDITIONAL NOTES:

The modulus operation (%) is a way of saying "X divided by Y with J remaining." 
For example, "100 divided by 16 with 4 remaining." The result of % is the J part, 
or the remaining part.

In the United States we use an acronym called PEMDAS which stands for Parentheses 
Exponents Multiplication Division Addition Subtraction, to determine the order
of operations. That's the order Python follows as well.

The / (division) operator drops the fractional part of the decimal
For example, 7/4=1  and 7.0/4.0=1.75
"""