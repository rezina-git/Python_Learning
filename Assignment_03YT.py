#WAP to ask the user to enter names of their 3 favorite movies and store them in list.
movies = []
movi1 = str(input("Enter the name of first fav movi:"))
movi2 = str(input("Enter the name of second fav movi:"))
movi3 = str(input("Enter the name of third fav movi:"))
movies.append(movi1)
movies.append(movi2)
movies.append(movi3)
print(movies)
#OR
movies = []
movies.append(input("Enter 1st movi:"))
movies.append(input("Enter 2nd movi:"))
movies.append(input("Enter 3rd movi:"))
print(movies)

#WAp to check if a list  contains a palindrome of elements.(Hint: Use copy()Method )
#Examples [1,2,3,2,1] or [1,"abc","abc",1]
list1 = [1,2,3,2,1]
copy_list1= list1.copy() 
copy_list1.reverse()

if(copy_list1 == list1):
    print("It is palindrome NUmber")
else:
    print("Not a palindrome")

list1 = ["m","a","a","m"]
copy_list1= list1.copy() 
copy_list1.reverse()

if(copy_list1 == list1):
    print("It is palindrome")
else:
    print("Not a palindrome")

#WAP to count the number of students with "A" grade in following tuple
# ["C","D","A","A","B","B","A"]

num = ("C","D","A","A","B","B","A")
std = num.count("A")
print(std)

#OR------
num = ("C","D","A","A","B","B","A")
print(num.count("A"))

#Store the above values in a list and sort them from "A" to "D"
Grade = ["C","D","A","A","B","B","A"]
Grade.sort()
print(Grade)

#Dictionary in python
#Used to store data values in key:Value pairs.
#keys are not repeated but values can be.
info = {
    "key": "value",
    "name": "Kankai",
    "Learning": "School",
    "age":"34",
    "is_adult": True,
    "12.9" :"12.9",
    "topics":("dict","set"),
    "marks":[95,87,98]
}
# print(info)
# print(type(info))

info["name"]= "Reji"
info["Surname"] = "Budhathoki"
print(info)
#To print empty dictionary
null_dict ={}
print(null_dict)

#nested dictionaries
student = {
    "name": "Sanjay",
    "Subjects": {
        "phy": 87,
        "Chem": 98,
        "Math": 95
    }  
}
print(student)
print(student["Subjects"])
print(student["Subjects"]["Chem"])

#Dictionary Methods
#1.To print all the keys:
print(list(student.keys()))
#To print numbers of keys
print(len(student))
#or
print(len(list(student.keys())))
#2.dict.values--> Prints all values
print(student.values())
print(list(student.values()))
#3.dict.items()--->Returns all (key,values) pairs as tuples.
print(student.items())
print(list(student.items()))
#To Access these values  of list individually:
pairs = list(student.items())
print(pairs[0])
#4.dict.get("key")--->Returns the key according to value.
#This is more suitable way to write than above one and industry oriented.
