things = []
name = raw_input("What is your name: ")
email = raw_input("what is your email: ")
phone = raw_input("what is your phone: ")
things.extend([name,email,phone])
print things
print things.index('tawheed')
if "tawheed" in things:
    print "I love you Tawheed"
else:
    print "Sad face"
