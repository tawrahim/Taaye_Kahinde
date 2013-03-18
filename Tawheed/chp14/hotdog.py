class HotDog:
    def __init__(self):
        self.cooked_level = 0
        self.cooked_string = "Raw"
        self.condiments = []

    def __str__(self):
	msg = "hot dog"
	if len(self.condiments) > 0:
		msg = msg + " with "
		for i in self.condiments:
			msg = msg + i + " "
	msg = msg.strip(", ")
	msg = self.cooked_string + " " + msg + "."
	return msg

    def cook(self,time):
        self.cooked_level = self.cooked_level + time
	if self.cooked_level > 8:
		self.cooked_string = "charcoal"
	elif self.cooked_level > 5:
		self.cooked_string = "Well done"
	elif self.cooked_level > 3:
		self.cooked_string = "Medium"
	else:
		self.cooked_string = "Raw"

    def addcondiment(self, condiment):
	self.condiments.append(condiment)

myDog = HotDog()
print myDog.cooked_level
print myDog.cooked_string
print myDog.condiments
print myDog
myDog.cook(34)
myDog.addcondiment("onions")
myDog.addcondiment("onions")
myDog.addcondiment("onions")
print myDog
cow = HotDog()
print cow.cooked_level
print "weeeeeeeee!"
print cow
