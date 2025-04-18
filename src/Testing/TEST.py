class human:     # class 1: Human class demonstrating Polymorphism
    eye = 2
    hands = 2
    legs = 2
    mouth = 1

    #function human can perform
    def walk(self):
        print("it can walk..")
    def eat(self):
        print("it can eat...")
    def fight(self):
        print("it can fight...")

class animal():   # class 2: Animal class demonstrating Polymorphism
    legs = 4
    eye = 2
    tail = 1

    def sound(self):
        print("animal is mooing..")
    def eat(self):
        print("animal is grazing...")

class bird(human,animal):  # class 3: Bird class demonstrating Inheritance
    wings = 2

    def fly(self):
        print("bird can fly..")


h1 = human()
h1.walk()
h1.fight()

a1 = animal()
a1.eat()
a1.sound()

b1 = bird()
b1.eat()
b1.fly()

# class 4: Some arithmetic functions
def add(a,b):
    return a + b
def mul(a,b):
    return a * b
def div(a,b):
    return a / b

print(add(9,3))
print(mul(9,3))
print(div(9,3))


print("----loops----")

for i in range (2,20,2):
    print(i)

movie = "holly","bolly","tolly","jolly","colly"
for i in movie:
    print(i)


temp = (int(input("Enter temperature: ")))
if temp <= 20:
    print("it is cold today..")
elif temp > 20 and temp < 30:
    print("it is sunny today..")
else:
    print("it is hot today!!!")












