"""
Also known as double ended queue
They are list-like objects that support adding and removing elements from either end of the queue.
Supports some list operations such as indexing but do not support slicing.
"""
#Problem 1
#Populating and consuming items sequentially from either end of the queue
from collections import deque
import itertools

dq = deque('abc') #Creates a deque(['a', 'b', 'c'])

dq.append('d') #Adds 'd' to the right end of the queue

dq.appendleft('x') #Adds 'x' to the left end of the queue

dq.extend('efg') #Adds 'e', 'f' and 'g' to the right end of the queue

dq.extendleft('yz') #Adds 'y' and 'z' to the left end of the queue

dq.pop() #Removes and returns the rightmost element of the queue

dq.popleft() #Removes and returns the leftmost element of the queue

dq

dq.rotate(2) #Rotates the queue to the right by 2 steps

dq.rotate(-2) #Rotates the queue to the left by 2 steps

dq

#Problem 2
#Returning the slice of a deque as a list
list(itertools.islice(dq, 3, 9))

#Problem 3
#Using the maxlen parameter to create a fixed length queue
dq2 = deque([], maxlen=3)
for i in range(6):
    dq2.append(i)
    print(dq2)