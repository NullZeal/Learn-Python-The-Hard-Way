print "You enter a dark room with two doors. Do you go through door #1 or door #2?"

door = raw_input("> ")

if door == "1":
    print "There's a giant bear here eating a cheese cake. What do you do?"
    print "1. Take the cake."
    print "2. Scream at the bear."
    
    bear = raw_input("> ")
    
    if bear == "1":
        print "The bear eats your face off. Good job!"
        print "Do you have anything else to say before you die?"
        last_words = raw_input("Last words: ")
        
        print "Magically, the pool of blood in which our hero died changes form and turns into the following letters : %s" % last_words
        print "You ressucitate and get to make another choice."
        print "1. Blueberries."
        print "2. Yellow jacket clothespins."
        print "3. Understanding revolvers yelling melodies."
        
        another_choice = raw_input("> ")

        if another_choice == "1" or another_choice == "2":
            print "Your body survives powered by a mind of jello. Good job!"
        else:
            print "The insanity rots your eyes into a pool of muck. Good job!"
        
    elif bear == "2":
        print "The bear eats your leg off. Good job!"
    else:
        print "Well, doing %s is probably better. Bear runs away." % bear
      
elif door == "2":
    print "You stare into the endless abyss at Cthulhu's retina."
    print "1. Blueberries."
    print "2. Yellow jacket clothespins."
    print "3. Understanding revolvers yelling melodies."

    insanity = raw_input("> ")

    if insanity == "1" or insanity == "2":
        print "Your body survives powered by a mind of jello. Good job!"
    else:
        print "The insanity rots your eyes into a pool of muck. Good job!"

else:
    print "You stumble around and fall on a knife and die. Good job!"