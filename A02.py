import sys


def contains_pies(string):
    string = string.lower()
    if string.startswith("pies "):
        return True
    elif string.endswith(" pies"):
        return True
    elif " pies " in string:
        return True
    elif string.rstrip("\n") == "pies":
        return True
    else:
        return False


for line in sys.stdin:
    if contains_pies(line):
        print(line.rstrip("\n"))
