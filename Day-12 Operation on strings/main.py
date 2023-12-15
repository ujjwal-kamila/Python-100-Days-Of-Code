#String Slicing & Operations on String
names = "Ujjwal"
# Length of a String
print(len(names)) # prints lenth


fruit = "Mango"
mangoLen = len(fruit)
print("Mango is a", mangoLen, "letter word.")
# print(fruit[0:4]) # including 0 but not 4
# print(fruit[1:4]) # including 1 but not 4
# print(fruit[:5])
# print(fruit[0:-3])
# print(fruit[:len(fruit)-3])
print(fruit[-1:len(fruit) - 3])
print(fruit[-3:-1])


#Loop through a String
alphabets = "ABCDE"
for i in alphabets:
    print(i)
    

# Quick Quiz:
nm = "Harry"
print(nm[-4:-2])  # ans is ar