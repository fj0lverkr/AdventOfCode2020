"""
Puzzle 1:
Starting at the top-left corner of your map and following a slope of right 3 and down 1,
how many trees would you encounter?

Puzzle 2:

    Right 1, down 1.
    Right 3, down 1. (This is the slope you already checked.)
    Right 5, down 1.
    Right 7, down 1.
    Right 1, down 2.

Multiplied together.
"""

DATA_SET = "datasets/day_3_puzzle_1.txt"
TREE = "#"


def singe_slope(right, down):
    position = 0
    trees_encountered = 0
    with open(DATA_SET, "r") as file:
        i = 0
        data = file.read().splitlines()
        lines = len(data)
        while i < lines:
            line = data[i]
            if line[position] == TREE:
                trees_encountered += 1
            position += right
            if position >= len(line):
                position = position - len(line)

            i += down

        return trees_encountered


def multi_slope(slopes):
    multiplied_all_the_trees = 1
    for slope in slopes:
        multiplied_all_the_trees *= singe_slope(slope[0], slope[1])

    return multiplied_all_the_trees


if __name__ == "__main__":
    print(singe_slope(3, 1))
    print(multi_slope([(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]))
