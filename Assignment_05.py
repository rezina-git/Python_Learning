#Using for range()
#range = sequence data type 
#syntax: range(start,end,step)
a = range(10) #end = 10 start =0 step=1

#for loop
#syntax : for variable in range(10):

for i in range(10):
     print(i,end = " ,") #Prints Horizontally
#Ex1. a = ["sita,"gita","hari"] Print this line by line:

b = ["sita","gita","hari"]
for i in b:
    print(i) #sita
    for j in i:
        print(j)

#Multiplication table 
#2*1
#2*2
#2*10

c = 2
for i in range(1,11,1): #variable ko name i nai rakhana parxa vanney hoina j rakh da ni telsey index janauxa
    print(f"{c}x{i}={c*i}")
    # print("2 *",i,"=",i*c)
    
#Print numbers from 1 to 100.
for i in range(1,101):
    print(i)

#Print numbers from 100 to 1.
for a in range(100,0,-1):
    print(a)
#Print the multiplication table n

n = int(input("Enter Number:"))

for i in range (1,11):
    print(n*i)

#Pass Statement
#Pass is null statement that does nothing.It is used as placeholder for future code.

# for el in range(10):
#     pass
if i > 5:
    pass
print("Some useful work")

#WAP to find the sum of first n numbers .(Using WHile)
n = 5
sum = 0
for i in range (1, n+1):
    sum+= i

print("Total sum =",sum)

n = 5
sum = 0
for i in range (1, n+1):
    sum+= i

print("Total sum =",sum)

#WAP to find the factorial of first n numbers.(Using for)
n = 5
fact =1
for i in range (1, n+1):
    fact *= i

print("factorial = ",fact)

#while loop 

M = 6 
fact = 1
i = 1
while (i <= M):
    fact *= i
    i += 1
print("factorial =", fact)