#print the word meaning in dictionary

dict = {
    "table" :["a piece of furniture", "list of facts & figures"],
     "cat" : "a small animal"
}
    

print(dict)

#number of classrooms required for each subject
subjects = {"python", "java", "c++", "python", "javascript", "java", "python", "java", "c++", "c"}

print("subjects are : ", subjects)
print("classrooms required : ", len(subjects))


#taking marks as input from user and store them in dictonary

marks = {}

sub1 = int(input("enter marks of subject1 :"))
marks.update({"sub1": sub1})

sub2 = int(input("enter marks of subject2 :"))
marks.update({"sub2": sub2})


sub3 = int(input("enter marks of subject3 :"))
marks.update({"sub3": sub3})

print(marks)

values = {9, "9.0"}
print(values)



