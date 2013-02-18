# Question 1 
purchasePrice = float(raw_input("What is the purchase price: "))
if purchasePrice < 10:
	discount = purchasePrice * .10
	amount = purchasePrice - discount
	print "You got a 10% discount of ", discount, " and you are required to pay ", amount
elif purchasePrice > 10:
	discount = purchasePrice * .20
	amount = purchasePrice - discount
	print "You got a 20% discount of ", discount, " and you are required to pay ", amount

print "\n\n\n"


# Question 2
gender = raw_input("What is your gender: ")
if gender == "f":
	age = int(raw_input("How old are you: "))
	if 10 <= age <= 12:
		print "you can play on the team"
	else:
		print "sorry you cant play on the team"
else:
	print "Sorry you need to be a female to be eligible for the team"

print "\n\n\n"


# Question 3
size_of_tank = float(raw_input("Size of tank: "))
percent_full = float(raw_input("Percent full: "))
km_per_liter = float(raw_input("km per liter: "))

