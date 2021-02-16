import re
import sys

regex = r"^pies$|^pies | pies$| pies "

for line in sys.stdin:
    if re.search(regex, line, re.I):
        print(line.rstrip("\n"))
