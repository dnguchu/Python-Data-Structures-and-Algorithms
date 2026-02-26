#problem 1
lst = [1, 2, 3, 4]

list(map(lambda x: x **3, lst))
list(filter(lambda x: x < 3, lst))

#Problem 2
#We will create our own higher order function which is the hallmark of higher order functions
words = str.split('The longest word in this sentance')

sorted(words, key=len)

#Problem 3
#Case sensitive sorting
sl = ['a', 'b', 'A', 'c', 'C']

sl.sort(key=str.lower)
"""
Functions or objects that change the object return None 
to show the object has only been changed and that no new object has been created
"""

sl
sl.sort()
sl

#Problem 4
#Use index elements to sort a list using lambda

