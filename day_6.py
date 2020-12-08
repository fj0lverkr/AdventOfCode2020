"""
Puzzle 1:
For each group, count the number of questions to which anyone answered "yes". What is the sum of those counts?

Puzzle 2:
For each group, count the number of questions to which everyone answered "yes". What is the sum of those counts?
"""

DATA_SET = "datasets/day_6_puzzle_1.txt"


def puzzle_1() -> int:
    total_unique_answers = 0
    with open(DATA_SET, "r") as file:
        for group in file.read()[:-1].split("\n\n"):
            group_answers = []
            for person in group.split("\n"):
                for letter in person:
                    group_answers.append(letter)
            total_unique_answers += len(set(group_answers))
    return total_unique_answers


def puzzle_2() -> int:
    total_shared_answers = 0
    with open(DATA_SET, "r") as file:
        for group in file.read()[:-1].split("\n\n"):
            group_answers = []
            for person in group.split("\n"):
                person_answers = []
                for letter in person:
                    person_answers.append(letter)
                    group_answers.append(person_answers)
            shared_answers = set(group_answers[0])
            for i in range(1, len(group_answers)):
                shared_answers = shared_answers.intersection(group_answers[i])
            total_shared_answers += len(shared_answers)
    return total_shared_answers


if __name__ == "__main__":
    print(f"Puzzle 1: {puzzle_1()}")
    print(f"Puzzle 2: {puzzle_2()}")
