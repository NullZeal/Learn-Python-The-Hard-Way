#Test

print "I am 6'2\" tall." #escape double-quote inside string
print 'I am 6\'2" tall.' #escape single-quote inside string

tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."
fat_cat = """
I'll do%s a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
""" % "\r"

print tabby_cat
print persian_cat
print backslash_cat
print fat_cat

#while False:
#   for i in ["/", "-", "|", "\\", "|"]:
#      print "%s\r" % i,

print "Let\'s go mon cher %s" % "what\'s up!"