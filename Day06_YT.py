#List and Tuples in Python
#It can store the elements of different types(Integer,float,string, etc) in single list
student = ["marks",94.5, "Nepal"] 
marks =[94.4, 45.6, 45.1]
print(marks)
print(type(marks))
print(marks[0])
print(marks[1])

#List Slicing 
#Similar to string slicing
#Syntax: list-name[starting_index:End_index] # Ending is not included.
marks = [85,87, 94, 76, 45]
print(marks[1:4]) #O/P is [87, 94, 76]
print(marks[:4])# O/p is [85, 87, 94, 76]
print(marks[1:])#o/p is [87, 94, 76, 45]

#List Methods
list = [2,1,3]
list.append(4)# Adds one element at the end
print(list)
#list.sort()#sorts in ascending order
print(list.sort())#Prints None
print(list)
#To print in descending order
print(list.sort(reverse=True))
print(list)
#Can also be done in strings or characters
list = ["Litchi", "Apple","Banana"]
print(list.sort())
print(list)
print(list.sort(reverse= True))
print(list)

#list.reverse--> Reverse the whole list
list = ["Litchi", "Apple","Banana"]
print(list.reverse())
print(list) 

#list.insert(index,element)-->Insert element at index
list = [2,1,3]
list.insert(1,5)
print(list) #o/p: [2, 5, 1, 3]
#list.remove()-->Removes the first occurence of element
list = [2,1,3,1]
list.remove(1)
print(list)
#list.pop(index)-->Removes element at index
list = [2,1,3,1]
list.pop(2)
print(list)
#Writing list. in vscode will show all the methods we can use in python also can see how it works in python documentation in Google.

#Tuples in python
tup = (2,3,4,5)
print(type(tup))
print(tup[0])#Allowed ti access
#But not allowed to assign tup[0] =5
#Can print empty tuple
tup = ()
print(tup)
print(type(tup))
#Important Note: If you want to percieve single value in tuple you have to write comma(,) after that values.
#tuples slicing is same as strings  slicing.
#Tuples Methods
tup = (2,1,3,1)
# syntax : tup.index(el) --> Returns the occurence of elements index (kati index ma xa tyo dinxa )
print(tup.index(3))
#tuple.count(el) #Counts total occurences tup.count(1) is 2
print(tup.count(1))