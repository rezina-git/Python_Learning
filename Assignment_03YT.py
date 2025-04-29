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
list = [1,2,3,2,1]
copy_list= list.copy() 
copy_list.reverse()

if(copy_list == list):
    print("It is palindrome NUmber")
else:
    print("Not a palindrome")

list = ["m","a","a","m"]
copy_list= list.copy() 
copy_list.reverse()

if(copy_list == list):
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
