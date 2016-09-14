print "I will now count my chickens:"

print "Hens", 25.0 +30.0 / 6.0    # I'm counting how many hens I have: 25.0+5.0 =30.0 hens
print "Roosters", 100.0 - 25.0 * 3.0 % 4.0   # I'm counting the number of roosters

print "now I will count the eggs:"

print 3.0 + 2.0 + 1.0 - 5.0 + 4.0 % 2.0 - 1.0 / 4.0 + 6.0   # 5.0 % 2.0 - 1.0/4.0 + 6.0

print "Is it true that 3.0 + 2.0 < 5.0 - 7.0?" # It's not true that 5.0 < -2.0

print 3.0 + 2.0 < 5.0 - 7.0     # False: 5.0 is greater tha -2.0

print "What is 3.0 + 2.0?", 3.0 + 2.0     # 3.0 + 2.0 = 5.0
print "What is 5.0 - 7.0?", 5.0-7.0      # 5.0-7.0 = -2.0

print "Oh, that's why it's False."

print "How about some more."

print "Is it greater?", 5.0 > -2.0     # TRUE
print "Is it greater or equal?", 5.0 >= -2.0   # TRUE
print "Is it less or equal?", 5.0 <= -2.0   # FALSE

"""
EXAMPLE OUTPUT:

bash-3.2$ python ex3_floating_point.py 
I will now count my chickens:
Hens 30.0
Roosters 97.0
now I will count the eggs:
6.75
Is it true that 3.0 + 2.0 < 5.0 - 7.0?
False
What is 3.0 + 2.0? 5.0
What is 5.0 - 7.0? -2.0
Oh, that's why it's False.
How about some more.
Is it greater? True
Is it greater or equal? True
Is it less or equal? False
"""