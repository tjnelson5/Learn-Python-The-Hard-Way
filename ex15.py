from sys import argv

# Take input from command line and create two string variables
script, filename = argv

# Open the file and create a file object
txt = open(filename)

print "Here's your file %r:" % filename
# read out the contents of the file to stdout.  This will read the whole
# file, because the command ends at the EOF character by default
print txt.read()
# always close the file - like gates in a field!
txt.close()

# create a new string variable from the prompt
print "Type the filename again:"
file_again = raw_input("> ")

# Create a new file object for this new file
txt_again = open(file_again)

# Same as above
print txt_again.read()
txt.close()
