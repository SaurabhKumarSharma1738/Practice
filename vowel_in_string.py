string = input("enter a string : ")

#defining a set of vowel
vowels = set("aeiouAEIOU")

#initializing the counter for vowel
vowel_count = 0
#iterate through each character in string
for char in string:
    if char in vowels:
        vowel_count +=1

print("number of vowel in this string : ", vowel_count)        

