# -*- coding: utf-8 -*-
# Exercise 20: Functions and Files

# We import modules here
from sys import argv

# We set up argument variables that are called on the command line when the script is executed,
# i.e., assign the first and second arguments to the two variables
script, input_file = argv

# Define a function called print_all to print the whole contents of a 
# pre-existing file (that we created for the purpose of this exercise),
# with one file object(f) as a formal parameter.
def print_all(f):
    # print the contents of the file
    print f.read()
 
# Define a function called rewind to make the file reader go back to the first
# byte of the file, with one file object (f) as a formal parameter.   
def rewind(f):
    # make the file reader go bck to the first byte of the file
    f.seek(0)

# Define a function called print_a_line to print a line of the file, with an
# integer counter (line_count) and a file object (f) as formal parameters.    
def print_a_line(line_count,f):
    # Test whether two variables are carrying the same value
    print "line_count equal to current_line?:", (line_count == current_line)
    # print the number and contents of a line
    print line_count, f.readline()
    
# Open the file
current_file = open(input_file)

# Print out a statement to standard output
print "First let's print the whole file:\n"

# Call the print_all function to print the whole file
print_all(current_file)

# Print out another statement to standard output
print "Now let's rewind, kind of like a tape."

# Call the rewind function to go back to the beginning of the file
rewind(current_file)

# Now print the three lines from the top of the file

# Print out another statement to standard output
print "Let's print three lines:"

# Set the current line to 1
current_line = 1
# We are writing out what current_line is equal to on each function call, and 
# tracing how it becomes line_count in print_a_line.
print "current_line = %d" % current_line
# Print the current line by calling the print_a_line function
print_a_line(current_line, current_file)

# Set the current line to 2 by adding 1
# current_line = current_line + 1
current_line += 1
# We are writing out what current_line is equal to on each function call, and 
# tracing how it becomes line_count in print_a_line.
print "current_line = %d" % current_line
# Print current line by calling print_a_line function
print_a_line(current_line, current_file)

# Set current line to 3 by adding 1
# current_line = current_line + 1
current_line += 1
# We are writing out what current_line is equal to on each function call, and 
# tracing how it becomes line_count in print_a_line.
print "current_line = %d" % current_line
# Print current line by calling print_a_line function
print_a_line(current_line, current_file)

"""
EXAMPLE OUTPUT:

bash-3.2$ python ex20.py test.txt
First let's print the whole file:

This is line 1
This is line 2
This is line 3

Now let's rewind, kind of like a tape.
Let's print three lines:
1 This is line 1

2 This is line 2

3 This is line 3

ADDITIONAL NOTES AND COMMENTS

* Each time 'print_a_line' is run, we are passing in a variable 'current_line'.

* The class file(object) opens a file

* The Python method seek() sets the file's current position at the offset.

* file.seek = seek(...) moves to a new file position. The argument offset is a 
byte count.

* f in the print_all and other functions is a variable just like you had in other
functions in Exercise 18, except this time it's a file. A file in Python is kind
of like an old tape drive on a mainframe, or maybe a DVD player. It has a "read head,"
and you can "seek" this read head around the file to positions, then work with it there.
Each time you do f.seek(0) you're moving to the start of the file. Each time you do 
f.readline() you're reading a line from the file, and moving the read head to right 
after the \n that ends that line. 

* seek(0) does not set the current_line to 0 because:
(1) the seek() function is dealing in bytes, not lines. The code seek(0) moves 
the file to the 0 byte (first byte) in the file.
(2) current_line is just a variable and has no real connection to the file at all. 
We are manually incrementing it.

* Recall that x =x x + y is the same as x += y

* Inside readline() is code that scans each byte of the file until it finds a \n character, 
then stops reading the file to return what it found so far. The file f is responsible for 
maintaining the current position in the file after each readline() call, so that it will 
keep reading each line.

* The readline() function returns the \n that's in the file at the end of that line. Add a , 
at the end of your print function calls to avoid adding double \n to every line.



MORE EXAMPLE OUTPUT:

bash-3.2$ python ex20.py test.txt
First let's print the whole file:

This is line 1
This is line 2
This is line 3

Now let's rewind, kind of like a tape.
Let's print three lines:
current_line = 1
1 This is line 1

current_line = 2
2 This is line 2

current_line = 3
3 This is line 3


bash-3.2$ python ex20.py test.txt
First let's print the whole file:

This is line 1
This is line 2
This is line 3

Now let's rewind, kind of like a tape.
Let's print three lines:
current_line = 1
line_count equal to current_line?: True
1 This is line 1

current_line = 2
line_count equal to current_line?: True
2 This is line 2

current_line = 3
line_count equal to current_line?: True
3 This is line 3

"""