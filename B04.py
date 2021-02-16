import re
import sys

regex = r"\d+"

numbers = list()

for line in sys.stdin:
    numbers = re.findall(regex, line)
    if numbers:
        print(" ".join(numbers))

