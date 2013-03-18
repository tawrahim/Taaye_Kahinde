
class Game_object:
	def __init__(self,name):
		self.name = name
	
	def pickUp(self):
		pass
		# put the code here to add the object
		# to the player's collection
	
class Coin(Game_object):
	def __init__(self, value):
		Game_object.__init__(self)
		self.value = value
	
	def spend(self, buyer, seller):
		pass
		# put the code here to remove the coin from
		# from the buyers money and
		# add it to the seller's money
