# Tawheed Abdul-Raheem
# chp 15 tryitout!

import time
import random
import print_module
from print_module import c_to_f

print_module.myName()
fahrenheit = c_to_f(78)
print 'Temprature ',fahrenheit

print 'Random int'
for i in range(0,5):
    print random.randint(0,100)

print 'decimai'
sleeper = 0
while (sleeper != 30):
    print random.random()
    time.sleep(3)
    sleeper += 3
