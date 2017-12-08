class Store(object):
    def __init__(self, product, location, owner):
        self.product = product
        self.location = location
        self.owner = owner
    
    def add_product(self, product):
        self.product.append(product)
        return self
    
    def remove_product(self, product):
        self.product.remove(product)
        return self

    def inventory(self):
        print "Item count:", len(self.product)
        for item in self.product:
            print item
        return self

    def __repr__(self):
        return "Store location: {}".format(self.location)
    
    

if __name__ == "__main__":
    store = Store(["egg", "ham", "bacon"], "VA", "Tuan")
    store.inventory()
    print ""
    store.add_product("bread")
    store.inventory()
    print ""
    store.remove_product("egg")
    store.inventory()