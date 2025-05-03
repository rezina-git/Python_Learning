#Loops in Python
#Loops are used for sequential traversal.For traversing list,string,tuples,etc.
list = [1,2,3,4,5]

for val in list :
    print(val)

vegis = ["potato", "brinjal","Ladyfingure"]
for val in vegis:
    print(val)
str = "apanacollege"

for char in str:
    print(char)
else:
    print("End")
    
#Ex1. Print the elements of following list in loop
list = [1,4,9,16,25,36,49,64,81,100]

for nums in list:
    print(nums)

#Search for number x in this tuple using loop.
list = [1,4,9,16,25,36,49,64,81,100]
x =49
idx = 0
for nums in list:
    if (nums== x):
        print("Number found at idx", idx)
    idx += 1

#range()
#Range functions returns a sequence of numbers,starting from 0 by default ,and increments by 1 (by default) and stops before a specified number. 
seq = range(5)

for i in seq:
    print(i)
    
for i in range (2,10,2): #range (start,stop,step)
    print(i)
    
#To print even number from 1 to 10 
for a in range(2, 100,2):
 print(a)
#To print Odd:
for i in range (1, 100, 2):
    print(i)