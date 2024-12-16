"""Polymorphism means “many forms.” In Object-Oriented Programming (OOP),
polymorphism allows the same method or operation to behave differently
depending on the object or the context.

It enables code reusability, flexibility, and simplicity by allowing
objects of different classes to be treated as objects of a common superclass.
"""

# Parent class
class Animal:
    def make_sound(self):
        return "Some generic sound"

# Child class 1
class Dog(Animal):
    def make_sound(self):  # Overriding the method
        return "Dog is Barking.."

# Child class 2
class Cat(Animal):
    def make_sound(self):  # Overriding the method
        return "Cat is Meowing.."

# Create objects of child classes
d1 = Dog()
c1 = Cat()
a1=Animal()

# Polymorphic behavior
print(d1.make_sound())  # Calls Dog's method
print(c1.make_sound())  # Calls Cat's method
print(a1.make_sound())