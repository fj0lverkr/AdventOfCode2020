"""
The first step of attacking the weakness in the XMAS data is to find the first number in the list (after the preamble)
which is not the sum of two of the 25 numbers before it. What is the first number that does not have this property?
"""

DATA_SET = "datasets/day_9.txt"
PRE = 25


def test_number(n: int, p: list) -> bool:
    for i in range(len(p)):
        for j in range(i+1, len(p)):
            if int(p[i]) + int(p[j]) == n:
                return True
    return False


with open(DATA_SET, "r") as file:
    lines = file.read().splitlines()
    while True:
        preamble = lines[:PRE]
        test_me = int(lines[PRE])
        if test_number(test_me, preamble):
            lines.pop(0)
        else:
            print(f"{test_me} failed the test.")
            break



