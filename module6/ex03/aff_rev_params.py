#!/usr/bin/env python3
import sys

args = sys.argv[1:]

lenar=len(sys.argv[1:])
if lenar < 2:
    print("none")
else:
    for i in range(len(args)):
        print(args[len(args) - i - 1])
        if ((len(args) - i - 1) == 0):
            break
        

"""     i = len(args) - 1
    while i >= 0:
        print(args[i])
        i -= 1
 """