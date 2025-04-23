#1. How would you extract the first 5 characters of the string `"HelloWorld"` using slicing?

word = "HelloWorld"
print(word[0:10:1])

#Given the string `"PythonProgramming"`, how would you slice and extract the last 4 characters?

word1= "PythonProgramming"
print(word1[12:])

#3. For the string `"abcdefg"`, how can you slice the string to get every second character starting from the first?

word3 ="abcdefg"
print(word3[0:8:2])

#4. How can you reverse the string `"Palindrome"` using slicing?

word4 = "Palindrome"
#If you leave the stop part empty (word4[10::-1]), Python keeps going backward until the beginning of the string, and includes everything back to index 0.
print(word4[10::-1]) #slice operation with the syntax string[start:stop:step].


#5. What will be the result of the slicing operation `s[3:]` if `s = "DataScience"`?

s = "DataScience"
print(s[3:])
#This will print 'aScience Only'

#6. How would you extract every second character in reverse order from the string `"abcdefgh"`?

word5 = "abcdefgh"
print(word5[7::-2])

#7. For the string `"ArtificialIntelligence"`, how would you extract the substring `"intelli"` using slicing?

word6 ="ArtificialIntelligence"
a = word6.lower()[10:17:1]
print(a)

#8. Given two strings `str1 = "Hello"` and `str2 = "World"`, concatenate them to form a new string `"HelloWorld".

w1 = "Hello"
w2 = "World"
combined = w1 + w2
print ('New string  is', combined)

#9. Extract the substring `"lowor"` from the string `str = "helloWorld"` using slicing.
word7 = "helloworld"
print(word7[3:8:1])
