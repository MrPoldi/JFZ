import re
import sys


for line in sys.stdin:
    if re.search(r"Hamlet", line):
        print(line.rstrip("\n"))
