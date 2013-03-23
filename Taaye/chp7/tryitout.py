# Taaye Giwa
#This code helps take the per centage off the price.
# No mistakes
import easygui
user_money= float(raw_input("How much are your items in total? "))
percent1= user_money - (user_money * 0.1)
percent2= user_money-(user_money * 0.2) 
if user_money < 10:
    print percent1, "  is how much you pay"
if user_money > 10:
    print percent2, "  is how much you pay"
print "\n\n"









gender=  raw_input("What is your gender? M=male and F=female: ")
if gender == 'F':
    uwere_abletojoin=easygui.msgbox ("OK, you are a female.")
    age=int(easygui.integerbox("What is your age?"))
    if 10<=age<=12:
        easygui.msgbox ("You are eligible to join the team.")
    else:
        easygui.msgbox ("Sorry, you can not join the team")
else:
    easygui.msgbox ("You can not join the team.")
print "n\n"






size_of_tank= easygui.integerbox("What is the size of your tank?")
percent_full= float(easygui.integerbox("How much percent full is it?"))
km_per_lit= easygui.integerbox("What is one kilometer per litter?")
multi1= (percent_full/100)*size_of_tank
product= int(km_per_lit * multi1) 
length= easygui.msgbox("You can go another   " + str(product) + "   km")  
if product >= 200:
    print length
    easygui.msgbox ("""The next gas station is 200 km away,
                    You can wait for the next gas station""")
else:
    print length
    easygui.msgbox("Get gas now!!!")
    















