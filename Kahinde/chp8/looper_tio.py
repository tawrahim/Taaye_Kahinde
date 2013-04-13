#Kainde's work,Chapter 8,tryitout,question1
number=int(raw_input("Hello, what table should I display? Type in a number:"))
print "Here is your table:"
for looper in range(number):
    print looper, "*",number,"=",looper*number
print "\n*************************************"




#Chapter 8,tryitout,question2
number=int(raw_input("Hello, what table should I display? Type in a number:"))
print "Here is your table:"
j=0
while (j<5):
    print j,"*",number,"=",j*number
    j=j+1
print "\n**************************************"



#Chapter 8,tryitout,question3
number=int(raw_input("Which multiplication table would you like?"))
number1=int(raw_input("How high do you want to go?"))
for looper in range(number1):
    print looper, "*",number,"=",looper*number
    if looper==number1:
        break
print "\n**************************************"





number=int(raw_input("Which multiplication table do you want?"))
number1=int(raw_input("How high do you want to go?"))
k=0
while k<number1:
    print number,"*",k,"=",number*k
    k+=1
