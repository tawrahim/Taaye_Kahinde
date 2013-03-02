print "First Question:"
firstname="Kahinde"
lastname="Giwa"
print "Hello,my name is,",firstname,lastname
print "\n\n\n"
print "**************************\n"
firstname=raw_input("Enter your first name please:")
lastname=raw_input("Now enter your lastname:")
print "You entered",firstname,"for your firstname,"
print "And you entered",lastname,"for your lastname"
print "Hello,",firstname,lastname,".How do you do?"
print "\n\n\n"
print "**************************\n"
print """Tell me the dimensions of a rectangular room
and I will give you the amount of carpet you need for that room."""
length=int(raw_input("What is the length?"))
width=int(raw_input("Now what is the width?"))
print "You entered,",length,"for the length."
print "And you entered,",width,"for the width."
answer=length*width
print "The answer is,",answer
print "So that's the amount of carpet you need for your floor",answer
print "\n\n\n"
print "**************************\n"
print """Tell me the demensions of a rectangular room and I will give
you the amount of money you need for that room in yards and feet"""
length=float(raw_input("What is the length?"))
width=float(raw_input("Now what is the width?"))
money=float(raw_input("What is the amount of money for each sq. yd."))
area_ft=length*width                    
yards=area_ft/9.0
cost=float(area_ft*money)
print "The area is," ,int(area_ft),"in feet."
print "The area is,",yards,"in yards."
print "The cost is,",cost
print "\n\n\n"
print "**************************\n"
print "I will ask you to give me your change so I can add it up for you."
quarter=int(raw_input("Enter in how many quarters:"))*25
dime=int(raw_input("Enter in how many dimes:"))*10
nickel=int(raw_input("Enter in how many nickels:"))*5
penny=int(raw_input("Enter in how many pennies:"))*1
formula=quarter+dime+nickel+penny
print "For change,you have",formula,"cents"

