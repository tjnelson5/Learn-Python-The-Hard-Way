from sys import argv

script, first, second = argv

state = raw_input("What is everything? ")

print "The script is called: ", script
print "Your first variable is: ", first
print "Your second variable is: ", second
print "According to you, everything is %r." % state
