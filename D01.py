import re
import sys


def substitute_letters(string: str):
    result = ""
    for char in string:
        if re.match(r'[a-ząćęłńóśźż]', char):
            result += char.capitalize()
        elif re.match(r'[A-ZĄĆĘŁŃÓŚŹŻ]', char):
            result += char.lower()
        else:
            result += char
    return result


word = r"\w{2,}"
regex = r"(\w*[a-ząćęłńóśźż]+\w*[A-ZĄĆĘŁŃÓŚŹŻ]+\w*)|(\w*[A-ZĄĆĘŁŃÓŚŹŻ]+\w*[a-ząćęłńóśźż]+\w*)"

for line in sys.stdin:
    line = re.sub(regex, lambda m: substitute_letters(m.group()), line)
    print(line.rstrip('\n'))
