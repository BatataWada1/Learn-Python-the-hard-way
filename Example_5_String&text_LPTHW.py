x = "There are %d type of people." % 10
binary = "binary"
do_not = "don't"
y = "Those who know %s and those who %s. " % ( binary, do_not )

print x 
print y

print "I said: %r " % x

#will print y in '' 
print "I also said: '%s'." % y 

hil = False
joke_evaluation = "Isn't that joke so funny? !%r"

print joke_evaluation % hil 

w = "This is the left side of ..."
e = "a string with right side."

print w + e
