class car:
#this is constructor, self is used by all programmer for common purpose but you an also change name
    def __init__(self,company):
        self.company = company
        print("car is created")

    # this is method/function for car class
    def drive(self):
        print("car is now in driving mode")
    def stop(self):
        print("car is now in stopping mode")
    def park(self):
        print("car is now in parking mode")


car1 = car("toyota")
car1.drive()
(car1.park())