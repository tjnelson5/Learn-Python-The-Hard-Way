from sys import argv

script, filename = argv

filetoread = open(filename, 'r')

filecontent = filetoread.read()

print "The file says the following:\n %s" % filecontent