#sum upto n numbers... Q1

n = int(input("enter the number : "))
sum = 0

for i in range(1, n+1):
     sum +=i

print("total sum : ", sum)  #by for loop


#above same question by while loop Q2

n = int(input("enter the number : "))
sum = 0
i = 1
while i <= n:
     sum +=i
     i+=1

print("total sum upto n: ", sum)    


#factorial upto n numbers... Q3

n = int(input("enter the number : "))
fact = 1

for i in range(1, n+1):
     fact *=i

print(" factorial is : ", fact)  #by for loop


#above same question by while loop Q4

n = int(input("enter the number : "))
fact = 1
i = 1
while i <= n:
     fact *=i
     i+=1

print("factorial: ", fact)   