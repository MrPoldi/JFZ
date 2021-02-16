import sys

dates = ["19" + str(x) + str(y) + " r." for x in range(0, 10) for y in range(0, 10)]


def contains_date(string):
    if any(date in string for date in dates):
        return True
    else:
        return False


for line in sys.stdin:
    if contains_date(line):
        print(line.rstrip("\n"))
