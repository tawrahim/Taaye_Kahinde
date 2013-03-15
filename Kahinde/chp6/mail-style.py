import easygui
easygui.msgbox ("This program will be displaying your adress in a mailing-style with full adress")
name=easygui.enterbox("Enter in your full name:")
numstreet=easygui.enterbox("Enter in your house number and street:")
citystate=easygui.enterbox ("Enter your city, then state. Please add a  comma in between them:")
easygui.msgbox("Here is the display...")
easygui.msgbox(str(name) + "\n" + str(numstreet) + "\n" + str(citystate))

            
