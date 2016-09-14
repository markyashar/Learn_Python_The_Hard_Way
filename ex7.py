# -*- coding: utf-8 -*-
# Exercise 7: More Printing

print "Mary had a little lamb."
# We print out a string within a string here. Note that 'snow' is not a 
# variable. A variable would not have single-quotes around it.
print "Its fleece was white as %s." % 'snow'
print "And everywhere that Mary went."
# This prints out '.' ten times, i.e., '..........'
print "." * 10 # what'd that do? 

end1 = "C"
end2 = "h"
end3 = "e"
end4 = "e"
end5 = "s"
end6 = "e"
end7 = "B"
end8 = "u"
end9 = "r"
end10 = "g"
end11 = "e"
end12 = "r"

# watch the comma at the end. try removing it to see what happens. When the
# comma is removed, 'Burger' is printed out on a separate line as 'Cheese'. 
print end1 + end2 + end3 + end4 + end5+ end6,
print end7 + end8 + end9 + + end10 + end11 + end12

"""
EXAMPLE OUTPUT
bash-3.2$ python ex7.py
Mary had a little lamb.
Its fleece was white as snow.
And everywhere that Mary went.
..........
Cheese Burger

ADDITIONAL COMMENTS:

* In Python, using either single-quotes or double-quotes to make a string is acceptable,
although we'll typically use single-quotes for any short strings like 'a' or 'snow'.

* In Python code, a line that's longer than 80 characters is bad style
"""