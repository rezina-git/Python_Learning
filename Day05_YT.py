#Sets in python--->Collection of unordered items
collections = {1,2,3,2,2,4,"hello","World","world",4}
print(collections)
print(type(collections))
print(len(collections))
#o/p:{1, 2, 3, 4, 'world', 'World', 'hello'}<class 'set'> 7(As duplicates values are noy alloweded in sets)

#To create empty sets
collections = set() #empty set
print(type(collections))

#Set Methods
#1.set.add(el)-->adds an element
collections = set()
collections.add(1)
collections.add(2)
collections.add(2)

collections.remove(2)
print(collections)

#Set Methods
set1 = {1,2,3}
set2 = {2,3,4}
print(set1.union(set2)) #O/p:{1, 2, 3, 4}
print(set1.intersection(set2))