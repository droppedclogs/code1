#!/usr/bin/env python3
import re
import sys

if len(sys.argv) !=2:
    print("none")
    sys.exit(1)

string = sys.argv[1]
operation = re.findall(r"z", string )
if len(operation) == 0:
    print("none")
else:
    print (''.join(operation))