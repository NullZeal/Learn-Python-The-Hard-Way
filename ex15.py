#This asks the commandline to import an argument value from the input
from sys import argv

#Declares 2 variables, script by default gets them name of the 
#script and filename is said to take the value of the argv
script, filename = argv

#this declares a txt var that contains the object of the file returned by the open(function)
#for a specific 'filename' file
txt = open(filename)

#prints string with filename at the end
print "\nHere's your file %r:\n" % filename

#prints the content of the txt object
print txt.read()

#prints a string
print "\nAnd here we go again!\n"

#declares a variable and put the user's input inside
file_again = filename

#puts an object containing a file specified by the user inside of a variable named txt_again
txt_again = open(file_again)

#use a function to print the content of the txt_again object value
print txt_again.read()

txt.close()
txt_again.close()

#Maybe it's better to have raw_input for a user and argv for a dev?