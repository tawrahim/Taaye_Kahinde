# Try changing the temperature-conversion program from chapter 5 to use GUI input and output instead of raw_input() and print.
#Write a program that asks for your name, then house number, then street, then city, then province/territory/state, then postal/zip code (all in EasyGui dialog boxes).
#The program should then display a mailing-style full address that looks something like this:


import easygui

fahrenheit = easygui.integerbox("Type in the temprature in Fahrenheit ")
celsius = (fahrenheit - 32) * 5.0 / 9
print fahrenheit , " degrees fahrenheit to celsius is ", celsius



