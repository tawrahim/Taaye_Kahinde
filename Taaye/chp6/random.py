# Taaye
# Ha Ha my program is better!
import easygui
easygui.msgbox ("This program helps you convert percentages to letter grades.")
user_percentage=easygui.integerbox("Type in your percentage grade.")
if 90<=user_percentage<=100:
    easygui.msgbox(" Your letter grade is an A")
elif 80<=user_percentage<=89:
    easygui.msgbox("Your letter grade is a B")
elif 70<=user_percentage<=79:
    easygui.msgbox("Your letter grade is a C")
elif 60<=user_percentage<=69:
    easygui.msgbox ("Your letter grade is a D")
else:
    easygui.msgbox ("Your letter grade is a F")
