"""
Python exposes a terse and intuitive syntax for performing
slicing on lists and strings. This makes it easy to reference
only a portion of a list or string.

This Stack Overflow answer provides a brief but thorough
overview: https://stackoverflow.com/a/509295

Use Python's slice syntax to achieve the following:
"""

a = [2, 4, 1, 7, 9, 6]

# Output the second element: 4:
print('Second Element:', a[1], '\n')

# Output the second-to-last element: 9
print('Second-to-Last Element:', a[4], '\n')

# Output the last three elements in the array: [7, 9, 6]
print('Last Three Elements:', a[-3:], '\n')

# Output the two middle elements in the array: [1, 7]
print('Two Middle Elements:', a[2:4], '\n')

# Output every element except the first one: [4, 1, 7, 9, 6]
print('All but the First:', a[1:], '\n')

# Output every element except the last one: [2, 4, 1, 7, 9]
print('All but the Last:', a[:-1], '\n')

# For string s...

s = "Hello, world!"

# Output just the 8th-12th characters: "world"
print('Last Word:', s[7:12])
