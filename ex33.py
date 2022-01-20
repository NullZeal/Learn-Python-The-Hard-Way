#def listCreator(increment):
#
#    numbers = []
#    banana = 100
#    i = 0
#    
#    while i < banana:
#        print "At the top i is %d" % i
#        numbers.append(i)
#        
#        i += increment
#        print "Numbers now: ", numbers
#        print "At the bottom i is %d" % i
#        
#    print "The numbers: "
#    
#    for num in numbers:
#        print num
#    
#    return numbers
#
#listCreator(10)

# SEPARATOR

def listCreator():

    listName = []
    
    for i in range(0,6):
        listName.append(i)
        print "listName numbers now: ", listName
        
    print "The numbers: "
    
    for num in listName:
        print num
    
    return listName

listCreator()