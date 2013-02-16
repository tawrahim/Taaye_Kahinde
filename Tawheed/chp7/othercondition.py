age = float(raw_input("What is your age: "))
grade = int(raw_input("What is your grade: "))
color = raw_input("Pick a color: ")

if age >= 8 or grade >= 3 or color == "pink":
    print "You can play the game"
else:
    print "Sorry you cant play the game"
