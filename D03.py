import re
import sys


capital_regex = r"\b[A-ZĄĆĘŁŃÓŚŹŻ]+\w*"
lower_regex = r"\b[a-ząćęłńóśźż]+\w*"


def count_words(string):
    lower = len(re.findall(lower_regex, string))
    capital = len(re.findall(capital_regex, string))
    return str(lower) + " " + str(capital)


for line in sys.stdin:
    print(count_words(line))



