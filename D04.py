import re
import sys


regex = r"(\D*[0-9]+\D+)[0-9]+(.*)"

for line in sys.stdin:
    match = re.search(regex, line)
    if match:
        print(re.sub(regex, r"\1\2", line).rstrip("\n"))
    else:
        print(line.rstrip("\n"))
