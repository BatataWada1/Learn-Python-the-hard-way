days = "Mon Tue Wed Thu Fri Sat Sun"
months = "Jan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug\nSep\nOct\nNov\Dec"

print "Here are the days: ", days

#newline characters
print "Here are months : ", months 


#multiline 
print """
There's something going on here.
11 With the three double- quotes.
12 We'll be able to type as much as we like.
13 Even 4 lines if we want, or 5, or 6
"""
#Using %s 
print "Here are the days: %s " % days 

print "Here are the months: %s " % months

#Using %r 
print "Here are the days: %r " % days
print "Here are the months: %r" % months
