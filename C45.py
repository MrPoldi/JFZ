import re
import sys


regex = r"^(([A-ZĆŁŚŹŻ][a-zćłśźż]*[^a\d\s] )|(Kosma )|(Jarema ))([A-ZĆŁŚŹŻ][a-zćłśźż]+)$"

for line in sys.stdin:
    match = re.match(regex, line)
    if match:
        print(match.group(5))
    else:
        print("<NONE>")
