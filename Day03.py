#replace
w= "My name is Reju"
j= w.replace("Reju","Rejeena")
print(j)

#strips() = It removes space from front and tail.
a = "!!wel come!!"
# b= a.strip() removes front and  tail back space.
# b= a.removesuffix("!!")
b= a.removeprefix("!!")
print(b)

#center
a = "My name is Reju"
b = a.center(80,"*")
print(b)

#Sequence Datatype
#list= Data structure or data format , data is stored in group fromat in list,data seperated by comma.
#List is Mutable(Original data is changrable, It allow duplicate value, order) 
a ="We are family"
print(len(a))

a = [12,67.90,34,"hello","world"]
print(type(a))
print(a)
print(len(a))

#indexing in list : Jun data order ma hunxa tesma indexing or slicing use garna painxa but not in unorder.
print(a[3]) # Prints hello
print(a[-1]) # prints world 
#Slicing in list  : If you need parts of list use slicing.
print(a[0:3:1])
print(a[3][0])#prints h
print(a[3][-1])#prints o
print(a[-1][0])#prints w
print(a[3][0:3])#prints hel
