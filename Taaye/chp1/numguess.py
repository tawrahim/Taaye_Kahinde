import random

secret=random.randint(1,  100)
guess = 0
tries = 0

print "Ahoy! I'm the Dread Pirate Buck Beak, and I have a secret!"
print "It is a number from 1 to 100. I'll give you  only 7 tries."

while guess != secret and tries <6:
    guess = input("What's yer guess?  ")
    if guess < secret:
        print "Too low, ye scurvy dog!"
    elif guess > secret:
        print "Too high, landlubber!"
    tries = tries + 1
if guess == secret:
    print "UUUH FOOEY! Ye finally got it! Found my secret, ye did, ye remind me of the time when me friend Donkey and I were on one of our adventures to get past a troll and he asked many many questions but I still got them right! Well any ways the point is good job!" 
else:
    print "No more guesses! Ye lost! The secret number was none of your beeswax  (something we pirates say these days).... ok stop givin me those googoo eyes heres the secret number", secret               
    
