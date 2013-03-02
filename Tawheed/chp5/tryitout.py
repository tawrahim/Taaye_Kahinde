
firstname = "Tawheed"
lastname = "Raheem"

print "My firstname is ", firstname, "and my last name is ", lastname


fname = raw_input("What is your first name: ")
lname = raw_input("What is your last name: ")
print "Welcome ", fname, " ", lname, "hope you are enjoying python"

fahrenheit = float(raw_input("Type in the temprature in Fahrenheit "))
celsius = (fahrenheit - 32) * 5.0 / 9
print fahrenheit , " degrees fahrenheit to celsius is ", celsius


length = float(raw_input ('length of the room in feet: '))
width = float(raw_input ('width of the room in feet: '))
cost_per_yard = float(raw_input ('cost per square yard: '))
area_feet = length * width
area_yards = area_feet / 9.0
total_cost = area_yards * cost_per_yard
print 'The area is', area_feet, 'square feet.'
print 'That is', area_yards, 'square yards.'
print 'Which will cost', total_cost


quaters = int(raw_input("quaters? "))
dimes = int(raw_input("dimes"))
nickles = int(raw_input("nickles"))
pennies = int(raw_input("pennies"))
change = (quaters*0.25)+(dimes*0.10)+(nickles*0.5)+(pennies*0.1)
print "Your total change is ", change
