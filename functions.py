#sum using function

def calc_sum(a,b): #function definition
    sum = a+b
    print(sum)
    return sum


calc_sum(2,4) #function call
calc_sum(34,6) #function call



#printing a string using function
def str(): #function definition
    print("hello")


str() #function call
str()
str()
str()


#average of three numbers

def average(a, b, c):
    avr = (a+b+c)/3
    print(avr)
    return avr

average(3, 4, 5)

#default value

def product(a=1, b=2):
    print(a*b)
    return a*b

product(3, 5) #give answer according to given arguments
product() #give answer of default values


#Q1
#to print the length of list using function
cities = ["Bareilly", "Noida", "Pune", "Shahjahanpur"]
heroes = ["Thor", "Ironman", "Captain America", "Hulk", "Shaktiman"]

def print_len(list):
    print(len(list))


print_len(cities)
print_len(heroes)        

def print_list(list): #to print the list...... Q2
    for item in list:
        print(item, end=", ")


print_list(heroes) 
print(" ")       
print_list(cities)        


#to calculate factorial using function

def cal_fact(n):
    fact = 1
    for i in range(1, n+1):
        fact *=i
    print(fact)

cal_fact(5)   
cal_fact(3)


#converting USD into INR
def converter(usd_val):
    ind_val = usd_val * 83
    print(usd_val, "USD=", ind_val, "INR")


converter(1)   
converter(100)   
converter(72)
converter(54)   


#even odd using function
def even_odd(n):
    n = int(input("enter a number :"))
    if(n%2 ==0):
        print("EVEN")
    else:
        print("ODD")
  

even_odd(" ")