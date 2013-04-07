import easygui
secret="Tawheed"
year=23
name=easygui.enterbox ("What is your name?")
if name == secret:
    str(easygui.msgbox ("Are you the birthday boy?"))
else:
   easygui.msgbox ("You are not the birthday boy. Sorry, no cake for you!")
number=easygui.integerbox("How old are you going to be on your birthday?")
if number==year:
    easygui.msgbox("You are the birthday boy! Blow the candles!Hip-hip-Hooray!Yay!")
else:
    easygui.msgbox ("You are dfinetly not the birthday boy! Too bad!")
    
