# Tawheed Abdul-Raheem
# Chapter 13 tryitout!

#Question1
def myName():
    print ("TTTTTTTTT         A        www         www   H        H   EEEEEEE     EEEEEEEE    DDDDDDD")
    print ("     T          A  A        W           W    H        H   E           E           D       D ")   
    print("     T         AAAAAAA      W           W    HAHHHHHHHH   EEEEEEE     EEEEEEEE    D        D")
    print("     T        A       A     W     WW    W    H        H   E           E           D       D ")
    print("     T       A         A    W    W  W   W    H        H   E           E           D      D")
    print("     T       A         A    W           W    H        H   EEEEEEE     EEEEEEE     DDDDDD")

for i in range(3):
	myName()
	print ("\n\n\n")

#Question2
def info(name,address,street,city,country):
	print "Name: ", name
	print "Address: ", address
	print "Street: ", street
	print "City:  ", city
	print "Country: ", country

# Question4 - nothing really :-)

# Question 4
def coinAdder(quaters,dimes,nickles, pennies):
	total = quaters + dimes + nickles + pennies
	return total

quaters = float(raw_input("quaters: ")) * .25
dimes = float(raw_input("dimes: ")) * .10
nickles = float(raw_input("nickles: ")) * .05
pennies = float(raw_input("pennies: ")) * .01

total = coinAdder(quaters,dimes,nickles,pennies)
print "The total is $",total

