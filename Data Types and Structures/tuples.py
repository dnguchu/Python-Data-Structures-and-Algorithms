"""
Tuples are immutable sequences of arbitrary objects.
Tuples are defined using parentheses () and can contain any number of elements, including zero.
Tuples are hashable, which means we can sort lists of tuples and use them as keys in dictionaries. 
"""

#Problem 1
#Creating a tuple
tuple('sequence')

#Problem 2
#Assigning more than one variable at a time
l = ('one', 'two')

x, y = l

print(x)

x, y = y, x

print(x)