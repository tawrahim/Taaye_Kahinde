# Try changing the temperature-conversion program from chapter 5 to use GUI input and output instead of raw_input() and print.
#Write a program that asks for your name, then house number, then street, then city, then province/territory/state, then postal/zip code (all in EasyGui dialog boxes).
#The program should then display a mailing-style full address that looks something like this:


purchasePrice = float(raw_input("What is the purchase price: "))
if purchasePrice < 10:
	discount = purchasePrice * .10
	amount = purchasePrice - discount
	print "You got a 10% discount of ", discount, " and you are required to pay ", amount
elif purchasePrice > 10:
	discount = purchasePrice * .20
	amount = purchasePrice - discount
	print "You got a 20% discount of ", discount, " and you are required to pay ", amount

gender = raw_input("What is your gender: ")

if gender == "f":
	age = int(raw_input("How old are you: "))
	if 10 <= age <= 12:
		print "you can play on the team"
	else:
		print "sorry you cant play on the team"
else:
	print "Sorry you need to be a female to be eligible for the team"
