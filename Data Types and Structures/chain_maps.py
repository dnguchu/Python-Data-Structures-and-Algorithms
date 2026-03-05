"""
Chain maps offer a way to link dictionaries and other mapping types to be treated as a single object.
The underlying mappings are stored in a list and are accessible through map[i] to retireve the i-th mapping.
They are useful when we are dealing with dictionaries containing related data.
"""
#Problem 1
from collections import ChainMap

defaults = {'theme': 'Default', 'language': 'eng', 'showIndex': True, 'showFooter': True}

cm = ChainMap(defaults) #Creaets a chainmap with the default configuration

cm2 = cm.new_child({'theme': 'bluesky'}) #Creates a new chainmap with a child that overrides the parent 

cm2['theme']

cm2.pop('theme') #Removes the child mapping and returns the value of the popped key

cm2['theme'] #Returns the default theme

cm2.maps[0] = {'theme': 'desert', 'showIndex': False} #adds a 'root_context' same as new_child()

cm2['showIndex']

"""
The advantage of using chain maps is that they allow us to retain previously set values
Adding a child context overrides values for the same key but it doesn't remove it from the data structure
This is useful for when we want to keep a record of the changes to help easily roll back to previous settings
"""
#Problem 2
#We can retireve and change any value in any of the dictionaries using the map() method with an index
cm2.maps[0] = {'theme': 'desert', 'showIndex': False}

cm2['showIndex']

cm2.parents #Returns defaults