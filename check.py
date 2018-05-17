#! usr/bin/env python2

import os
ch=raw_input("Enter a word :")
for file in os.listdir("//bin/"):
    if file.endswith(ch):
        print "sorry! It is a command"
	exit()
else:
	print "This is not a command"
