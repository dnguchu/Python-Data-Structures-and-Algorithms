"""
Sets are unordered collections on unique immutable items and cannot contain duplicates
They are used to perform mathematical set equations like union, intersection, difference and complement.
"""
#Problem 1
st1 = {'ab', 3, 4, (5,6)}

st2 = {'ab', 7, (7,6)}

print(st1-st2)

st1.intersection(st2)

st1.union(st2)

'ab' in st1

'ab' not in st2

for element in st1:
    print(element)

"""
Immutable sets work like regular sets but they cannot be changed after creation.
They are useful in that you can use them as keys in dictionaries and as elements of other sets.
They are called frozensets and are created using the frozenset() function.
"""
#Problem 2
st1.add(st2)

st1.add(frozenset(st2))
st1

fs1 = frozenset(st1)
fs2 = frozenset(st2)

{fs1: 'fs1', fs2: 'fs2'}