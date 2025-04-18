class human:
    eye = 2
    hands = 2
    legs = 2
    height = "5'"

    #function human can perform
    def walk(self):
        print("Human can walk..")
    def eat(self):
        print("Human can eat...")
    def fight(self):
        print("Human can fight...")


class animal(human):
    legs = 4
    eye = 2

    def sound(self):
        print("animal is making sound..")

h1 = human()
h1.walk()
h1.fight()

a1 = animal()
a1.eat()
a1.sound()

#some function
def add(a,b):
    return a + b
def mul(a,b):
    return a * b
def div(a,b):
    return a / b

print(add(9,3))
print(mul(9,3))
print(div(9,3))














