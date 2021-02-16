import re
import sys


def substitute_numbers(string):
    result = ''
    subs = {
        '0': 'a',
        '1': 'b',
        '2': 'c',
        '3': 'd',
        '4': 'e',
        '5': 'f',
        '6': 'g',
        '7': 'h',
        '8': 'i',
        '9': 'j'
    }
    for char in string:
        result += subs[char]
    return result


regex = r"[0-9]{4}"

for line in sys.stdin:
    line = re.sub(regex, lambda m: substitute_numbers(m.group()), line)
    print(line.rstrip('\n'))
