class Animal(object):
    def __init__(self, name, health):
        self.name = name
        self.health = health
    def walk(self):
        self.health-=1
        return self
    def run(self):
        self.health-=5
        return self
    def display_health(self):
        print "Health:", self.health
        return self

animal = Animal("pet",50)
animal.walk().walk().walk()
animal.run().run()
animal.display_health()

class Dog(Animal): 
    def __init__(self, name, health):
        super(Dog, self).__init__(name, health)
        self.health = 150

    def pet(self):
        self.health+=5
        return self

dog = Dog("dog pet", 50)
dog.walk().walk().walk()
dog.run().run()
dog.pet()
dog.display_health()

class Dragon(Animal):
    def __init__(self, name, health):
        super(Dragon, self).__init__(name, health)
        self.health = 170
    def fly(self):
        self.health-=10
        return self
    def display_health(self):
        super(Dragon, self).display_health()
        print "I am a Dragon"
        return self

dragon = Dragon("big pet", 100)
dragon.display_health()
