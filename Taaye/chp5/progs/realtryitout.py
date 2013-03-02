#1
firstname = "Taaye"
lastname= "Giwa"
print "Hello my name is ,",firstname, lastname
print "************************************************\n"
#2
firstname= raw_input("Type in your first name:")
lastname= raw_input("Type in your last name:")
print "Hello",firstname,lastname,"How are you."
print "************************************************\n"
#3
base= int(raw_input("Type in your first demention for the area of your carpet:"))
height = int(raw_input("Type in your second demention:"))
product= base*height
print "The area of your carpet is,",product,"sq. ft." 
print"*****************************************************\n"
#4
square_yard=9
money =float(raw_input("How much is the cost of 1 square yard(9sq.ft.)?"))
base= float(raw_input("Type in the first demention of your carpet"))
height= float(raw_input("Type in your second demention:"))
area_feet= (base*height)
area_yards=float(area_feet)/9
cost = (area_feet)*money
print "The cost is,", cost
print "The answer is in square feet",area_feet
print "The area in yards", area_yards
print "***********************************************************\n"
#4

quarter= int(raw_input("Type in how many quaters you have:"))*25
print quarter
dimes= int(raw_input("Type in your dimes:"))*10
nickles= int (raw_input("Type in your nickles:"))*5
pennies= int(raw_input("Type in your pennies:"))*1
total= quarter+dimes+nickles+pennies
print "This is your total change,", total
