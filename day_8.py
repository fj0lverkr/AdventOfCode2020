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
        exit(0)
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


if __name__ == "__main__":
    run_instructions(read_instructions())
