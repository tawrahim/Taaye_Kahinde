numBlocks = int(raw_input("How many block of stars do you want: "))
for numBlocks in range(1,numBlocks+1):
    print 'the variable numBlocks is: ', numBlocks
    for lines in range(1, numBlocks *2):
        print 'the variable line is: ', lines
        for stars in range(1, (lines + numBlocks)*2):
            print "*",
        print 
    print




























'''

numLines = int(raw_input("How many lines do you want: "))
stars = int(raw_input("How many stars do you want: "))
blocks = int(raw_input("How many blocks do you want: "))


for i in range(0,blocks):
    for j in range(0, numLines):
        for k in range(0,stars):
            print "*",
        print
    print

    #number_lines = int(raw_input("How many lines do you want: "))
stars = int(raw_input("How many stars do you want: "))

for i in range(0, stars):
    print "*",
    
'''
