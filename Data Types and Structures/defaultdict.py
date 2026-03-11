"""
For the default dict, instead of throwing an error when attempting to access a key not in the dictionary,
defaultdict runs a function that returns a default value for the key. 
The default value is specified when creating the defaultdict.
"""
#Problem 1
from collections import defaultdict

def isprimary(c):
    if (c == 'red') or (c == 'blue') or (c == 'green'):
        return True
    else:
        return False

dd2 = defaultdict(bool)

dd2
