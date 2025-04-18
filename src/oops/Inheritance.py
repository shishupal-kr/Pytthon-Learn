"""
It allows one class (child class) to inherit properties and methods from another class (parent class).
This promotes code reusability, polymorphism, and modularity.
"""
# Parent classes
class Father:
    def skill(self):
        return "Driving"

class Mother:
    def mother_skill(self):
        return "Cooking"

# Child class (inherits from Father and Mother)
class Child(Father, Mother):
    def own_skill(self):
        return "Coding"

#object of child class
child = Child()

# Access skills from both parent classes and child class
print("Father's skill:", child.skill())
print("Child's own skill:", child.own_skill())
print("mother's own skill:", child.mother_skill())