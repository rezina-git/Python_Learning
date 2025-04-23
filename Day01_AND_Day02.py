#Datatype in python
    #1.Integer
    #2.Float
    #3.Complex(Combination of real and imaginary number C= 3 + 4j )
#Text dataype( String which is denoted by quotation('',"",''' ''')For more than one line we use triple quotation)
#Escape Methods in strings.
    #\t = tab it gives space.
    #n = It gives line break.

#Indexing = Position of character.
    #syntax: variable_name[index]
    #Example 1
a = "My name is Rejeena"
print(a[0])
print(a[3])
print(a[-1])#starting from last where -1 is first index.

#Slicing= Accesing the part of string
    #Syntax: variable_name[start:end:step]

#Example 2
    #To get 'name' from a
print(a[3:7:1])
    #To get reverse 'eman'
print(a[6:2:-1])#Count from M(index 0) to e(index 6 of name):3-1(2):Step(-1)
#To extract Rejeena
print (a[11:18:1])
# To get all after 2 index
print(a[2:])# Output: name is rejeena
#To get from 0 to 6 index
print(a[:7])
#To get all strings
print(a[::])
#To get all strings in reverse 
print(a[::-1])

#Example 3
'''To print 1.Kathmandu
            2.athmandu
            3.thmandu
            4.thman
            5.hma
            6.m'''
b = "Kathmandu"
print(b[0:9:1])
print(b[1:9:1])
print(b[2:9:1])
print(b[2:7:1])
print(b[3:6:1])
print(b[4:5:1])

#Strings inbuilt (precoded and predefine)method.
    #Mutable = Original data is changeable
    #immutable = Original data is not changeable.
#Strings are immutable
#1.upper()
c= "My name is reju"
d=c.upper()
print(d) #prints all strings in capital.

#2.Lower
d=c.lower()
print(d)#prints all strings in small.

#3.Swapcase = It converts lower to upper case letter and uppper to lower case letters.
d = c.swapcase()
print(d)

#Capitalize()
d = c.capitalize()
print (d) # Change only first letter to capital.

#startswith()
m = "Hey iam really excited in this python learning session"
l = m.startswith("Hey")
print(l)

#endswith()
m = "Hey iam really excited in this python learning session"
l = m.endswith("sessio")
print(l)

#count() : Counts the number of characters.
m = "Hey iam really excited in this python learning session"
l = m.count("e")
print(l) # O/p : 6

#find(): Finds the index of character 
m = "Hey iam really excited in this python learning session"
l = m.find("really")
print(l) #O/p : 8 as r is in 8th index.

#index
l = m.index("y")
print(l) # o/p : 2

#Split = "Apple, Banana, Orange"
t = "Apple Banana Orange"
r = t.split()
print(r)