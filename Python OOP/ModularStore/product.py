class Product(object):
    def __init__(self, name, price, weight, brand):
        self.price = price
        self.name = name
        self.weight = weight
        self.brand = brand
        self.status = "for sale"

    def Sell(self):
        self.status = "sold"
        return self
    def Addtax(self, tax):
        return self.price * (1+tax)

    def Return(self, reason):
        if reason is "defective":
            self.status = reason
            self.price = 0
        if reason is "new":
            self.status = "for sale"
        if reason is "opened":
            self.status = "used"
            self.price*=.80
        return self
    def DisplayInfo(self):
        print "Item Name:", self.name
        print "Price:", self.price
        print "Weight:", self.weight
        print "Brand:", self.brand
        print "Status:", self.status
        print ""
        return self

    def __repr__(self):       
        return "Item Name: {}".format(self.name)

if __name__ == "__main__":
    item = Product("PC", 600, "3lbs", "HP")
    item.DisplayInfo()
    item.Sell()
    item.DisplayInfo()
    item.Return("new")
    print item.Addtax(0.2)
    item.DisplayInfo()