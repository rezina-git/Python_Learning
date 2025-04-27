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
