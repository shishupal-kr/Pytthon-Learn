class car:
    def __init__(self,company):
        self.company = company

s1=car("bmw")
s2=car("toyota")

print(s1.company)
print(s2.company)

del s1.company
print(s1.company)