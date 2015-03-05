name = 'Tommy Nelson'
age = 33 # not a lie
height = 74 # inches
height_cm = height * 2.54
weight = 180 # lbs
weight_kg = weight * 0.454
eyes = 'Brown'
teeth = 'White'
hair = 'Brown'

print "Let's talk about %s." % name
print "He's %d cm tall." % height_cm
print "He's %.1f kg heavy." % weight_kg
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth

# this line is tricky, try to get it exactly right
print "If I add %d, %d and %d I get %d." % (age, height, weight, age + height + weight)