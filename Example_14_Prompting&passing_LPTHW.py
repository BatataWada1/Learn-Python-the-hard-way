from sys import argv

script, user_name = argv
prompt = '>'

print "Hi %s, I am the %s script." % (user_name, script)
print "I would like to ask you a few questions"
print "do you like me ? %s : Yes/No " % user_name
likes = raw_input(prompt)

print "where do you live %s: " % user_name
lives = raw_input(prompt)

print "What kind of computer do you have?: "
computer = raw_input(prompt)

print """
Alright, so you said %r about liking me.
You live in %r. Not sure where it is.
And you have a %r computer. Nice .
""" % (likes, lives, computer)