#use of range function

for i in range(2, 20, 2): #range(start, stop, stepsize)
    print(i) 


# #even number using range function

for i in range(2, 101, 2): #even numbers from 1 to 100
    print(i)    



#odd number using range function

for i in range(1, 101, 2): #odd numbers from 1 to 100
    print(i)        



#number from 1 to 100
for i in range(1, 101):
    print(i)


 #number from 1 to 100
for i in range(100, 0, -1):
    print(i)



#multiplication table of n

n = int(input("enter the number : "))

for i in range(1, 11):
    print(n*i)