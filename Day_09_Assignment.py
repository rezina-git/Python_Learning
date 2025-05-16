#Wap to print the length of the list .(List is  the parameter)
#wap to print the elements of list in a single line.(List is the parameter)
#Wap to find the factorial of n (n is parameter)
#Wap to cinvert USD to NPR

#1.#Wap to print the length of the list.(List is  the parameter)

a = ["apple","mango","orange"]
b = ["Potato","Cabbage","Cauliflower","Maize"]
def print_len(list):
    print(len(list))

print_len(a)
print_len(b)

#2.wap to print the elements of list in a single line.(List is the parameter)

b = ["Potato","Cabbage","Cauliflower","Maize"]
def print_list (list):
    for item in list:
        print(item, end = " ")
print_list(b)

#3.Wap to find the factorial of n (n is parameter)
n = 5
def cal_fact(n):
    fact = 1
    for i in range(1,n+1):
        fact *= i
    print(fact)
cal_fact(n)

#4.#Wap to convert USD to NPR

def converter(usd_val):
    NPR_val = usd_val *135
    print (usd_val, "USD=", NPR_val, "NPR")
converter(300)

