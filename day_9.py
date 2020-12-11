"""
Part1:
The first step of attacking the weakness in the XMAS data is to find the first number in the list (after the preamble)
which is not the sum of two of the 25 numbers before it. What is the first number that does not have this property?

Part 2:
The final step in breaking the XMAS encryption relies on the invalid number you just found: you must find a contiguous
set of at least two numbers in your list which sum to the invalid number from step 1.
Then find the sum of the largest an smallest number in this range.
"""

DATA_SET = "datasets/day_9.txt"
PRE = 25


def test_number(n: int, p: list) -> bool:
    for i in range(len(p)):
        for j in range(i + 1, len(p)):
            if int(p[i]) + int(p[j]) == n:
                return True
    return False


def contiguous_range(n: int) -> list:
    with open(DATA_SET, "r") as f:
        data = f.read().splitlines()
        for i in range(len(data)):
            sum_of_elements = 0
            for j in range(i, len(data)):
                sum_of_elements += int(data[j])
                if sum_of_elements == n:
                    return [int(num) for num in data[i:j+1]]


with open(DATA_SET, "r") as file:
    lines_to_keep = file.read().splitlines()
    lines = lines_to_keep
    while True:
        preamble = lines[:PRE]
        test_me = int(lines[PRE])
        if test_number(test_me, preamble):
            lines.pop(0)
        else:
            print(f"{test_me} failed the test.")
            break
    c_items = contiguous_range(test_me)
    c_items.sort()
    print(f"Break the code: {sum([c_items[0], c_items[-1]])}!")
