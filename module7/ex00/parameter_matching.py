#!/usr/bin/env python3

import re
import sys

if len(sys.argv) == 2:
    yey = input("what was the parameter?: ")
    if yey == sys.argv[1]:
        print("good job!")
    else:
        print("nope, sorry")
else:
    print("none")