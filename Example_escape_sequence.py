print "\\"  #Escape Sequence \\ Description Prints Backslash

print "\'" 	# \`	#Prints single-quote

print "\""	#\" 	#Prints Double-quote

print "\a"	#\a		#ASCII bell makes ringing the bell alert sounds ( eg. xterm )	#no output just sound

print "abc" + "\bde" #\b #ASCII backspace ( BS ) removes previous character #abde

print "hello\fworld" #\f #hello
							#world
print "hello\nworld" #\n #hello
						 #world

print "123456\rXX_XX" #\r #ASCII carriage return (CR). Moves all characters after ( CR ) the the beginning of the line while overriding same number of characters moved. #XX_XX6

print "kulkarni\rmandar" #mandarni

print "mandar\tkulkarni" #\t #ASCII horizontal tab (TAB). Prints TAB #mandar  kulkarni

print "mandar\vkulkarni\vpune" #\v #ASCII vertical tab (VT). 

print "\043" #Prints character based on its octal value ##

print "\x41\x42\x43" #hexa value to print #ABC

escape1 = "\""
escape2 = "\'"

print "%r" % escape1 #print '"'

print "%s" % escape1 #print "

print "%r" % escape2 #print "'"

print "%s" % escape2 #print '

#while True:
# for i in ["/","- ","|","\\","|"]:
#	print "%s\a" % i,
	

	
	