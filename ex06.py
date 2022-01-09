x = "There are %d types of people." % 10
binary = "binary"
do_not = "don't"
y = "Those who know %s and those who %s" % (binary, do_not)

print x
print y

print "I said: %r." % x
print "I also said: '%s'." % y

hilarious = False;
joke_evaluation = "Isin't that joke so funny?! %r"

#Prints variable joke_evaluation and replaces %r with a variable
print joke_evaluation % hilarious

w = "This is the left side of..."
e = "a string with a right side."

#Concatenation of w and e variables containing strings.
print w + e



