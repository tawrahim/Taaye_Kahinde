import time

#Quesion 1
timer = int(raw_input("Countdown timer: How many seconds? "))
for i in range(timer,0,-1):
    print i
    time.sleep(1)
print 'BLAST OFF'


#Question 2
timer = int(raw_input("Countdown timer: How many seconds? "))
for i in range(timer,0,-1):
    print i,
    for j in range(i):
        print "*",
    time.sleep(1)
    print
print 'BLAST OFF'
