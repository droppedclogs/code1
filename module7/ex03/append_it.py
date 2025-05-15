#!/usr/bin/env python3
import re
import sys


args = sys.argv[1:]

for i in args:
    search = re.search(r'ism+$', i)
    if bool(search) == True:
        pass
    else:
        #print(f"{i}")

        print(f"{i}ism")

