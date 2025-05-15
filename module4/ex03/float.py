#!/usr/bin/env python3

numb = (input( "give me a number: "))

try:
	numb = float(numb)
	if numb.is_integer():
 		print ("this number is an integer")
	else:
 		print ("this number is a decimal")
except ValueError:
 	print ("this is not a number")