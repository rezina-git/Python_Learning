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
#An oprator is symbol that performs a certain operatio between Operands.
#Arithmetic operators a certain Operations between operands.
#Arithematic Operators(+,-,*,/,%,**)
#Relational/Comparison Operators(==, !=, >,<,>=,<=)
#Assignment Operators(=,+=,*=,/=,%=,**=)
#Logical Operators(Not,And,or)