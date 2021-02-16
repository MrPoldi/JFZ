import re
import sys

regex = r".*19[0-9]{2} r\."

for line in sys.stdin:
    if re.search(regex, line):
        print(line.rstrip("\n"))
