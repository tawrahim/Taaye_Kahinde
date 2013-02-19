print "This is an example of a string being"
print "converted to a float"

#Ok so here, you are saving the string '12.34' into the variable string
string= "12.34" 

# When you get here you are just saving the formula to another variable called formula, remember that it is a string
formula="float(string)"

# This is where the magic happens, here you convert the string to a float and then save the converted answer to a variable called doit
doit= float(string)

# So here, I see that you are trying to print the string "12.34" but you said it is not working the way you want it to, because it is not printing it with the "". Well unfortuately that is not going to work because when you print a string, the quotation marks get ignored. To try out what I am saying, open up Idle => type this in name = "Kahinde" => now do print name, does the quaotation marks get printed when the name was printed? The answer is no! print simply ignores the quotation marks.
print "The string is," ,string

# If you want it to work, you have to do trick python by telling it that, you want a quotation to be printed around the variable. I think it is a little bit advance for now. The way you have it is fine and perfect. In any case if you are curious to find out how it is done, the line below demonstrates it.
print "The string is," , "\"" , string , "\""

print "This is the formula:"
print formula
print "This is the answer:"
print doit
