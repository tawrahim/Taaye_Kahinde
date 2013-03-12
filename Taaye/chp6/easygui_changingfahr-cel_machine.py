#1 (with extra stuff) :)
import easygui
easygui.msgbox ("This program converts Fahrenheit to Celcius.")
user=easygui.integerbox("Type in the temperature in fahrenheit:")
girl=float(user)
celcius= (girl-32)*5.0/9
easygui.msgbox("The temperture in celcius is  " + str(celcius))
girl=easygui.buttonbox ("Isn't this program great?",
                        choices= ['YES','NO'])
if girl== 'YES':
    easygui.msgbox ("Great! I thought so too! It makes converting temperature easier.")
else:
    easygui.msgbox ("Really? I thought it was helpful!")
    extra=easygui.codebox ("Type in your reply", title= 'Your reply....')
    easygui.msgbox('Oh...good point. I will look into that. Thanks for the reply.....   ' + str(extra))

 

#2
easygui.msgbox("This program will help setup your adress and name in mail-style.")
name= easygui.enterbox ("What is your first name and your last name?")
street= easygui.enterbox ("What is your number and what is your street?")
live= easygui.enterbox ("What town do you live in, and what state or country?")
zip_code= easygui.enterbox ("What is your zip code?")
easygui.msgbox ( name + "\n" + 
                 street + "\n" +  
                 live + "\n" +
                 zip_code)
