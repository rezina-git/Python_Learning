#Function and recurrsion 

#Function Definition
# def calc_sum(a,b): #parameters
#     return a + b 

# sum = calc_sum(1,2) #function call; arguments 
# print(sum)

def print_hello():
    print("hello")
print_hello()
print_hello()
print_hello()
print_hello()
print_hello()#Same kam dheraii choti repeat garera garnu xa vaney we make  function which decreases the redundancy.
            #It is optional to  add  parameters inside the function. Matlab kunaii input lidaina parameter add nagarda ra return ni gardaina.

#Example: Calculate average of three numbers:

def calc_avg(a,b,c):
    sum = a+b+c  #Inside the function there should be always intendation.
    avg = sum/3
    print(avg)
    return avg
calc_avg(97,92,43)

#----------> Built in Functions------->
#To print multiple lines of code in same line
print("Rejeena",end=" ") #sep = " "
print("Budhathoki") #end = \n

#len() range() type ()

#----->User Defined functions---Made by user itself or programmer.

#------>Default Parameters

def cal_prod(a=4, b=2):#Default parameters
    print(a*b)
    return a*b

cal_prod()
#Also can assign only one parameters
def cal_prod(a, b=2):#Default parameters
    print(a*b)
    return a*b

cal_prod(2)

#----->But cannot be assign to  only to second para
# def cal_prod(a=3, b):#Error
#     print(a*b)
#     return a*b

# cal_prod(2) 