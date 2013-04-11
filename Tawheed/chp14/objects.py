class Animal:
    def __init__(self, food):
        self.food = food

    def __str__(self):
        print "Hello world! the food is ", self.food
        
    def friends(self):
        if self.food == "grass":
            self.food = "yum yum grass!"
        else:
            self.food = "not tasty!"


cow = Animal("fish")
cow.__str__()

'''
class Animal:
    def __init__(self,food):
        self.food = food
        
    def friends(self):
        if self.food == "grass":
            self.food = "yum yum grass!"
        else:
            self.food = "not tasty!"


cow = Animal("grass")
print cow.food
'''
