name = 'Zed A. Shaw'
age = 35 # not a lie
height = 74 # inches
weight = 180.000 # lbs
weight_in_kilos = weight * 0.453
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

print "Let's talk about %s." % name
print "He's %d inches tall." % height
print "He's %d kilos heavy." % weight_in_kilos
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth

# this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (
    age, height, weight, age + height + weight)
    
