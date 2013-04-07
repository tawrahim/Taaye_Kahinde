money=float(raw_input("Enter in amount of money:"))
runit=(money*0.10)
answer=money-runit
run=(money*0.20)
something=money-run
if money <= 10:
    print " Great! You get a 10% discount!"
    print "Your final amount is,",answer
if money > 10:
    print "Great! You get a 20% discount!"
    print "Your final amount is," ,something
print "\n"
print "********************************************"
import easygui
persons=easygui.enterbox("Enter in if you are female, or male.")
if persons=="female":
            easygui.msgbox ("You can be in the Female soccer team.")
else:
            easygui.msgbox ("Sorry, the soccer team is only for females.")
age=easygui.integerbox ("What is your age?")
if age < 12 and age > 10 and persons == "female":
            easygui.msgbox ("YES!! You can be on the team! You are 10 to 12 yrs. old.")
else:
    easygui.msgbox("You definetely can not be in the team. You are not 10-12 yrs. old")
print "\n"
print "*******************************************"
import easygui
tank=easygui.integerbox("Enter in Size of tank:")
full=easygui.integerbox("How much is full in percent?")
liter=easygui.integerbox("Kilometers per liter:")
distance=(full/100.0 *tank)* liter 
easygui.msgbox ("You can go another " + str(distance) + "km")
if distance > 200:
    easygui.msgbox("The next gas station is 200 km away. Get Gas Now!.")
elif distance < 200:
    easygui.msgbox("The gas station is 200 km away. You can wait for the next station.")
print "\n"
print "**************************************"
   
age = float(raw_input("Enter in your age:"))
grade = int(raw_input("Enter in your grade:"))
if age >= 8:
    if grade >=3:
        print "You can play this game."
else:
    print "Sorry, you can't play the game. You're too petite"

age = float(raw_input("Enter your age:"))
if not(age<8):
    print "You're allowed to play this game."
else:
    print "Sorry, you can't play the game."
