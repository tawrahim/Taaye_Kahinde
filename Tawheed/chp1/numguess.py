import random,easygui

secret=random.randint(1,  100)
guess = 0
tries = 0

easygui.msgbox( "Ahoy! I'm the Dread Pirate Roberts, and I have a secret!"
 "It is a number from 1 to 100. I'll give you  only 6 tries.")

while guess != secret and tries <6:
    guess = easygui.integerbox("What's yer guess?  ")
    if guess < secret:
        easygui.msgbox( "Too low, ye scurvy dog!")
    elif guess > secret:
        easygui.msgbox( "Too high, landlubber!")
    tries = tries + 1
if guess == secret:
    easygui.msgbox( "Avast! Ye got it! Found my secret, ye did!" )
else:
    easygui.msgbox( "No more guesses! Better luck next time, matey!" )              
    easygui.msgbox( "The secret number was" + str(secret) )
