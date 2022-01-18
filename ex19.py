def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print "You have %d cheeses!" % cheese_count
    print "You have %d boxes of crackers!" % boxes_of_crackers
    print "Man that's enough for a party!"
    print "Get a blanket.\n"
    

print "We can just give the function numbers directly:"
cheese_and_crackers(20,30)


print "OR, we can use variables from our script:"
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)


print "We can even do math inside too:"
cheese_and_crackers(10 + 20, 5 + 6)

print "And we can combine the two, variables and math:"
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)

def triple_data(data_to_triple):
    tripled_data = data_to_triple * 3
    print "%s will become %s when tripled!" % (data_to_triple, tripled_data)

triple_data(330)
triple_data("331")
triple_data(332)
triple_data(333)
triple_data(334)
triple_data("335")
triple_data("336")
triple_data(337)
triple_data(338)
triple_data(339)
triple_data("340")