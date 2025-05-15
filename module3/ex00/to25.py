#!/usr/bin/env python3
var1 = float(input ("enter a number less than 25:\n "))
if var1 > 25:
	print ("Error")
while var1 < 26:
	print("inside the loop, my variable is ",int(var1))
	var1 += 1
	if var1 == 26:
		break
