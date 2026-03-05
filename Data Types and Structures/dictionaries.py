#Problem 1
d ={'one': 1 , 'two': 2, 'three': 3 } # creates a dictionary

print(d)

d['four']=4 #add an item 

print(d)

d.update({'five': 5, 'six': 6}) #add multiple items 

print(d)

'five' in d

sorted(list(d))

sorted(list(d.values()))

sorted(list(d), key = d.__getitem__)

[value for (key, value) in sorted(d.items())]

sorted(list(d), key=d.__getitem__, reverse=True)

d2 = {'one': 'uno', 'two':'deux', 'three':'trois', 'four':'quatre', 'five':'cinq', 'six':'six'}

sorted(d2, key=d.__getitem__)

[d2[i] for i in sorted(d2, key=d.__getitem__)]

def corder(string):
    return string[-1]

sorted(d2.values(), key=corder)

def wordcount(fname):
    try:
        fhand=open(fname)
    except:
        print('File cannot be opened')
        return
    
    count=dict()
    for line in fhand:
        words = line.split()
        for word in words:
            if word not in count:
                count[word] = 1
            else:
                count[word] += 1
    return count

count=wordcount('/mnt/Data/Projects/Python-Data-Structures-and-Algorithms/Data Types and Structures/alice.txt')
filtered = { key:value for key, value in count.items() } 
filtered