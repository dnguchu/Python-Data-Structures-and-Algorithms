"""
Counter is a subclass of the dictionary where each key is a hashable object and the value is an
integer count of that object
"""
#Problem 1
from collections import Counter

c1 = Counter('anysequence')

c2 = Counter({'a': 1, 'c': 1, 'e': 3})

c3 = Counter(a=1, c=1, e=3)

c1

#Problem 2
#Populating an empty counter object using the update() method on an iterable or a mapping
from collections import Counter

ct = Counter() #Creates an empty counter object

ct.update('abca') #Populates the object

ct

ct.update({'a': 3}) #Updates the count of 'a' by adding the updated number

ct

for item in ct:
    print('%s : %d' % (item, ct[item]))

"""
Counter objects are different from dictionaries in that they return a zero for missing items 
rather than raising a key error
"""

#Problem 3
#This creates an iterator out of a counter object where counts below 1 are ignored and order is not guaranteed
ct.update({'a': -3, 'b': -2, 'd': 3, 'e': 2})

sorted(ct.elements())

ct.most_common()

ct.subtract({'a': 2})

ct