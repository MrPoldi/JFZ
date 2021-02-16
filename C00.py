import re
import sys


regex = r"(^[-]?(([1-9][0-9]*)|([1-9]*))[50]$)|(^0$)"

for line in sys.stdin:
    if re.match(regex, line):
        print("yes")
    else:
        print("no")
