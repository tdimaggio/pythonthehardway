#defines the cuntion with the arguments cheese_count and box_of_crackers
def cheese_and_crackers(cheese_count, box_of_crackers):
    print "You have %d cheeses!" % cheese_count #this variable is always the cheese
    print "You have %d boxes of crackers!" % box_of_crackers #this variable is always the boxes of crackers
    print "Man that's enough for a party!" #this always prints
    print "Get a blanket.\n" # this always prints


print "We can just give the function numbers directly:"
cheese_and_crackers (20, 30) # the numbers in parathesis is always cheese count and boxes


print "OR, we can use variables from our script:"
# this replaces the function with a variable
amount_of_cheese = 10 
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)

#here were just doing the math of the function
print "We can even do the math insides too:"
cheese_and_crackers(10 + 20, 5 + 6)

#here were taking the variable, passing to the function and then adding more math to it
print "And we can combine the two, variables and math:"
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)
