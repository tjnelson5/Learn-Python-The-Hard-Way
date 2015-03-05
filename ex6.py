# This line creates a string stating that there are two types of people with 2 in binary
x = "There are %d types of people." % 10
# create a string variable called binary that is also equal to binary
binary = "binary"
# create a string variable that is equal to "don't"
do_not = "don't"
# Build a string using the two variables above
y = "Those who know %s and those who %s." % (binary, do_not)

# print the two strings from above
print x
print y

# print the strings again with some additional text
print "I said: %s." % x
print "I also said: '%s'." % y

# About to tell a joke: create a variable that states whether it is funny or not
hilarious = False
# Create a string that states if the joke is funny
joke_evaluation = "Isn't that joke so funny?! %r"

#print the evaluation of the joke
print joke_evaluation % hilarious

# create a string in two halves
w = "This is the left side of..."
e = "a string with a right side."

# print the entire string
print w + e