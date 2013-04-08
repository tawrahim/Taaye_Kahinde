# Code snippets to explain the following 
# break, continue, while and for constructs
sum = 0
i = 0

# Testing the for-loop logic
while (i < 5):
    sum += i
    print sum
    i += 1

# Testing the for loop
for i in range(5):
    sum += i
    print sum

# Test the break logic
for i in range(5):
    if i == 3:
        print "I am going to stop printing and quit the loop"
        break
    print i

# Test the continue logic
while (i < 5):
    i += 1
    if i == 3:
        print "Let go back in the begining"
        continue
    print i
