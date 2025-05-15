#!/usr/bin/env python3
import sys

n = len(sys.argv)
if n != 2:
    print("none")

for i in range (1, n):
    if str(sys.argv[i]):
        print (sys.argv[i])
        break

