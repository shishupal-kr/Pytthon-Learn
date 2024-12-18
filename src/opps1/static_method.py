class Bike:
    company = "Bajaj"
    model = "Pulsar 150"

    @staticmethod
    def start():
        return "Bike has started"
    @staticmethod
    def stop():
        return "Bike has stopped"
    @staticmethod
    def self ():
        return "Bike ready to go"

#static method/function is class level method/function
b1 = Bike()

print(b1.start())
print(b1.stop())

print(Bike.company)
print(Bike.model)

b2 = Bike()
print(b2.self())
print(b2.self)  #location of self method in memory