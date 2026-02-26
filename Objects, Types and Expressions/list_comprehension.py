"""
List comprehensions are recommended over map ad filter due to their readability and ease of use.
"""
#problem 1
def f1(x): return x*2 
def f2(x): return x*4 

lst = [] 
for i in range(16): 
    lst.append(f1(f2(i))) 

print(lst) 

print([f1(x)  for x in range(64) if x in [f2(j) for j in range(16)]]) 

#problem 2
list1 = [[1,2,3], [4,5,6]]

[i * j for i in list1[0] for j in list1[1]]

#problem 3
words = 'here is a sentance'.split()

[[word, len(word)] for word in words]

