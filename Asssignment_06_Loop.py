# Write a program to print the squares of numbers from 1 to 10 using a for loop.

# Write a program to print all even numbers between 1 and 20 using a for loop.

# Write a program to calculate the sum of numbers from 1 to 50 using a for loop.

# Write a program to calculate the sum of all odd numbers between 1 and 100 using a for loop.

# Write a program to find the largest number in a list [2, 8, 1, 16, 5, 23, 7] using a for loop.

# Write a program that uses a while loop to print numbers from 1 to 10.

# Write a program that prints all even numbers between 1 and 20 using a while loop.

# Write a program that uses a while loop to print numbers from 10 to 1 in reverse order.

# Write a program that keeps taking input from the user and stops only when the user types "stop".

# Write a program to print the multiplication table of 5 using a while loop.

# Write a program to print the square of numbers from 1 to 10 using a while loop.

# Write a program to calculate the sum of all odd numbers between 1 and 30 using a while loop.

#--------->>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#1. Write a program to print the squares of numbers from 1 to 10 using a for loop.
for sq in range(1,11,1):
    print(f"{sq}*{sq} = {sq} *{sq}")
 
#OR---->>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

for i in range (1,11,1):
    s = i*i
    print(s)


# 2. Write a program to print all even numbers between 1 and 20 using a for loop.

for i in range(1,21):
    if i%2 == 0:
        print(i)
        
#3. Write a program to calculate the sum of numbers from 1 to 50 using a for loop.

a = 0
for i in range (1,50):
    a +=i

print(f"sum of numbers from 1 to 50 = {a}")

#4. # Write a program to calculate the sum of all odd numbers between 1 and 100 using a for loop.
b = 0
for i in range(1,101):
    if i%2 != 0:
        b+=i
print("sum = ",b)
       

#5. Write a program to find the largest number in a list [2, 8, 1, 16, 5, 23, 7] using a for loop.

a= [2, 8, 1, 16, 5, 23, 7]
largest= a[0]
for i in a:
    if i>largest:
        largest=i
print(f"the largest number in the list is:{largest}")

#------>While------>
#5. Write a program that uses a while loop to print numbers from 1 to 10.
i=1
while (i<11):
    print(i)
    i+=1

## Write a program that prints all even numbers between 1 and 20 using a while loop.

i=2
while (i<=21):
    print(i)
    i+=2
    
# Write a program that uses a while loop to print numbers from 10 to 1 in reverse order.
a=10
while a>=1:
    print(a)
    a-=1

# Write a program that keeps taking input from the user and stops only when the user types "stop".
# while True:
#     a = input("Write Something here:")
#     if a == "stops":
#         break

# Write a program to print the multiplication table of 5 using a while loop.
b = 5
i = 1

while i<=10:
    print(f"{b}*{i}={b*i}")
    i+=1

# Write a program to print the square of numbers from 1 to 10 using a while loop.
i = 1 
while i <=10:
    print((f"The square of {i}={i*i}"))
    i+=1

# Write a program to calculate the sum of all odd numbers between 1 and 30 using a while loop.

total = 0
i = 1
while i <= 30:
    total += i
    i+= 2
print(f"Sum of all odd numbers from 1 t0 30 ={total}")