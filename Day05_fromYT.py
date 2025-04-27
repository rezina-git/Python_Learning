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
