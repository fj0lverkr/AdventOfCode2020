DATA_SET = "datasets/day_8.txt"


def read_instructions() -> list:
    with open(DATA_SET, "r") as file:
        instructions = []

        for line in file.read().splitlines():
            command = line.split(" ")
            instruction = [command[0], command[1], False]
            instructions.append(instruction)
        return instructions


def run_instructions(inst: list, pos: int = 0, acc: int = 0):
    accumulator = acc
    current_instruction = inst[pos]
    command, argument, has_run = current_instruction
    if has_run:
        print(f"Final accumulator value: {accumulator}.")
        return None
    elif command == "acc":
        accumulator += int(argument)
        inst[pos][2] = True
        run_instructions(inst, pos + 1, accumulator)
    elif command == "jmp":
        inst[pos][2] = True
        run_instructions(inst, pos + int(argument), accumulator)
    elif command == "nop":
        inst[pos][2] = True
        run_instructions(inst, pos + 1, accumulator)
    else:
        raise Exception("Invalid command")


def reset(inst: list, swap: int):
    new_swap = calculate_swap(inst, swap)
    for i, _ in enumerate(inst):
        inst[i][2] = False
    run_instructions_safe(inst, new_swap)


def calculate_swap(inst: list, swap: int) -> int:
    for i, instruction in enumerate(inst):
        if i > swap and instruction[0] != "acc":
            return i
    return -1


def run_instructions_safe(inst: list, swap: int = 0):
    accumulator = 0
    pos = 0
    if swap < 0:
        exit(0)
    while True:
        if pos >= len(inst) or pos < 0:
            print(f"Final accumulator value: {accumulator}.")
            return None
        else:
            current_instruction = inst[pos]
            command, argument, has_run = current_instruction
            if has_run:
                break
            elif command == "acc":
                accumulator += int(argument)
                inst[pos][2] = True
                pos += 1
            elif command == "jmp" or (command == "nop" and pos == swap):
                inst[pos][2] = True
                if pos == swap:
                    pos += 1
                else:
                    pos += int(argument)
            elif command == "nop":
                inst[pos][2] = True
                if pos == swap:
                    pos += int(argument)
                else:
                    pos += 1
            else:
                raise Exception("Invalid command")
    reset(inst, swap)


if __name__ == "__main__":
    run_instructions(read_instructions())
    run_instructions_safe(read_instructions())
