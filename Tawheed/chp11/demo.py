print_number = int(raw_input("Enter some number: "))
while print_number != 0:
    print "I shall print hello"
    for i in range(0,print_number):
        print "Hello"
    print_number = int(raw_input("Enter some number: "))    
print "Goodbye"
