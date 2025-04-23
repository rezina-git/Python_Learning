#Variables(we use variables to store data temporarily in computers memory, use small letters to declare variables)

#Eg.1--We check in a patient named Jhon Smith.He's 20 Years old and is new patient.

name = 'Jhon Smith'
age = 20
is_newpatient = True
print(name,age,is_newpatient) 

#Taking input from user
name1 =  input('What is your name? ')
print('Hi '+ name1) # Joining two strings with + operator
#Eg.2-- Ask two questions: person's name and favourite color.Then, print message like "Preson name likes this color"
name2 = input ('What is your name? ')
color = input('What is your favourite color?')
print(name2 +' likes '+ color)

#Type conversion
#Program that will ask the year that we born in and then it will calculate our age and print on the terminal.
birth_year = input ('Birth year: ')
print(type(birth_year))
age = 2025-int(birth_year)
print(type(age))# Whenever we use the input function,you always get string ,so if you're expecting a numerical value you should always convert that string into an integer or a float.
print(age)

#E.g03 Ask a user their weight(in pounds),Convert it to Kilograms and print on the terminal.
weight = input("Your weight in pounds:")
weight_kg = int(weight) * 0.45
print(weight_kg)