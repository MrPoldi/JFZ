import re
import sys


lower_regex = r"[a-ząćęłńóśźż]"
capital_regex = r"[A-ZĄĆĘŁŃÓŚŹŻ]"
digit_regex = r"[0-9]"


def count_chars(string):
    lower = len(re.findall(lower_regex, string))
    capital = len(re.findall(capital_regex, string))
    digit = len(re.findall(digit_regex, string))
    rest = len(string) - lower - capital - digit
    return str(lower) + " " + str(capital) + " " + str(digit) + " " + str(rest)


for line in sys.stdin:
    print(count_chars(line.rstrip("\n")))
