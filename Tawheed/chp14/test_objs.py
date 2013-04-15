class Animal:
    def __init__(self, food):
        self.food = food
        self.abu = "Hello America"

    def __str__(self):
        print "Hello world! the food is ", self.food
        
    def friends(self):
        if self.food == "grass":
            self.food = "yum yum grass!"
        else:
            self.food = "not tasty!"

    def tawheed(self):
        blaah = "jd"
        print blaah

cow = Animal("fish")
cow.__str__()
cow.tawheed()
print cow.abu
