"""
Puzzle 1:
find the two entries that sum to 2020 and then multiply those two numbers together.
"""

DATA_SET = "datasets/day_1_puzzle_1.txt"
DATA_SUM_GOAL = 2020

expenses = []


def puzzle_1():
    with open(DATA_SET, "r") as file:
        data = file.read().splitlines()

        for i in range(int(len(data)/2)):
            for j in range(i+1, len(data)):
                expenses_sum = int(data[i]) + int(data[j])
                if expenses_sum == DATA_SUM_GOAL:
                    print(f"These expenses add up to {DATA_SUM_GOAL}: {data[i]} + {data[j]}.")
                    print(f"Puzzle answer is {int(data[i]) * int(data[j])}.")
                    break


"""
Puzzle 2:
find the three entries that sum to 2020 and then multiply those three numbers together.
"""


def puzzle_2():
    with open(DATA_SET, "r") as file:
        data = file.read().splitlines()

        for i in range(len(data)):
            for j in range(i + 1, len(data)):
                for k in range(j + 1, len(data)):
                    expenses_sum = int(data[i]) + int(data[j]) + int(data[k])
                    if expenses_sum == DATA_SUM_GOAL:
                        print(f"These expenses add up to {DATA_SUM_GOAL}: {data[i]} + {data[j]} +  {data[k]}.")
                        print(f"Puzzle answer is {int(data[i]) * int(data[j]) * int(data[k])}.")
                        break


if __name__ == "__main__":
    # puzzle_1()
    puzzle_2()
