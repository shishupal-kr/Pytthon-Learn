class mac:
    company = "apple"
    model = "macbook air"

#create a object of our mac class
mac1 = mac()

print(mac1.company)
print(mac1.model)

#2nd class
class car:
    company = "toyota"
    model = "corolla"

    # this is method/function for car class
    def drive(self):
        print("car is now in driving mode")
    def stop(self):
        print("car is now in stopping mode")
    def park(self):
        print("car is now in parking mode")

car1 = car()
car1.drive()
car1.stop()
car1.park()