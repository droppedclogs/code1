#!/usr/bin/env python3
import re
import sys

if len(sys.argv) == 3:
    matches = re.findall(sys.argv[1], sys.argv[2])
    print(len(matches))
else:
    print("none")