#1. Store following word meanings in python dictionary
# table : "a piece of furniture","List of facts and figures"
#cat :"a small animal"
meanings = {
    "table" :  ["a piece of furniture","list of facts and figures"],
    "Cat" : "a small animal"
}
print(meanings)

#2.Your are given a list of subjects for students.Assume one classroom is required
#for 1 subject.How many classrooms are needed by all the students.
#"python","java","C++","python","javascript","java","Python","java,"C++","C"
subjects = {
    "python", "java","c++","python","javascript","java","python","java","c++","c"
}
print(len(subjects))

#3.WAP to enter marks of 3 subjects from the user and store them in dictionary.Start with an empty dictionary and add one by one.Use subject name as key and marks as value.
marks = {}
sub1= input("Enter the marks of phy:")
marks.update({"phy": sub1})

sub2= input("Enter the marks of chem:")
marks.update({"chem": sub2})

sub3= input("Enter the marks of social:")
marks.update({"Social": sub3})

print(marks)

#Figure out way to store 9 and 9.0 as seperate values in the set.
#(You can take help pf built-in data types)
values = { 9, 9.0}
print(values) #o/p: 9 as python treat both values as same.
#SO-->Can be stored as strings
values = {9,"9.0"}
print(values)
#OR--> You can use built-in datatypes.
value = { #Dict(as it is mutable) lai set ko vitra rakhna mildaina so we use tuple.
    ("int",9),
    ("float",9.0)
}
print(value)