# Tawheed Abdul-Raheem
# chapter14 tryitout

class BankAccount:
	def __init__(self, name, account_number ):
		self.name = name
		self.account_number = account_number
		self.balance = 0.0 
	
	def show_balance(self):
		if self.balance < 10:
			print "Your balance is low, you only have $", self.balance, " in your account"
		else:
			print "You have $", self.balance , " in your account "
	
	def make_deposit(self, money):
		self.balance = self.balance + money
		print "Your new balance is $", self.balance
	
	def make_withdrawals(self, amount):
		if self.balance >= amount:
			self.balance = self.balance - amount
			print "You just took $", amount, " out of your account and your new balance is ", self.balance
		else:
			print "You do not have sufficient funds in your account"

class InterestAccount(BankAccount):
	def addIntrest(self,rate):
		intrest = self.balance * rate
		self.make_deposit(intrest)

banky = BankAccount("chase", 9788383848) 
banky.show_balance()
banky.make_deposit(10)
banky.show_balance()
banky.make_withdrawals(5)
banky.show_balance()
intrest = InterestAccount("city",9876579)
intrest.make_deposit(84)
intrest.addIntrest(4)
