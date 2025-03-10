input("Enter your name : ") #input() without variable
Age = input("Enter you age: ") #input with variable
print("Your age is ", Age)

#default value of input is string type
#if you want to take input specific type of data
# use int(input())

name = str(input("Enter Your Name: "))
age = int(input("Enter Your Age: "))
dob = float(input("Enter Your DOb MM.YYYY: "))

print("your name is ",name)
print("you are",age ,"years old")
print("your Date of birth is ",dob)