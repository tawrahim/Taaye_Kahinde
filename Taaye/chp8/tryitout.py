#Taaye Giwa
#question 1
number = int(raw_input("Which multiplication table would you like?"))
print "Here's your table:"
for looper in range(1,11):
    print looper,"*",number,"=", looper* number     #Displays loop
print "\n"                                          #Creates new line



print "Which multiplication table would you like?"
number = 1
random= int(raw_input())
while(number<=10):
    print number, "*", random,"=", random*number
    number +=  1



print "Which multiplication table would you like?"
table_number= int(raw_input())
print "How high would you like it to go?"
table_range= int(raw_input())
for looper in range(0,table_range):
    print looper, "*", table_number,"=", looper*table_number
    


print "Which multiplication table would you like?"
number = 0
table_number= int(raw_input())
print "How high would you like it to go?"
table_range= int(raw_input())
while(number<table_range):
    print number, "*", table_number,"=", number*table_number
    number+=1
    
