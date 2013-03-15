import easygui
easygui.msgbox("This program will convert fahrenheit to celsius when you type in a temperature in fahrenheit.")
fahren_temp=easygui.integerbox("Enter temperature:")
box=float(fahren_temp)
celsius=box*5.0/9
easygui.msgbox ("That's your answer,   " + str(celsius))
