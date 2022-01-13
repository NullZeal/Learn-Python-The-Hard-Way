from sys import argv

script, filename = argv

print "We're goin to read %r." % filename

print "Opening the file..."
target = open(filename)

print target.read()
target.close()
