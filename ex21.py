def add(a, b):
    print "ADDING %d + %d" % (a, b)
    return a + b
    
def subtract(a, b):
    print"SUBTRACTING %d - %d" % (a, b)
    return a - b
    
def multiply(a, b):
    print "MULTIPLYING %d * %d" % (a, b)
    return a * b
    
def divide(a, b):
    print "DIVIDING %d / %d" % (a, b)
    return a / b

    
print "Let's do some math with just functions!"

age = add(30, 5)
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)

print "Age: %d, Height: %d, Weight: %d, IQ: %d" % (age, height, weight, iq)


# A puzzle for the extra credit, type it in anyway
print "Here's a puzzle."

def calculate_final_answer():
    v1 = float(raw_input())
    v2 = float(raw_input())
    v3 = float(raw_input())
    v4 = float(raw_input())
    
    final_answer_p1 = divide(v1, 2)
    final_answer_p2 = multiply(v2, final_answer_p1)
    final_answer_p3 = subtract(v3, final_answer_p2)
    final_answer = add(v4, final_answer_p3)
    print "According to your characteristics, the final answer is : ", final_answer

calculate_final_answer()

