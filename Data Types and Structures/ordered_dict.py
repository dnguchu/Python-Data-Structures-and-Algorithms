"""
Ordered dictionaries remember the insertion order as opposed to regular dictionaries 
which are arbitrary and do not guarantee any order. 
They are useful when we want to maintain the order of items in a dictionary.
"""
#Problem 1
from collections import OrderedDict

od1 = OrderedDict()

od1['one'] = 1

od1['two'] = 2

od2 = OrderedDict()

od2['two'] = 2

od2['one'] = 1

od1 == od2 #Returns False because the order of items is different

#Problem 2
kvs = [('three', 3), ('four', 4), ('five', 5), ('six', 6)]

od1.update(kvs)

for k, v in od1.items():
    print(k, v)

od3 = OrderedDict(sorted(od1.items(), key = lambda t: (4*t[1]) - t[1] ** 2))

od3.values()