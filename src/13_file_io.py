"""
Python makes performing file I/O simple. Take a look
at how to read and write to files here:

https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
"""

# Open up the "foo.txt" file (which already exists) for reading
# Print all the contents of the file, then close the file
# Note: pay close attention to your current directory when trying to open "foo.txt"

# YOUR CODE HERE

# open:
foo = open('foo.txt', 'r')

# print:
[print(line, end='') for line in foo]

# close:
foo.close()

# all together: using with closes the file once its done.
with open('foo.txt', 'r') as f:
    [print(line, end='') for line in f]

print('\n')


# Open up a file called "bar.txt" (which doesn't exist yet) for
# writing. Write three lines of arbitrary content to that file,
# then close the file. Open up "bar.txt" and inspect it to make
# sure that it contains what you expect it to contain

# YOUR CODE HERE
# r+ allows you to read and write
with open('bar.txt', 'r+') as b:
    b.write('This is line 1\n')
    b.write('This is line 2\n')
    b.write('This is line 3\n')
    [print(line, end='') for line in b]




# close:
