#!/usr/bin/env python3
i=0
while i < 11:
	print ("table of", i,":", end=" ")
	f=0
	while f < 11:
		mult = i * f
		f+=1
		print(int(mult), end=" ")
	print()
	i+=1
