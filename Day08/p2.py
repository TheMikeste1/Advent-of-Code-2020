def parse_instructions(instructions):
    result = []
    for instruction in instructions:
        ins, amount = instruction.split(' ')
        amount = int(amount)
        result.append([ins, amount, 0])
    return result


def execute(instructions):
    total = 0
    i = 0
    while instructions[i][0] is not None:
        instruction = instructions[i]
        if instruction[2] > 0:
            raise Exception("Code looped!")
        instruction[2] += 1

        action = instruction[0]
        if action == "acc":
            total += instruction[1]
        elif action == "jmp":
            i += instruction[1] - 1
        i += 1
    return total


def copy_instructions(iterable):
    return [[j for j in i] for i in iterable]


def change_nop(instructions):
    for instruction in instructions:
        action = instruction[0]
        if action == "nop":
            instruction[0] = "jmp"
            c_ins = copy_instructions(instructions)
            try:
                return execute(c_ins)
            except:
                instruction[0] = "nop"
        elif action == "jmp":
            instruction[0] = "nop"
            c_ins = copy_instructions(instructions)
            try:
                return execute(c_ins)
            except:
                instruction[0] = "jmp"

    i = 0
    while instructions[i][0] is not None:
        instruction = instructions[i]
        action = instruction[0]

        if action == "nop":
            instruction[0] = "jmp"
            c_ins = copy_instructions(instructions)
            try:
                return execute(c_ins)
            except:
                instruction[0] = "nop"

        elif action == "jmp":
            instruction[0] = "nop"
            c_ins = copy_instructions(instructions)
            try:
                return execute(c_ins)
            except:
                instruction[0] = "jmp"
            i += instruction[1] - 1
        i += 1

    raise Exception("No change worked!")


with open("code.txt", "r") as file:
    instructions = file.read().splitlines()

instructions = parse_instructions(instructions)
# Add None to the end to serve as a break
instructions.append([None, 0, 0])

value = change_nop(instructions)
print(value)

exit(0)
