class Bike(object):
    def __init__(self, price, max_speed):
        self.price = price
        self.max_speed = max_speed
        self.miles = 0
    def displayInfo(self):
        print "Bike price is {}, maximum speed is {}, and total miles is {}.".format(self.price, self.max_speed, self.miles)
        return self
    
    def ride(self):
        print "Riding"
        self.miles+=10
        return self

    def reverse(self):
        print "Reversing"
        self.miles-=5
        return self


bike1 = Bike(200, "25mph")
bike2 = Bike(300, "50mph")
bike3 = Bike(100, "20mph")

bike1.ride()
bike1.ride()
bike1.ride()
bike1.displayInfo()

bike2.ride().ride().reverse().reverse().displayInfo()


bike3.reverse()
bike3.reverse()
bike3.reverse()
bike3.displayInfo()
