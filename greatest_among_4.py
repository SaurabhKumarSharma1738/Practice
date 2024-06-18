a = int(input("enter the first number : "))
b = int(input("enter the second number : "))
c = int(input("enter the third number : "))
d = int(input("enter the fourth number : "))

if(a>=b and a>=c and a>=d):
    print("the greatest number is : ",a)
elif(b>=c and b>=d):
    print("the greatest number is : ",b)
elif(c>=d):
    print("the greatest number is : ",c)
else:
     print("the greatest number is : ",d)
