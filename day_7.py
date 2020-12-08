"""
Puzzle 1:
How many bag colors can eventually contain at least one shiny gold bag?

Puzzle2:
How many individual bags are required inside your single shiny gold bag?
"""

DATA_SET = "datasets/day_7_puzzle_1.txt"


class Bag:
    def __init__(self, name: str, children: list):
        self.name = name
        self.children = children

    def __repr__(self):
        total_children = 0
        for c in self.children:
            total_children += int(c[0])

        return f"{self.name} with {len(self.children)} unique children and {total_children} children in total:" \
               f"\n{self.children}"

    def reset_children(self, bags: list):
        for b in bags:
            if b.name == self.name:
                self.children = b.children
                break

    def print_children(self):
        print(self.children)

    def find_parents(self, bags: list) -> list:
        ancestors = []
        parents = []
        for b in bags:
            for c in b.children:
                if c[1] == self.name:
                    parents.append(b)
        for p in parents:
            ancestors.append(p)
            for p_p in p.find_parents(bags):
                ancestors.append(p_p)
        return ancestors

    def count_children(self, bags: list) -> int:
        if len(self.children) == 0:
            self.reset_children(bags)
        offspring = 0
        for ch in self.children:
            child_bag = Bag(ch[1], [])
            offspring += ch[0] + ch[0] * child_bag.count_children(bags)
        return offspring


def process_data() -> list:
    all_bags = []
    with open(DATA_SET, "r") as file:
        for rule in file.read().splitlines():
            child_bags_amount = []
            rule = rule.strip(".")
            parent_bag = rule.split(" contain ")[0].rstrip("s")
            container_rule = rule.split(" contain ")[1]
            child_bags = container_rule.split(", ")
            for child in child_bags:
                if child[0].isdigit():
                    amount = int(child[0])
                    child_name = child[2:].rstrip("s")
                    child_bags_amount.append((amount, child_name))
            all_bags.append(Bag(parent_bag, child_bags_amount))
    return all_bags


if __name__ == "__main__":
    my_bag = Bag("shiny gold bag", [])
    print(f"Puzzle 1: {len(set(my_bag.find_parents(process_data())))}.")
    print(f"Puzzle 2: {my_bag.count_children(process_data())}.")
