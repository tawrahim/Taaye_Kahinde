import random

secret= random.randint(1, 150)
guess = 0
tries = 0

print "AHOY! I'm the Dread Pirate Tawheed, and I have a secret!"
print "It is a number from 1 to 150. I'll give you 10 tries."

while guess != secret and tries < 10:
    guess = input ("What's yer guess? ")
    if guess < secret:
        print "Too low, ye scurvy dog!"
    elif guess > secret:
          print " Too high, landlubber!"
    tries = tries + 1
if guess == secret:
    print "Thunderin' Typhoons! Ye got it alright! Found my secret, ye did! Yer a good fellow!"
else:
    print " Heh Heh Heh! No more guesses ye bilge rat! Ye belong in Davy Jone's Locker ye scervy dog! Heh Heh Heh!!  Better luck next time matey!"
    print "The secret number was", secret
