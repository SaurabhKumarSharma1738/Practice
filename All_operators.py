#Arithematic operators(+, -, /, %, *, **)

a=50
b=20
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a % b)
print(a ** b)


#Rlational opereators (==, !=, >=, >, <=, <)

a=50
b=20
print(a == b) #False
print(a != b) #True
print(a >= b) #True
print(a > b) #True
print(a <= b) #False
print(a < b) #False

#Assignmant operator (=, +=, -=, /=, %=, **=)

num=10
num = num + 10 #this and next line have same meaning
num+= 10 #this
print("new_num : ", num)

num=10
num -= 10 
print("new_num : ", num)

num=10
num *= 10 
print("new_num : ", num)
num=10
num /= 10 
print("new_num : ", num)
num=10
num %= 10 
print("new_num : ", num)

num=10
num **= 10 
print("new_num : ", num)

#Logical operators (and, not, or)
#works on boolean value(True, False)

print(not False) #True
print( not True) #False

a=50
b=20
print(not (a>b))