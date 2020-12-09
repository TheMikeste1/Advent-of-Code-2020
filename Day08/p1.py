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
            return total
        instruction[2] += 1

        action = instruction[0]
        if action == "acc":
            total += instruction[1]
        elif action == "jmp":
            i += instruction[1] - 1
        i += 1
    raise Exception("Code did not loop!")


with open("code.txt", "r") as file:
    instructions = file.read().splitlines()

instructions = parse_instructions(instructions)
# Add None to the end to serve as a break
instructions.append([None, 0, 0])

value = execute(instructions)
print(value)

exit(0)
