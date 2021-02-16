import re
import sys


regex = r"(^((?!555)\d{3})[ ]\d{3}[ ]\d{3}$)|(^((?!555)\d{3})[-]\d{3}[-]\d{3}$)"

for line in sys.stdin:
    if re.match(regex, line):
        print("yes")
    else:
        print("no")
