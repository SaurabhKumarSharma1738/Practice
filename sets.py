#SETS...

nums = {1 ,2 , 2, 3, 4, "hello", "world", "world"}

print(nums) #print only unique items
print(type(nums))
print(len(nums)) #total number of unique items

num1 = {} #empty dictionries
print(type(num1))

num2 = set() #empty set
print(type(num2))


#union of sets
set1 = {1, 2, 3,}
set2 = {2, 3, 4,}

print(set1.union(set2)) #will print the union of both sets
print(set1)
print(set2)


#intersection of sets
set3 = {1, 2, 3, 4}
set4 = {2, 3, 4, 5}

print(set3.intersection(set4)) #will print the intersection of sets
print(set3)
print(set4)

