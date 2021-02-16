import re
import sys


regex = r"(\W*\w+\b\W*)(\w+\b\W*)(\w+)(.*)"


def substitute(m):
    string = re.sub(r".", "x", m.group(3))
    return re.sub(regex, r"\1\2"+string+r"\4", m.group(0))


for line in sys.stdin:
    match = re.search(regex, line)
    if match:
        print(substitute(match).rstrip("\n"))
    else:
        print(line.rstrip("\n"))
