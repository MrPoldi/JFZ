import sys


def extract_numbers(string):
    nums = "".join((c if c in "0123456789" else " ") for c in string)
    list_of_nums = nums.split()
    return " ".join([str(num) for num in list_of_nums])


for line in sys.stdin:
    res = extract_numbers(line).rstrip("\n")
    if res != "":
        print(res)
