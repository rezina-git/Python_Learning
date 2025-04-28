# Whatever we write inside the input it takes as string so if we have to write other data we have to use type casting.
val = input ("Enter some value:")
print(type(val),val) # if you type 33 here it gives its type as string so  we  surround input with the type we want to acess.
val =int(input ("Enter some value:")) 
print(type(val),val)

name = str(input("Enter Your Name:"))
age = int(input("Enter your age:"))
marks = float(input("Enter your marks:"))
print("Welcome! My Name is:",name)
print("Age=", age)
print("Marks=",marks)

#Ex2: WAP to input the side of square and print its area.
side = int(input("Enter one side of square:"))
side *=side
print("The area of square is:",side)
#Ex3: WAP to input 2 floating point numbers and print their average.
f1 = float(input("Enter the first number:"))
f2 = float(input("Enter the second:"))
print("Average is :",(f1 + f2)/2)
#Ex 4: WAP to input 2 int numbers, a snd b.Print True if a is greater than or equal to b.If not print false.
a = int(input("Enter fist num:"))
b = int (input("Enter the second num:"))
print(a>=b)

#Control Statements
light = "green"

if(light=="red"):
    print("Stop")
elif(light == "green"):
    print("GO")
elif(light == "Yellow"):
    print("Look")
else:
    print("Light is broken")
#else is always written in last that means if all above above condition is wrong then else statement will run.

#Grade students based on marks:
#marks>=90, grade = "A"
#90>marks>=80, grade = "B"
#80>marks>=70,grade = "C"
#70>marks,grade ="D"

marks = int(input("Enter the marks:"))
if (marks>=90):
    print("Grade A")
elif(marks>90 and marks>=80):
    print("Grade B")
elif(marks>80 and marks>=70):
    print("Grade C")
else:
    print("Grade D")
    
#EX 5: 
#WAP to check if a number entered by the user is ODD or EVEN
num = int(input("Enter a number:"))
if(num%2==0):
    print("NUmber is EVEN")
else:
    print("ODD")
    
#WAP to find the greatest of three numbers entered by the user.
a = int(input("Enter a first num:"))
b = int(input("Enter a second num:"))
c = int(input("Enter third num:"))
if(a>b and a>c):
    print("A is greatest",a)
elif(b>c and b>a):
    print("B is greatest",b)
else:
    print("C is greatest",c)

#WAP to check if a number is multiple of 7 or not.

D = int(input("Enter a num to check is it multiple of 7:"))
if (D%7 == 0):
    print("Number is multiple of  7")
else:
    print("NOt a multiple of 7")