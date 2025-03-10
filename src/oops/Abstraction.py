"""
Abstraction is the process of hiding internal implementation details
and only exposing the essential features of an object.
"""
from abc import ABC , abstractmethod

#abstract class or abstract base class(ABC)
class shape(ABC):
     @abstractmethod
     def area(self):   #abstract method
      pass

#child class
class rectangle(shape):
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):    #overriding abstract method
       return self.length * self.breadth

    def perimeter(self):   #normal method
        return 2*(self.length + self.breadth)

#object of child class
rect = rectangle(10, 20)
print("area of rectangle is: ", rect.area())

print("perimeter of rectangle is: ", rect.perimeter())

