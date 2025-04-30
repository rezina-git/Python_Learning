#Loops in python-->Loops are used to repeat instructions
#While Loops

count = 1
while count<=5:
    print("Hello",count)
    count += 1

#print numbers from 1 to 5
i = 1
while i <= 5:
    print(i)
    i += 1
print("Loop Ended")
#To print from 5 to 1
i = 5
while i >= 1:
    print(i)
    i -= 1
print("Loop Ended")

#1. Print the numbers from 1 to 100
count = 1
while count<=100:
    print(count)
    count +=1
#2. Print the numbers from 1 to 100
count = 100
while count>=1:
    print(count)
    count -=1
#3.Print the multiplication table of number n.
n = int(input("Enter a number:"))
i = 1
while i<= 10:
    print(n*i)
    i+= 1
    
#4. Print the elements of the following list using a loop
#[1,4,9,16,36,49,64,81,100]
nums = [1,4,9,16,36,49,64,81,100]
idx = 0
while idx < len(nums):
    print(nums[idx])
    idx +=1
    
#Search for the number X in this tuple using loop:
nums= [1,4,9,16,25,36,49,64,81,100]
x = int(input("Enter the number you want to search in list:"))
i =0 
while i<len(nums):
    if(nums[i]== x):
       print("Found at index:",i)
    else:
        print("Finding...")
    i +=1 
    
#Break and Continue 
nums= [1,4,9,16,25,36,49,64,81,100]
x = int(input("Enter the number you want to search in list:"))
i =0 
while i<len(nums):
    if(nums[i]== x):
       print("Found at index:",i)
       break
    else:
        print("Finding...")
    i +=1
print("End")

#Continue-->Acts as skip

i= 0
while i<=5:
    if(i == 3):
        i +=1
        continue
    print(i)
    i +=1
#To print odd and Even
i= 1
while i<=10:
    if(i%2 == 0):# Even
        i +=1
        continue
    print(i)
    i +=1

i= 1
while i<=10:
    if(i%2 != 0):# odd
        i +=1
        continue
    print(i)
    i +=1