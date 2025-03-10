a = "demographic"
b = "Detail"
print (a+b)

print(a.capitalize())
print(b[0:4])


name = str(input("Enter you name: "))
age = input("Enter your age: ")

print("Your name is: ",name , "& Your age is: ",age)


age =int(input("Enter you age: "))
if(age == 18):
    print("Adult")
if(age >= 25):
    print("you are a man")
elif(age >= 13 or age < 18):
    print("you are a teen!!")
else:
    print("your are a child!!!")


