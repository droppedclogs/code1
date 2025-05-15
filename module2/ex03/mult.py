#!/usr/bin/env python3
num1 = float(input ("enter first number: "))
num2 = float(input ("enter second number: "))
mult = num1 * num2
print (num1, "x", num2, "=", mult)
if mult > 0:
	print ("the resut is positive")
elif mult < 0:
	print ("the result is negatve")
else:
	print ("the result is positive and negative")
