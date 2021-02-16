import sys


def contains_hamlet(string):
    if "Hamlet" in string:
        return True
    else:
        return False


for line in sys.stdin:
    if contains_hamlet(line):
        print(line.rstrip("\n"))
