name = 'Tony DiMaggio'
age = 40 #Not a Lie
height = 78 # Inches
weight = 255 # lbs
eyes = "Brown"
teeth = "White"
hair = 'Salt and Pepper' # more salt than pepper these days

#convert inches to cm
cm = (height * 2.54)
kg = (weight * 0.453)

print "Let's talk about %s." % name
print "He's %d inches tall." % height
print "In metric he's %d cm tall." % cm
print "He's %d pounds heavy." % weight
print "In metric he's %d kg heavy." % kg
print "He could stand to lose a few."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "He's teeth are usually %s depending on the coffee." % teeth

#this line is tricky, try to get it exactly right
print "If I add %r, %r, and %d I get %d." % (age, height, weight, age + height + weight)
