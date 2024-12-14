#function means it is like a formula to reuse again n again without writing code again

def sum(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def avg(a, b, c):
    return (a + b +c) / 2


print(sum(4, 5))
print(sub(10, 5))
print(mul(6, 5))
print(avg(10, 20, 30))



#define function 1 time use many time eg:-  print(),type(),len()
#it return none because function doesn't return anything
#function is like method in java,
def hi():
    print("hi coder")
print(hi())

#or
name = "shishupal"
def greet():
    print("Hello ",name)
print(greet())