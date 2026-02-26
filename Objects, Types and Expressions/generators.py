"""
These are functions that return an entire sequence or results instead of a single value
Call by using the yield keyword instead of return
They are an easy way to create iterators and can be used in a loop in place of lists or other iterables
"""

#Problem 1
#Compares the running time of a list and a generator
import time

#generator function creates an iterator of odd numbers between n and m
def oddGen(n, m):
    while n < m:
        yield n
        n += 2

#builds a list of odd numbers between n and m
def oddLst(n, m):
    lst = []
    while n < m:
        lst.append(n)
        n += 2
    return lst

#calculates the time it takes to perform the sum on an iterator
t1 = time.time()
sum(oddGen(1, 1000000))
print('Time taken to sum an iterator: %f' %(time.time() - t1))

#calculates the time it takes to build and sum a list
t1 = time.time()
sum(oddLst(1, 1000000))
print('Time taken to sum a list: %f' %(time.time() - t1))

"""
Generators perform better since they generate values on demand while lists build the
whole list and saves it in memory before processing it.
A calculation can begin before all elements are generated and only needed values are generated.
"""

#Problem 2
"""
You can create generator expressions by replacing square brackets with parentheses
Instead of creating a list, it creates a generator object that can be iterated over, on demand.
"""
lst1 = [1, 2, 3, 4]
gen1 = (10 ** i for i in lst1)
gen1
for x in gen1:
    print(x)