class car:

#this is constructor, self is used by all programmer for common purpose but you an also change name
    def __init__(self,company):
        self.company = company
        print("car company is: ",company)

    # this is method/function for car class,which is object level function/method
    def drive(self):
        print("car is now in driving mode")
    def stop(self):
        print("car is now in stopping mode")
    def park(self):
        print("car is now in parking mode")

#car1 is object of car class
car1 = car("bmw")
car1.drive()
car1.park()

car2 = car("toyota")
car2.drive()
car2.park()