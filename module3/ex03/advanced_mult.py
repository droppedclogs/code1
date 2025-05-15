#!/usr/bin/env python3
for i in range(0,11):
	print("table of", i, ":", end=" ")
	for f in range(0,11):
		mult = i * f
		f+=1
		print(int(mult), end=" ")
	print()
	i+=1
