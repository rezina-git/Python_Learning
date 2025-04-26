#1. fruits = ["apple", "banana", "cherry", "date", "elderberry"]
# What is fruits[0]?
# What is fruits[-1]?
# What is fruits[2]?

#Answer: fruitd[0] = apple
fruits = ["apple", "banana", "cherry", "date", "elderberry"]
print(fruits[0])
print(fruits[-1])#elderberry
print(fruits[2])#Cherry

#2. numbers = [10, 20, 30, 40, 50, 60]
# Access the third element.
# Access the last element.
# Access the second-to-last element.
numbers = [10, 20, 30, 40, 50, 60]
print(numbers[2])
print(numbers[-1])
print(numbers[1:])

#3. colors = ["red", "green", "blue", "yellow", "purple", "orange"]

# Extract the first three elements.
colors = ["red","green","blue","yellow","purple","orange"]
print(colors[0:3])
# Extract the last two elements.
print(colors[4:6])
# Extract every second element.
print(colors[0::2])
# Reverse the list using slicing.
print(colors[::-1])

# 4.letters = ["a", "b", "c", "d", "e", "f", "g", "h"]
# Extract ["c", "d", "e"]
# Extract ["a", "c", "e", "g"]
# Extract ["h", "f", "d", "b"]
letters = ["a", "b", "c", "d", "e", "f", "g", "h"]
print(letters[2:5])
print(letters[::2])
print(letters[-1::-2])

#5.numbers = [1, 2, 3, 4, 5, 6] Change the third element to 99
numbers = [1, 2, 3, 4, 5, 6]
numbers[2] = 99
print(numbers)

#5. words = ["Python", "is", "a", "great", "programming", "language"]
# Extract the words "is a great" using slicing.
# Reverse the order of words.
words = ["Python", "is", "a", "great", "programming", "language"]
print(words[1:4:1])
print(words[::-1])

str = "apple,banana,orange"
fruits = str.split(",")#Comes inside bracket in list seperated by comma.
print(fruits)

my_list = [1,2,3]
new_list = my_list*3 # 1,2,3  comes in three times
print(new_list)

#mutable= Original data changeable
#EG: Change value of 2 to Hi
my_list[1]="Hi"
print(my_list)
#String is immutable so there we use replace but list is mutable so indexwise value is repalced.


