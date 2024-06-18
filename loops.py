#to print the table of any number

n = int(input("enter the number whos table you want : "))
i=1
while i<=10:
    print(n*i)
    i +=1

#find the element in tuple using loop
    
nums = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)

x = 36

i = 0 #initialization
while i < len(nums):
    if( nums[i] == x ):
        print("found on index : ", i)
        break #to end the loop when it find the number
    else:
        print("finding...")
    i+=1            

#print the element of the list using loop

nums = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

i = 0
while i < len(nums):
    print(nums[i])
    i +=1



#print numbers from 1 to 100

i = 1
while i<=100:
    print(i)
    i+=1    




#print numbers from 100 to 1

i = 100
while i>=1:
    print(i)
    i-=1        