"""
It refers to hiding the internal details of an object and restricting access
to its data. This is achieved by making the data (attributes) private
and accessing it through getter and setter methods.
"""

class student:
    def __init__(self,name,age):
        self.__name = name #private name variable
        self.__age = age

    #to get private variable eg-name
    def get_name(self):
        return self.__name
    def get_age(self):
        return self.__age

    #to set private variable eg-name
    def set_name(self,name):
        self.__name = name
    def set_age(self,age):
        self.__age = age

s1 = student("Rukkhi",20)

#prin name before by get method
print(s1.get_name())
print(s1.get_age())

#set name by set method
s1.set_name("Nirma")
s1.set_age(24)

#print name after by set method
print(s1.get_name())
print(s1.get_age())