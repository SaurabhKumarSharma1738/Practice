#clever if condition
age= int(input("age:"))
vote = ("yes","no") [age<18] #(false_val, true_val)
print(vote)