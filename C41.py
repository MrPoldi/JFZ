import re
import sys


regex = r"(^1 rok$)" \
        r"|(^(([1-9][0-15-9])|([5-9])) lat$)" \
        r"|(^1(([0-1][0-15-9])|(1?[2-4])) lat$)" \
        r"|(^1((0[2-4])|(2[2-3])) lata$)" \
        r"|(^[2-9]?[2-4] lata$)" \
        r"|(^120 lat$)"

for line in sys.stdin:
    if re.match(regex, line):
        print("yes")
    else:
        print("no")
