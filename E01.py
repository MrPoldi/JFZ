import sys


aut = dict()
accept = set()


def add_aut_info(string: str):
    temp = string.split()
    if len(temp) > 1:
        aut[(temp[0], temp[2])] = temp[1]
    else:
        accept.add(temp[0])


def aut_accept(word):
    curr_state = "0"
    for c in word:
        next_state = aut.get((curr_state, c), None)
        if next_state is not None:
            curr_state = next_state
        else:
            return False
    if curr_state in accept:
        return True
    else:
        return False


def aut_find_in_line(line):
    curr_state = "0"
    for c in line:
        next_state = aut.get((curr_state, c), None)
        if next_state is not None:
            curr_state = next_state
            if curr_state in accept:
                return True
        else:
            curr_state = "0"
    return False


add_aut_info("0 1 H")
add_aut_info("1 2 a")
add_aut_info("2 3 m")
add_aut_info("3 4 l")
add_aut_info("4 5 e")
add_aut_info("5 6 t")
add_aut_info("6")

for line in sys.stdin:
    if aut_find_in_line(line.rstrip("\n")):
        print("YES")
    else:
        print("NO")
