from sys import argv

script, user_name, user_job = argv
prompt = '--> '

print "Hi %s, I'm the %s script." % (user_name, script)
print "I'd like to ask you a few questions."
print "Do you like me %s %s?" % (user_job, user_name)
likes = raw_input(prompt)

print "Where do you live %s %s?" % (user_job, user_name)
lives = raw_input(prompt)

print "What kind of computer do you have?"
computer = raw_input(prompt)

print """
Alright, so you said %r about liking me.
You live in %r.  Not sure where that is.
And you have a %r computer. Nice.
Being a %r must be awesome, %r!
""" % (likes, lives, computer, user_job, user_name)