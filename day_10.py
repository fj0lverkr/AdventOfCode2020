DATA_SET = "datasets/day_10.txt"

with open(DATA_SET, "r") as f:
    data = f.read().splitlines()
    adapters = [int(a) for a in data]
    adapters.sort()
    adapters.append(adapters[-1] + 3)
    # start jumps_1 at 1 to account for the jump from 0 to 1
    jumps_1 = 1
    jumps_2 = 0
    jumps_3 = 0
    for i, adapter in enumerate(adapters):
        if i < len(adapters) - 1:
            next_adapter = adapters[i + 1]
            jump = next_adapter - adapter
            if jump == 1:
                jumps_1 += 1
            elif jump == 2:
                jumps_2 += 1
            elif jump == 3:
                jumps_3 += 1
            else:
                raise ValueError("Too many jumps!")
    print(f"Puzzle 1: {jumps_1 * jumps_3}.")
