"""
Puzzle 1 and 2:
How many passwords are valid according to their policies?
Policy 1: password needs to contain min and max occurrences of a given character.
Policy 2: password needs to have a given character at either position 1 or position 2.
"""

DATA_SET = "datasets/day_2_puzzle_1.txt"


def puzzle_1():
    with open(DATA_SET, "r") as file:
        valid_passwords = 0
        data = file.read().splitlines()

        for line in data:
            line_parts = line.split(" ")
            policy_min = int(line_parts[0].split("-")[0])
            policy_max = int(line_parts[0].split("-")[1])
            policy_letter = line_parts[1].rstrip(":")
            password = line_parts[2]

            if policy_min <= password.count(policy_letter) <= policy_max:
                valid_passwords += 1

        return valid_passwords


def puzzle_2():
    with open(DATA_SET, "r") as file:
        valid_passwords = 0
        data = file.read().splitlines()

        for line in data:
            line_parts = line.split(" ")
            policy_pos_1 = int(line_parts[0].split("-")[0]) - 1
            policy_pos_2 = int(line_parts[0].split("-")[1]) - 1
            policy_letter = line_parts[1].rstrip(":")
            password = line_parts[2]

            if (password[policy_pos_1] == policy_letter and password[policy_pos_2] != policy_letter) or \
                    (password[policy_pos_2] == policy_letter and password[policy_pos_1] != policy_letter):
                valid_passwords += 1

        return valid_passwords


if __name__ == "__main__":
    print(f"Solution 1 = {puzzle_1()}.")
    print(f"Solution 2 = {puzzle_2()}.")
