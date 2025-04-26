#EX.1 : Add a person with name Tony stark.
#Tonny's age is 52 years old.
#Tony is genius.

name = "Tony stark "
age = 52
is_genius = True
print(name)
print(age)
print(is_genius)
#Takiing input from user
#Ex.2 Tony is seceretly a Superhero.Ask him for his superheroname and show iton the terminal.
a = input("What is your Superhero title? ")
print("Hello! iam " +  a + ".") 

#Type Conversion (It is required in pyton because all inputs in python comes in strings format )
old_age = input ("Enter your age:")
new_age = int(old_age) + 2
print(new_age)
#Also can be converted into float(),str(),bool()
#EG: Print the sum of two numbers from taking input from user
first = input("Enter first number :")
second =input("Enter second Number :")
sum = int(first) + int(second)
print("The sum is :"+ str(sum))

#Strings Methods
name = "Tony Stark"
print(name.find('S'))
print(name.replace("Tony Stark","IronMan"))# Characters can also be replaced
print(name.replace("T","R"))

#Types of Operators
#An operator is symbol that performs a certain operatio between Operands.
#Arithmetic operators a certain Operations between operands.
#Arithematic Operators(+,-,*,/,%,**)
#Relational/Comparison Operators(==, !=, >,<,>=,<=)
#Assignment Operators(=,+=,*=,/=,%=,**=)
#Logical Operators(Not,And,or)

#Assignment Operators 
num = 10
# num = num + 10
#short form num += num and ** is power operator
num **=5 #(Means  10 to the power 5)
print("Num:", + num) 

#Logical Operators
print (not False)# O/p : True
print (not True)#O/p : False

#not operators works on single operand
a = 300
b =200
print(not(a>b)) #O/p: false as condition is true.
#And and Or operators works on two operands.
val1 = True
val2 = False
print("AND Operator :", val1 and val2) # Ans is false if any one of value is false then answer will be false to be true both should be true.
print("OR Operator :", val1 and val2) # Ans  is True as one value is true
print("OR Operator :", (a==b) or (a>b)) # Ans is True , if anyone is true then it will be true