#!/usr/bin/env python3
import re
import sys

if len(sys.argv) == 1:
    print ("none")
else:
    print("parameters:", len(sys.argv) -1)

args=sys.argv[1:]
for i in args:
    print(i, len(i))